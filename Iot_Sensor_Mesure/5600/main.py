from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
import ubinascii              # Conversions between binary data and various encodings
import machine                # Interfaces with hardware components
from machine import Pin       # Define pin
import time
import dht


# BEGIN SETTINGS
# These need to be change to suit your environment
RANDOMS_INTERVAL = 20000    
last_random_sent_ticks = 0  
led = Pin("LED", Pin.OUT)   



# Wireless network ---------------------------------------------------------
# --------------------------------------------------------------------------
WIFI_SSID = "akraft"        # Wifi Name
WIFI_PASS = "akraft123"     # Wifi Password
# --------------------------------------------------------------------------



# Adafruit IO (AIO) configuration ------------------------------------------
# --------------------------------------------------------------------------
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "Ak155"
AIO_KEY = "aio_VDOB39YZREr9jikayIbkaiwVccsd"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id()) 
AIO_TEMPERATURE_FEED = "Ak155/feeds/temperature"        # Tempe    - SIP-3
AIO_MAGNETIC_FEED = "Ak155/feeds/magnetic-field-data"   # Magnetic - TO-92
AIO_HUMIDITY_FEED ="Ak155/feeds/humidity-dht11"         # Humidity - DHT11
# --------------------------------------------------------------------------



# END SETTINGS -------------------------------------------------------------
# --------------------------------------------------------------------------
MCP9700_PIN = 28   # Pin 34 for MCP9700 TO-92  - Temperature
TLV49645_PIN = 16  # Pin 21 for TLV49645 SIP-3 - Hall-effektsensor
DHT11_PIN = 27
# --------------------------------------------------------------------------



# Function to connect Pico to the WiFi ------------------------------------
# --------------------------------------------------------------------------
def do_connect():
    import network
    from time import sleep
    wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode

    if not wlan.isconnected():                  # Check if already connected
        print('connecting to network...')
        wlan.active(True)                       # Activate network interface
        wlan.config(pm = 0xa11140)
        wlan.connect(WIFI_SSID, WIFI_PASS)      # Your WiFi Credential
        print('Waiting for connection...', end='')
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip
# --------------------------------------------------------------------------

# New Code.

halleffect = Pin(TLV49645_PIN, mode=Pin.IN) #Hall-effekt sensor
tempsensor = machine.ADC(machine.Pin(MCP9700_PIN))
dht_sensor = dht.DHT11(machine.Pin(DHT11_PIN ))  # DHT11 sensor connected to Pin 27

try:
    ip = do_connect()
    print(ip)
except KeyboardInterrupt:
    print("Interupted")

adc = machine.ADC(MCP9700_PIN)
sf = 4095/65535 # Scale factor
volt_per_adc = (3.3 / 4095)
client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY, keepalive=30)
client.connect()


while True:
 
    # ------------------------------------
    # MCP9700 SIP-3 Calculations
    adc_value = tempsensor.read_u16()
    mv = adc.read_u16()
    adc_12b = mv * sf
    volt = adc_12b * volt_per_adc
    dx = abs(50 - 0)
    dy = abs(0 - 0.5)
    shift = volt - 0.5
    temp = shift / (dy / dx)
    print(temp)
    # ------------------------------------

    # ------------------------------------
    # Magnetic No Calculations
    print("Magnetic: " + str(halleffect.value()))
    # ------------------------------------

    # ------------------------------------
    # Read DHT11 sensor data
    dht_sensor.measure()
    humidity = dht_sensor.humidity()
    print("Humidity: " + str(humidity))
    # ------------------------------------
    
    try:
        client.publish(topic=AIO_TEMPERATURE_FEED, msg=str(temp))
        client.publish(topic=AIO_MAGNETIC_FEED, msg=str(halleffect.value()))
        client.publish(topic=AIO_HUMIDITY_FEED, msg=str(humidity))
        print("Data sent successfully!")
    except Exception as e:
        print("Error sending data:", str(e))

    time.sleep(10)