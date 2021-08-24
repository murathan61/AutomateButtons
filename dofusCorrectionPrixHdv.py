import pyautogui
import pygetwindow
import time
import PIL
import pytesseract
import mouse
import os


def takePriceImage():
    picture = pyautogui.screenshot()
    picture.save(r'C:\Users\yilma\Pictures\Python\testCodePython.png')


def cropPriceImage():
    pathToImagePrixHdv = r"C:\Users\yilma\Pictures\Python\prixHdv.png"
    pathToImageMonPrix = r"C:\Users\yilma\Pictures\Python\monPrix.png"
    im = PIL.Image.open(r'C:\Users\yilma\Pictures\Python\testCodePython.png')
    width, height = im.size
    prixHdv = im.crop((520, 643, 589, 675))
    prixHdv.save(pathToImagePrixHdv, quality=100)

    monPrix = im.crop((515, 278, 581, 305))
    monPrix.save(pathToImageMonPrix, quality=100)

    return pathToImagePrixHdv, pathToImageMonPrix


def extractedNumberToInt(extractedStrNumber):
    extractedIntNumber=""
    for c in extractedStrNumber:
        if c == "0":
            extractedIntNumber += "0"
        elif c == "1":
            extractedIntNumber += "1"
        elif c == "2":
            extractedIntNumber += "2"
        elif c == "3":
            extractedIntNumber += "3"
        elif c == "4":
            extractedIntNumber += "4"
        elif c == "5":
            extractedIntNumber += "5"
        elif c == "6":
            extractedIntNumber += "6"
        elif c == "7":
            extractedIntNumber += "7"
        elif c == "8":
            extractedIntNumber += "8"
        elif c == "9":
            extractedIntNumber += "9"

    extractedIntNumber = int(extractedIntNumber)

    return extractedIntNumber

def extractNumber(pathToImagePrixHdv, pathToImageMonPrix):
    pathToTesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    imgPrixHdv = PIL.Image.open(pathToImagePrixHdv)
    imgMonPrix = PIL.Image.open(pathToImageMonPrix)

    pytesseract.tesseract_cmd = pathToTesseract

    textPrixHdv = pytesseract.image_to_string(imgPrixHdv)
    textMonPrix = pytesseract.image_to_string(imgMonPrix)


    intPrixHdv = extractedNumberToInt(textPrixHdv)
    intMonPrix= extractedNumberToInt(textMonPrix)

    return intPrixHdv,intMonPrix

def replacePrice():
    dofusWindowTitle = "--sadilekiller-- - Dofus 2.60.4.13"
    dofusWindow = pygetwindow.getWindowsWithTitle(dofusWindowTitle)[0]
    dofusWindow.moveTo(0, 0)
    time.sleep(3)
    dofusWindow.activate()

    for i in range(0,11):
        mouse.move(868, 273+(i*40), absolute=True, duration=0.5)
        mouse.click('left')
        time.sleep(2)
        mouse.move(823, 198, absolute=True, duration=0.5)
        mouse.click('left')
        time.sleep(2)

        takePriceImage()
        cropPriceImage()
        pathToImagePrixHdv = r"C:\Users\yilma\Pictures\Python\prixHdv.png"
        pathToImageMonPrix = r"C:\Users\yilma\Pictures\Python\monPrix.png"
        intPrixHdv,intMonPrix = extractNumber(pathToImagePrixHdv,pathToImageMonPrix)
        time.sleep(1)

        if intPrixHdv+5 < intMonPrix:
            mouse.move(868, 273 + (i * 40), absolute=True, duration=0.5)
            mouse.click('left')
            time.sleep(2)
            pyautogui.write(str(intPrixHdv-1))
            time.sleep(1)
            mouse.move(555, 456, absolute=True, duration=0.5)
            mouse.click('left')


        mouse.move(868, 273+((i+1)*40), absolute=True, duration=0.5)
        mouse.click('left')
        os.remove(r"C:\Users\yilma\Pictures\Python\prixHdv.png")
        os.remove(r"C:\Users\yilma\Pictures\Python\monPrix.png")
        os.remove(r'C:\Users\yilma\Pictures\Python\testCodePython.png')
        time.sleep(2)
    time.sleep(5)
    dofusWindow.minimize()

