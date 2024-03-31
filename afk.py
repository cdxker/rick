import random, keyboard,time, pyautogui
import requests

value = 1
count = 0

pyautogui.FAILSAFE = False #!!!!!!!MAKE SURE TO SET TO TRUE IF TESTING ANYTHING AT ALL, YOU DRAG MOUSE TO CORNER OF SCREEN TO STOP THE SCRIPT WHEN ACTIVE
def catchInMatch(value): # timer of the script, change for loop to control runScript cals
    global count
    if value == 1:
        for _ in range(75):
            time.sleep(.03)
            if count == 1: # picks class once all bots are loaded in.
                keyboard.press('space')
                time.sleep(.1)
                keyboard.release('space')
                time.sleep(.1)
                keyboard.press('space')
                time.sleep(.1)
                keyboard.release('space')
                time.sleep(.4)
            runScript()

    if value == 0:
        for _ in range(1):
            count = 0

def runScript():
    global count

    end_y = random.randint(1, 800)

    if end_y % 2 == 0:
        pyautogui.click()

    if end_y % 9 == 8:
        keyboard.press('w')
        keyboard.release('w')

    keyboard.press('f')
    keyboard.release('f')
