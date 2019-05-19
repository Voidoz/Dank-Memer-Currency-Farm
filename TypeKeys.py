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
    html = urllib.request.urlopen("https://pastebin.com/raw/NUMtwjAx").read().decode()
    status = re.findall("KillSwitch1: (.*)", html) [-1]
    if status == "ON":
        killSwitchOn = 1
    elif status == "OFF":
        killSwitchOn = 0
def introProgram(running):
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
        print("")
    else:
        print("An error occured preventing the program from starting.")
        input("Press any key to continue.")
def beginProgram(killed):
    while killed == 0:
        checkKillSwitch()
        if killSwitchOn == 1:
            print("The kill switch has been activated and you are no longer able to use this program until is has been deactivated. Please contact the developer for more information.")
            input("Press any key to continue.")
            break
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
        
        checkKillSwitch()

        time.sleep(10)

checkKillSwitch()

if killSwitchOn == 0:
    introProgram(0)
    beginProgram(killSwitchOn)
elif killSwitchOn == 1:
    print("The kill switch has been activated and you are no longer able to use this program until is has been deactivated. Please contact the developer for more information.")
    input("Press any key to continue.")
else:
    print("ERROR: Kill Switch Not Found!")
    input("Press any key to continue.")