#imports
from pynput.keyboard import Key, Controller
import urllib.request
import re
import time
import random


keyboard = Controller()
postmemesSubList = ["d", "e", "n", "m", "r"]
html = urllib.request.urlopen("https://pastebin.com/raw/NUMtwjAx").read().decode()

def checkKillSwitch():
    global killSwitchOn
    status = re.findall("KillSwitch1: (.*)", html) [-1]
    if status == "ON":
        killSwitchOn = 1
    elif status == "OFF":
        killSwitchOn = 0
def beginProgram(running):
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
        input("Press any key to continue.")


    while running == 1:
        postmemeSub = random.choice(postmemesSubList)

        for char in "pls beg":
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.12)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)

        for char in "pls postmemes":

                keyboard.press(char)
                keyboard.release(char)
                time.sleep(0.12)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)

        for char in "{}".format(postmemeSub):

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

checkKillSwitch()

if killSwitchOn == 0:
    beginProgram(0)
elif killSwitchOn == 1:
    print("The kill switch has been initiated and you are no longer able to use this program. Please contact the developer for more information.")
    input("Press any key to continue.")
else:
    print("ERROR: Kill Switch Not Found!")
    input("Press any key to continue.")