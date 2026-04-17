from gpiozero import LED, Button
from time import sleep

ir = Button(17)   # IR sensor OUT
led = LED(27)     # LED

while True:
    if ir.is_pressed:   # Object detected
        print("Object Detected")
        led.on()
    else:
        print("No Object")
        led.off()
    
    sleep(0.2)
