# DHT22USB

- ### Temperature, Humidity Sensor DHT22 on RPi Pico
If you want to use DHT22 sensor on long cable, copy two files PicoDHT22.py and main.py to RPi Pico.

Connect the DHT22 sensor to the i2C RPi Pico port using wiring diagram below.

 - ### Wiring diagram
```
RPi Pico  [GP22 Pin 29]------------------------------ [VCC]  BME280
RPi Pico  [GP20 Pin 26] ----------------------------- [SDA]  BME280
RPi Pico  [GND  Pin 38] ----------------------------- [GND]  BME280
```
Connect PC with the RPi Pico together with the USB cable.
```
DHT22 [i2c] <------> [i2C] RPi Pico [USB] <--------------> RPi [USB]
```

Select proper USB port number in RPiMS configuration.

## Usefull links

* [Micropython DHT22](https://github.com/danjperron/PicoDHT22/blob/main/DHT22.py)
* [Raspberry Pi Pico -- DHT22 (AM2302) Temperature Sensor -- OLED Display](https://www.instructables.com/Raspberry-Pi-Pico-DHT22-AM2302-Temperature-Sensor-/)

## B.o.M - Bill of Materials

* [DHT22](https://botland.store/multifunctional-sensors/4920-temperature-and-humidity-sensor-dht22-am2302-module-cables-waveshare-11092-5903351242479.html) - 1 pcs
* [Raspberry Pico](https://botland.store/raspberry-pi-pico-modules-and-kits/18767-raspberry-pi-pico-rp2040-arm-cortex-m0-0617588405587.html) - 1 pcs
* [RPi Pico and Sensor Case](https://www.tme.eu/pl/en/details/pp73g/enclosures-for-alarms-and-sensors/supertronic/) - 1 pcs
* [MicroUSB B-A cable](https://botland.store/usb-20-cables/6417-microusb-b-a-cable-in-white-braid-esperanza-eb181w-2m-5901299920107.html) - 1 pcs
