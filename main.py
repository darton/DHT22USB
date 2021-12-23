from machine import Pin
from PicoDHT22 import DHT22
from utime import sleep_ms

sleep_ms(1000)
sid = 'DHT22'

DHT22_VCC = Pin(22, Pin.OUT)
DHT_DATA_PIN = Pin(20,Pin.IN,Pin.PULL_UP)

dht_sensor = DHT22(DHT_DATA_PIN,DHT22_VCC,dht11=False)

while True:
    T,H = dht_sensor.read()
    if T is not None and H <= 100:
        t,h = (int(float(T)*10),int(float(H)*10))
        print(sid,t,'°C',h,'%', 10)
    else:
        print(' SENSOR ERROR')
    sleep_ms(2000)
