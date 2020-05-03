# code for micropython 1.10 on esp8266

import random

import machine
import st7789py as st7789
import time


spi = machine.SPI(1, baudrate=10000000, polarity=1, sck=machine.Pin(18), miso=machine.Pin(19), mosi=machine.Pin(23))
display = st7789.ST7789(
        spi, 240, 240,
        reset=machine.Pin(5, machine.Pin.OUT),
        dc=machine.Pin(15, machine.Pin.OUT),
    )
display.init()

while (1):
    display.fill(st7789.color565(random.getrandbits(8),random.getrandbits(8),random.getrandbits(8),),)
    time.sleep(2)


