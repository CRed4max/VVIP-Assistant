import os
import keyboard
def CloseBrowserTab():
    os.system("taskkill /im chrome.exe /f")
def CloseMicrosoftBrowser():
    os.system("taskkill /im msedge.exe /f")
def CloseBraveBrowser():
    os.system("taskkill /im brave.exe /f")
def CloseFirefoxBrowser():
    os.system("taskkill /im firefox.exe /f")
def CloseTheCurrentTab():
    keyboard.press_and_release('ctrl+w')