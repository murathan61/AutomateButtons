#How to automate buttons clicking on one window
import pyautogui
import time
import keyboard
import pygetwindow


def clickTwoButtons(firstButton, secondButton):
    dofusWindowTitle = "--sadilekiller-- - Dofus 2.60.4.13"
    dofusWindow = pygetwindow.getWindowsWithTitle(dofusWindowTitle)[0]
    dofusWindow.moveTo(0, 0)
    time.sleep(1)
    dofusWindow.activate()
    while not (keyboard.is_pressed('q') or keyboard.is_pressed("Q")):
        for i in range(3):
            pyautogui.press(str(firstButton))
            time.sleep(1)
        for i in range(3):
            pyautogui.press(str(secondButton))
            time.sleep(1)
        time.sleep(3)
