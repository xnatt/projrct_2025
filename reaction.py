# reaction.py (基础版)
from gpiozero import LED, Button
from time import sleep, time
from random import uniform

led = LED(4)
left_button = Button(14)
right_button = Button(15)

left_name = input("Left player name: ")
right_name = input("Right player name: ")

def game_loop():
    led.on()
    sleep(uniform(5, 10))
    led.off()
    
    while True:
        if left_button.is_pressed or right_button.is_pressed:
            return

# 修改部分（第23-28行）
left_score = 0
right_score = 0

def pressed(button):
    global left_score, right_score
    if button.pin.number == 14:
        print(f"{left_name} wins this round!")
        left_score += 1
    else:
        print(f"{right_name} wins this round!")
        right_score += 1

left_button.when_pressed = pressed
right_button.when_pressed = pressed

while True:
    game_loop()
    sleep(1)
