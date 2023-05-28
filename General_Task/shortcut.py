import keyboard;
import pyautogui
import random;
import os;
# kb.send("windows+d")
# keyboard.write("Python Programming is always fun!", delay=0.1)
def ShutDown():
    # print("Enter Number of Seconds to Shutdown System: ")
    # sec = int(input())
    sec=3
    strOne = "shutdown /s /t "
    strTwo = str(sec)
    str1 = strOne+strTwo
    os.system(str1)
def Restart():
    # print("Enter Number of Seconds to Restart the System: ")
    # sec = int(input())
    sec=3
    strOne = "shutdown /r /t "
    strTwo = str(sec)
    str1 = strOne+strTwo
    os.system(str1)
def CloseTheApplication():
    keyboard.send("alt+F4, space")
def Escape():
    keyboard.send('Esc')
def SearchInBrowser():
    keyboard.send('ctrl+E')
def ChangeTab():
    keyboard.send('alt+tab')
def CapsLock():
    keyboard.send('caps lock')
def NumsLock():
    keyboard.send('num lock');
def ScreenShot():
    myScreenshot = pyautogui.screenshot()
    k = random.randint(0,10000000);
    myScreenshot.save(r'C:\Images\Screenshot\screenshot_'+str(k)+'.png')

# ChangeTab()
# openApplication()
# numLock()
# ScreenShot()
# ShutDown()
# Restart()
# capsLock()
# CloseTab()

























































































































































































