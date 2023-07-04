# Visualizing data from sensors


Anton Kraft

ak255ic

# Overview

This reports presents my project from the course Applied Iot from Linnaeus University. This report will cover a wide range of topics necessary to building your own device, such as the materials needed, the code making it work and finally how to send and receive data.

This project is not that long nor that difficult to perform, so the average time to complete should be around 3-5 hours depending on prior knowledge when it comes to programming.

# Objective

The objective of this project is to use a microcontroller to measure different types of values, such as temperature, humidity and magnetic field data. The goal of this project is to measure more values than your traditional thermometer and being able to view the data in another location through Adafruit.

# Material

Everything I’ve used in this project can be found in the **[LNU – 1DT305 Standard Kit (2023)](https://www.electrokit.com/en/product/lnu-1dt305-standard-kit-2023/)**

But if you’d like to buy them separately I have provided a table below.



| Device          | Amount Needed             | Total Price             | Where to buy    |
|:-------------:|:-------------:|:-------------:|:-------------:|
| Rasberry Pico W    | 1     | 98.00 SEK     |   [Electrokit](https://www.electrokit.com/en/product/raspberry-pi-pico-w/)
| MCP9700 TO-92      | 1     | 10.75 SEK     |   [Electrokit](https://www.electrokit.com/en/product/mcp9700-e-to-to-92-temperature-sensor/) |
| TLV49645 SIP-3     | 1     | 18.00 SEK     |   [Electrokit](https://www.electrokit.com/en/product/tlv49645-sip-3-hall-effektsensor-digital-2/) |
| DHT11 Sensor       | 1     | 49.00 SEK     |   [Electrokit](https://www.electrokit.com/en/product/digital-temperature-and-humidity-sensor-dht11/) |
| USB A-male to MicroB | 1     | 39.00 SEK     |   [Electrokit](https://www.electrokit.com/en/product/usb-cable-a-male-microb-male-1-8m/) |
| Breadboard 400     | 2     | 98.00 SEK (49 Each)    |   [Electrokit](https://www.electrokit.com/en/product/solderless-breadboard-400-tie-points/) |
| Jumper wires     | 9     | 29.00    |   [Electrokit](https://www.electrokit.com/en/product/jumper-wires-1-pin-male-male-150mm-10-pack/) |

#

## **Fig.1 Rasberry Pico W**

The Raspberry Pi Pico W is an affordable microcontroller board that serves as the foundation for various projects. With its built-in wireless networking capabilities, it offers convenient connectivity options.

<a href="url"><img src="https://www.electrokit.com/uploads/productimage/41019/41019110-1.jpg" align="middle" height="600" width="800" ></a>

#

## **Fig.2 MCP9700 TO-92**

The MCP9700 TO-92 is a small temperature sensor module commonly used in electronic projects. With its compact form factor and straightforward interface, it provides accurate temperature measurements. Its TO-92 package allows for easy integration into circuits, making it an ideal choice for temperature sensing applications.

<a href="url"><img src="https://www.electrokit.com/uploads/productimage/41011/41011628.jpg" align="middle" height="600" width="800" ></a>

#

## **Fig.3 TLV49645 SIP-3**

The TLV49645 SIP-3 is a compact magnetic sensor module widely used in various electronic applications. With its small size and convenient SIP-3 package, it offers precise magnetic field detection. The module is easily integrated into circuits, making it an excellent choice for projects requiring magnetic sensing capabilities.

<a href="url"><img src="https://www.electrokit.com/uploads/productimage/41015/41015964.jpg" align="middle" height="600" width="800" ></a>

#

## **Fig.4 DHT11 Sensor**

The DHT11 sensor is a commonly used module for measuring temperature and humidity in electronic projects. It is a cost-effective sensor that provides reliable and accurate readings. With its compact size and simple interface, the DHT11 sensor is widely employed in applications where monitoring environmental conditions is necessary.

<a href="url"><img src="https://www.electrokit.com/uploads/productimage/41015/41015728-1.jpg" align="middle" height="600" width="800" ></a>

#

## **Fig.5 USB A-male to MicroB**

The USB A-male to MicroB cable is a standard connector used for connecting devices with MicroB ports, such as the Raspberry Pi Pico W, to USB A ports. It enables data transfer and power delivery between devices. With its universal compatibility and convenient design, this cable is widely employed for connecting the Raspberry Pi Pico W, smartphones, tablets, and other peripherals to computers and chargers.

<a href="url"><img src="https://www.electrokit.com/uploads/productimage/41003/41003290.jpg" align="middle" height="600" width="800" ></a>

#

## **Fig.5 Breadboard 400**

The Breadboard 400 is a versatile prototyping tool used in electronics projects. With its 400 tie-points and easy-to-use design, it allows for quick and convenient circuit building without the need for soldering. The Breadboard 400 is widely used by hobbyists and professionals alike for testing and experimenting with various electronic components and connections.

<a href="url"><img src="https://www.electrokit.com/uploads/productimage/41012/41012199.jpg" align="middle" height="600" width="800" ></a>

#

## **Fig.6 Jumper wires**

Jumper wires are essential components that facilitate the connection between different electronic components on a breadboard, such as the Breadboard 400. These wires are used to establish electrical connections and provide flexibility in circuit design.

<a href="url"><img src="https://www.electrokit.com/uploads/productimage/41015/41015693.jpg" align="middle" height="600" width="800" ></a>


# Wiring

## **Fig.1 MCP9700 TO-92**

![image](https://github.com/Akraftt/IOT_Sensors/assets/90035332/89d206ad-afbe-47bd-87a0-1c7ff8be4165)


<a href="url"><img src="https://i.imgur.com/OEZxPa7.png" align="middle" height="600" width="800" ></a>

#


## **Fig.2 TLV49645 SIP-3**

![image](https://github.com/Akraftt/IOT_Sensors/assets/90035332/693d6f12-a79a-4b2a-a379-929ac55c7967)


<a href="url"><img src="https://i.imgur.com/Gn52EAZ.png" align="middle" height="" width="" ></a>


## **Fig.3 DHT11 Sensor**

![image](https://github.com/Akraftt/IOT_Sensors/assets/90035332/a3249866-2154-43f0-adc1-5bca143b0a6f)



<a href="url"><img src="https://i.imgur.com/Pu5MOOW.png" align="middle" height="" width="" ></a>

#



# Computer Setup: Installation

Any OS should work fine, but unfortunately I cannot verify this since I only use Windows 10 for this project. This project is focused around Visual Studio Code, since it is a very easy IDE for beginners to use. To start writing code the following steps below is a requirement.


* Install the most current version of [Node JS](https://nodejs.org/en) not LTS. Open cmd and enter ["node -v"](https://i.imgur.com/hjv598i.png) to verify your installation.
* Install the correct version of [Visual Studio Code](https://code.visualstudio.com/) depending on your OS.
* Navigate to the [Extensions](https://i.imgur.com/wYmMKGn.png) in Vs Code or simply press (Ctrl + Shift + X) & Search for pymakr and download the current version.

# Computer Setup: Flashing your Raspberry Pico W
* Download the [firmware](https://micropython.org/download/rp2-pico-w/), very important! choose the .uf2 file under **Releases** not **Nightly builds**!
* After downloading the file, connect the micro-USB to your Raspberry Pico W. **Do not connect the other end of the cable into your PC yet!**
* Hold down the BOOTSEL button on your Pico W meanwhile you connect the other end of the cable into your PC.
![image](https://github.com/Akraftt/IOT_Sensors/assets/90035332/3e82eb35-63c7-4db9-9a3f-60148e96f6a0)

* If done correctly a new file storage called **RPI-RP2** should open.
* Drag and drop your .uf2 file into this folder. If done correctly the folder should disappear and your Pico should disconnect and reconnect from your PC. If you have System Sounds you will hear the corresponding sounds.

# Computer Setup: Executing code.
The first and most important step to running code on your Pico W is to connect the device with PyMakr
![image](https://github.com/Akraftt/IOT_Sensors/assets/90035332/d9e159da-50fa-4374-ac3a-b1934c8476c0)

After connecting your Pico, you need to create a terminal. This where we will see the output from running the code.
![image](https://github.com/Akraftt/IOT_Sensors/assets/90035332/ff69b894-de04-40de-8bcc-0e5abb9e89f1)

Once the terminal has been created, we can test our device by running the following code:
```python
print("test")
```
![image](https://github.com/Akraftt/IOT_Sensors/assets/90035332/d01c0e28-2baf-4e03-a642-0a949360a313)

To easiest and most effective way to upload code to our device is done by:
1. Right click on the folder, in my case "5600"
2. Hover over pymakr
3. Click "Upload to device" which also can be done by pressing (Ctrl+Shift+S)
By uploading the entire folder we make sure every single change or newly written code is saved.
![image](https://github.com/Akraftt/IOT_Sensors/assets/90035332/e67e673e-7d7b-4c2c-b2f5-c21f1614fade)


Running the code on our device is done by:
1. Right click main.py
2. Hover over pymakr
3. Select "Run File on device"
![image](https://github.com/Akraftt/IOT_Sensors/assets/90035332/16e3311f-5ee6-4f39-b15b-403dcfb674ec)


# Platform
Before we move on to the code it is important to choose your platform. Personally I choose the Wi-Fi and Adafruit (MQTT) path, because it is the easiest one by far for a beginner. It requires relatively very little code in order to work.
If you are looking for a challenge I strongly recommend loRaWAN instead of Wi-Fi, because then your device is not dependent on a Wi-Fi connection which can be quite short if you want to measure things for example in your garden or further away from where you live.

# Code

There is a total of 4 files inside my project
* **main.py** - *Where the code is executed from*
* **boot.py** - *Where the connects to Wi-Fi (Empty in my case)*
* **credentials.py** - *Contains your ssid and password to your Wi-Fi*
* **mqtt.py** - *Provides functionality to connect to an MQTT server*

# main.py
Importing all necessary for this project.
```python
from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
import ubinascii              # Conversions between binary data and various encodings
import machine                # Interfaces with hardware components
from machine import Pin       # Define pin
import time
import dht
```

Adafruit IO (AIO) configurations.
```python
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "Ak155"
AIO_KEY = "Your-Key-Here"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id()) 
AIO_TEMPERATURE_FEED = "Your-Feed-Here"     # Tempe    - SIP-3
AIO_MAGNETIC_FEED = "Your-Feed-Here"        # Magnetic - TO-92
AIO_HUMIDITY_FEED ="Your-Feed-Here"         # Humidity - DHT11
```

Setting up our sensors.
```python
MCP9700_PIN = 28   # Pin 34 for MCP9700 TO-92  - Temperature
TLV49645_PIN = 16  # Pin 21 for TLV49645 SIP-3 - Hall-effektsensor
DHT11_PIN = 27
```
Passing the sensors in as arguments.
```python
halleffect = Pin(TLV49645_PIN, mode=Pin.IN) #Hall-effekt sensor
tempsensor = machine.ADC(machine.Pin(MCP9700_PIN))
dht_sensor = dht.DHT11(machine.Pin(DHT11_PIN ))  # DHT11 sensor connected to Pin 27
```

Function to connect to Wi-Fi.
```python
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
```

Actually connecting to the Wi-Fi
```python
try:
    ip = do_connect()
    print(ip)
except KeyboardInterrupt:
    print("Interupted")
```
And finally, we use our (AIO) configurations and do some calculations so the temperature is in celsius. The loop will run indefinitely and print and send data every 10 seconds.
```python
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
```


# Transmitting the data
The data is sent every 10 seconds to avoid exceeding Adafruits limit. And as previously mentioned the transmission is done through Wi-Fi using the MQTT protocol. 
```python
time.sleep(10)
```

# Presenting the data
All data is presented on Adafruit. In the image below we can see three different feeds, temperature, magnetic field data and finally humidity. 
![image](https://github.com/Akraftt/IOT_Sensors/assets/90035332/86106828-4f97-46ed-98b8-07b86d130cb4)

# Finalizing the design and reflections.
In the image below the final product of the project can be seen.
![image](https://github.com/Akraftt/IOT_Sensors/assets/90035332/477ed7de-37c7-4ea0-8c50-6de3e435ae18)

Overall the project was a success, I manage to connect a few censors and circuit them correctly along with some code so that their data was able to be sent and presented.

There were some issues in the beginning the I’ve managed to overcome with the help of a couple of teaching assistants. One them were that the boot file “boot.py” was not executed properly, thus everything had to be stored inside the main file. Another were that the Pico was not compatible with my main computer due to some Windows shell issues. Because of those issues the time towards the end got a bit hectic by everything worked out in the end.


