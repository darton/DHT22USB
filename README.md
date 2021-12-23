# DHT22USB

- ### Temperature, Humidity Sensor DHT22 on RPi Pico
If you want to use DHT22 sensor on long cable, copy two files PicoDHT22.py and main.py to RPi Pico.

Connect the DHT22 sensor to the i2C RPi Pico port using wiring diagram below.

 - ### Wiring diagram
```
RPi Pico  [GP22 Pin 29]------------------------------ [VCC ]  DHT22
RPi Pico  [GP20 Pin 26] ----------------------------- [DATA]  DHT22
RPi Pico  [GND  Pin 38] ----------------------------- [GND ]  DHT22
```
Connect PC with the RPi Pico together with the USB cable.
```
DHT22 <------> RPi Pico [USB] <--------------> RPi [USB]
```
Select proper USB port number in RPiMS configuration.

Output data format:

type of sensor, temperature value, temperature unit, humidity value, humidity unit, factor

The factor indicates by how much the read value should be divided

example 

DHT22 247 °C 201 % 10


## Usefull links

* [Micropython DHT22](https://github.com/danjperron/PicoDHT22/blob/main/DHT22.py)
* [Raspberry Pi Pico -- DHT22 (AM2302) Temperature Sensor -- OLED Display](https://www.instructables.com/Raspberry-Pi-Pico-DHT22-AM2302-Temperature-Sensor-/)
* [DHT111 and DHT22 tutorial](https://lastminuteengineers.com/dht11-dht22-arduino-tutorial/)

## B.o.M - Bill of Materials

* [DHT22](https://botland.store/multifunctional-sensors/4920-temperature-and-humidity-sensor-dht22-am2302-module-cables-waveshare-11092-5903351242479.html) - 1 pcs
* [Raspberry Pico](https://botland.store/raspberry-pi-pico-modules-and-kits/18767-raspberry-pi-pico-rp2040-arm-cortex-m0-0617588405587.html) - 1 pcs
* [RPi Pico and Sensor Case](https://www.tme.eu/pl/en/details/pp73g/enclosures-for-alarms-and-sensors/supertronic/) - 1 pcs
* [MicroUSB B-A cable](https://botland.store/usb-20-cables/6417-microusb-b-a-cable-in-white-braid-esperanza-eb181w-2m-5901299920107.html) - 1 pcs
