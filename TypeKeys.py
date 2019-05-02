#imports
from pynput.keyboard import Key, Controller
import time
import random


keyboard = Controller()
postmemesSubList = ["d", "e", "n", "m", "r"]
running = 0


print("Click into Discord now!")
print("Starting in:")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
running = 1

if running == 1:
    print("Program has started successfully and is typing!")
else:
    print("An error occured preventing the program from starting.")


while running == 1:
    postmemeSub = random.choice(postmemesSubList)

    for char in "pls beg":
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(0.5)

    for char in "pls postmemes {}".format(postmemeSub):

            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(0.5)

    for char in "pls deposit max":
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(0.5)

    for char in "pls search":
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(60)