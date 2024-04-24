#!pip install pynput
from pynput.mouse import Controller
from pynput.keyboard import Controller
# we can't use mouse & keyboard Controller at same time
from pynput.mouse import Listener
from pynput.keyboard import Listener

def Control_mouse():
    mouse = Controller()
    mouse.position = (100, 200)

def Control_keyboard():
    keyboard = Controller()
    keyboard.type("Hello World")

def save_keyboard_clicks_in_file(key):
    ch = str(key)
    with open("demo.txt", 'a') as f:
        f.write(ch)

def save_mouse_movement_in_file(x, y):
    key = str(f"\nposition of mouse = {x}, {y}")
    with open("demo.txt", 'a') as f:
        f.write(key)

def save_keyboard_clicks():
    with Listener(on_press=save_keyboard_clicks_in_file) as ch:
        ch.join()

def save_mouse_movement():
    with Listener(on_move=save_mouse_movement_in_file) as l:
        l.join()