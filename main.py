#How to automate buttons clicking on one window


import pyautogui
import time
import keyboard

if __name__ == '__main__':
    #pyautogui.press('capslock')
    while not (keyboard.is_pressed('q') or keyboard.is_pressed('Q')):
        for i in range(3):
            pyautogui.press('a')
            time.sleep(1)
        #time.sleep(3)
        for i in range(3):
            pyautogui.press('e')
            time.sleep(1)
        time.sleep(3)

    pyautogui.press('capslock')