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
| Breadboard 400     | 2     | 98.00 SEK (49 Each)    |   [Electrokit](https://www.electrokit.com/en/product/digital-temperature-and-humidity-sensor-dht11/) |
| Jumper wires     | 9     | 29.00    |   [Electrokit](https://www.electrokit.com/en/product/jumper-wires-1-pin-male-male-150mm-10-pack/) |

#

**Fig.1 Rasberry Pico W**

The Raspberry Pi Pico W is an affordable microcontroller board that serves as the foundation for various projects. With its built-in wireless networking capabilities, it offers convenient connectivity options.

<a href="url"><img src="https://www.electrokit.com/uploads/productimage/41019/41019110-1.jpg" align="middle" height="600" width="800" ></a>

#

**Fig.2 MCP9700 TO-92**

The MCP9700 TO-92 is a small temperature sensor module commonly used in electronic projects. With its compact form factor and straightforward interface, it provides accurate temperature measurements. Its TO-92 package allows for easy integration into circuits, making it an ideal choice for temperature sensing applications.

<a href="url"><img src="https://www.electrokit.com/uploads/productimage/41019/41019110-1.jpg" align="middle" height="600" width="800" ></a>

#

**Fig.3 TLV49645 SIP-3**

The MCP9700 TO-92 is a small temperature sensor module commonly used in electronic projects. With its compact form factor and straightforward interface, it provides accurate temperature measurements. Its TO-92 package allows for easy integration into circuits, making it an ideal choice for temperature sensing applications.

<a href="url"><img src="https://www.electrokit.com/uploads/productimage/41019/41019110-1.jpg" align="middle" height="600" width="800" ></a>

#

**Fig.4 DHT11 Sensor**

The MCP9700 TO-92 is a small temperature sensor module commonly used in electronic projects. With its compact form factor and straightforward interface, it provides accurate temperature measurements. Its TO-92 package allows for easy integration into circuits, making it an ideal choice for temperature sensing applications.

<a href="url"><img src="https://www.electrokit.com/uploads/productimage/41019/41019110-1.jpg" align="middle" height="600" width="800" ></a>

#

**Fig.5 USB A-male to MicroB**

The MCP9700 TO-92 is a small temperature sensor module commonly used in electronic projects. With its compact form factor and straightforward interface, it provides accurate temperature measurements. Its TO-92 package allows for easy integration into circuits, making it an ideal choice for temperature sensing applications.

<a href="url"><img src="https://www.electrokit.com/uploads/productimage/41019/41019110-1.jpg" align="middle" height="600" width="800" ></a>

#

**Fig.5 Breadboard 400**

The MCP9700 TO-92 is a small temperature sensor module commonly used in electronic projects. With its compact form factor and straightforward interface, it provides accurate temperature measurements. Its TO-92 package allows for easy integration into circuits, making it an ideal choice for temperature sensing applications.

<a href="url"><img src="https://www.electrokit.com/uploads/productimage/41019/41019110-1.jpg" align="middle" height="600" width="800" ></a>

#

**Fig.6 Jumper wires**

The MCP9700 TO-92 is a small temperature sensor module commonly used in electronic projects. With its compact form factor and straightforward interface, it provides accurate temperature measurements. Its TO-92 package allows for easy integration into circuits, making it an ideal choice for temperature sensing applications.

<a href="url"><img src="https://www.electrokit.com/uploads/productimage/41019/41019110-1.jpg" align="middle" height="600" width="800" ></a>
