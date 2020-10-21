# ESP32 & ST7789 tft_display driver for MicroPython
==================================

This is a MicroPython updated driver for 240x240 ST7789 display without CS pin. It also supports esp8266 Nodemcu board.
Original library Link is here: https://github.com/devbis/st7789py_mpy

If you create a project by esp32 and st7789 tft display
With micropython. This is the driver to interfacing
st7789 with esp32.

Examples
--------

#ESP32 st7789 micropython test
#Owner: Shuvabrata Dey

import machine
import st7789py
spi = machine.SPI(1, baudrate=10000000, polarity=1, sck=machine.Pin(18), miso=machine.Pin(19), mosi=machine.Pin(23))
display = st7789py.ST7789(spi, 240, 240, reset=machine.Pin(5, machine.Pin.OUT), dc=machine.Pin(15, machine.Pin.OUT))
display.init()
display.pixel(120, 120, st7789py.RED)
