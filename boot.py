# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from machine import Pin, SoftI2C
import ssd1306
import random



# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))

oled_width = 128
oled_height = 64
display = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
display.rotate(False)
display.fill(0)
for iTerator in range(20):
    display.line(30,30,random.randint(0, 55),random.randint(0, 55),1)
display.text('Calculus', 60, 10, 1)
display.text('SSD1306', 60, 22, 1)
display.text('128x64', 60, 34, 1)
display.text('v 0.02', 60, 48, 1)
display.show()


F1 = Pin(25, Pin.OUT)
F2 = Pin(26, Pin.OUT)
F3 = Pin(27, Pin.OUT)

F1.off()
F2.off()
F3.off()

C1 = Pin(22, Pin.IN, Pin.PULL_DOWN)
C2 = Pin(21, Pin.IN, Pin.PULL_DOWN)
C3 = Pin(19, Pin.IN, Pin.PULL_DOWN)
C4 = Pin(18, Pin.IN, Pin.PULL_DOWN)
C5 = Pin(17, Pin.IN, Pin.PULL_DOWN)
C6 = Pin(16, Pin.IN, Pin.PULL_DOWN)


Columns = [ C1, C2, C3, C4, C5, C6]
Files = [ F1, F2, F3]


Caracteres = [
    [["1","4","7","-","+","mode"],["2","5","8","0","*","del"],["3","6","9",".","/","eval"]],
    [["sin()","log()","^","F","pi","mode"],["cos()","log10()","exp()","'","e","del"],["tan()","v","sqrt()","ans","j","graph"]],
    [["A","D","T","X","(","mode"],["B","E","U","Y",")","del"],["C","F","V","Z","=","exe"]] ]
