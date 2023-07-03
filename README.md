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
