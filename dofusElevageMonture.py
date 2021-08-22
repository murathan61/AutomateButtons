#How to automate buttons clicking on one window
import pyautogui
import time
import keyboard


def clickTwoButtons(firstButton, secondButton):
    while not (keyboard.is_pressed(str(firstButton)) or keyboard.is_pressed(str(secondButton))):
        for i in range(3):
            pyautogui.press(str(firstButton))
            time.sleep(1)
        for i in range(3):
            pyautogui.press(str(secondButton))
            time.sleep(1)
        time.sleep(3)
