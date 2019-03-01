#!/usr/bin/env python
from os.path import expanduser
import sqlite3
import time, datetime
import winshell

"""
This script accesses the history sqlite 3 database for the chrome browser using sqlite3 library
and gets the urls' last visit time, title, number of visits. Then writes the results to a txt file
"""
def start():
    try:
        # the place where Chrome stores its history
        HISTORY_DB='~/AppData/Local/Google/Chrome/User Data/Default/History'

        # open destination database
        conn = sqlite3.connect(expanduser(HISTORY_DB))
        
        # get a data cursor to work with the database
        c = conn.cursor()
            
        #list existing history in chrome
        result = c.execute('SELECT datetime(last_visit_time/1000000-11644473600, "unixepoch") as last_visited, url , title, visit_count FROM urls;')

        # specify destination path of file I will write the results to
        dest_path = winshell.desktop() + r"\Spyware\Output"
        dest_path = dest_path.replace('\\','/') + "/history.txt"

        f = open(dest_path, 'w+', encoding="utf-8")

        # iterate through the SQL result and write it to the file
        for row in result:
            try:
                data = ' '.join(str(r) for r in row)
                data += "\r\n"
                f.write(data)
            except Exception:
                continue

        f.close()
    except Exception:
        print("Failed")