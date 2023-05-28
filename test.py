from FileManage.tasks.audio import AudioInput
from chat import chat
from Methods.renameMethod import renameMethod
from Methods.deleteMethod import deleteMethod
from Methods.openFileMethod import openFileMethod
from Methods.searchMethod import searchMethod
from Methods.createFileMethod import createFileMethod
from Methods.createFolderMethod import createFolderMethod
from Methods.zipMethod import zipMethod
from Methods.extractMethod import extractMethod
from Methods.copyPasteMethod import copyPasteMethod
from Methods.cutPasteMethod import cutPasteMethod

from General_Task import volume, brightness , shortcut, openApplication
from Brower_Tasks import close, open
from sendmail import *

import os
from gtts import gTTS
from pdfminer.high_level import extract_text
import gradio as gr
import speech_recognition as s_r

# print("ready to do your task.........")
# inp = input("Please enter your task to do \n")
# inp = AudioInput()
# response = chat(inp)

# folder to zip is working
# file to zip is not working
# unzip is not working


def invoker(response, list):
    match response:
        case 'Rename':
            return renameMethod(list)
        case 'Delete':
            return deleteMethod(list)
        case 'Search':
            return searchMethod(list)
        case 'open':
            return openFileMethod(list)
        case 'CreateFile':
            return createFileMethod(list)
        case 'CreateFolder':
            return createFolderMethod(list)
        case 'CopyPaste':
            return copyPasteMethod(list)
        case 'CutPaste':
            return cutPasteMethod(list)
        case 'ZipDirectory':
            return zipMethod(list)
        case 'UnzipDirectory':
            return extractMethod(list)
        case "OpenBrowser":
            open.OpenBrowser('www.chrome.com') # Will open the browser
        case "VolumeInc":
            volume.VolumeInc()   # For Increase the volume
        case "VolumeDec":
            volume.VolumeDec()   # For Decrease the volume
        case "SearchInBrowser":
            shortcut.SearchInBrowser()  # Will search in the current tab
        case "CloseTab":
            close.CloseBrowserTab()  # Close the browser Tab
        case "OpenApplication":
            openApplication.OpenApplication() # For Opening any app available in the pc
        case "ShutDown":
            shortcut.ShutDown()  # For shutting down the pc
        case "Restart":
            shortcut.Restart()  # For Restarting the pc
        case "NumsLock":
            shortcut.NumsLock()  # For Inverting the nums lock key
        case "CapsLock":
            shortcut.CapsLock()   # For Inverting the caps lock key
        case "Screenshot":
            shortcut.Screenshot()  # For taking the screenshot
        case "Mute":
            volume.Mute()       # For Mute 
        case "BrightnessInc":
            brightness.BrightnessInc()  # For Increasing the brightness
        case "BrightnessDec":
            brightness.BrightnessDec() # For Decreasing the brightness
        case "OpenNewTabInNewWindow":
            open.OpenNewTabInNewWindow() # Open the new tab in new Window
        case "CloseTheCurrentTab":
            close.CloseTheCurrentTab() # Close the current tab
        case "CloseTheApplication":
            shortcut.CloseTheApplication()  # Will close the app you are on
        case "SendMail":  # for sending mail
            send_email(list)
        # case default:
        #     print("Why I am here")
        #     print("Invalid Input")
        case default:
            print("sorry couldn't get you, please try again !!")

# invoker("open")


# import tensorflow as tf
# print(tf.__version__)