# CS683-Spyware
This is a course project. The purpose of the project is to create a spyware that could do some functionalities for educational purposes.

## Spicyware Overview
My spyware is called spicyware and it is coded to run only on Windows machines. <br/>
**The spyware is programmed to run on startup and is formed of several python scripts that are merged into one "exe" file.**

## Spicyware Functionality
When the program runs, it does the following:
1. Access the machine's webcam and save the video to an "avi" file
2. Access the machine's microphone and save the audio to an "mp3" file
3. Access Chrome Browser's History database file and extract all the visited urls, visited time, and the number of visits. Then writes the results to a "txt" file.
4. Access Chrome Browser's Login Data database file, decrypt the passwords, and extract the urls with the username and password. Then writes the result to a "txt" file.
5. Send the login data "txt" file via email to my personal email.
6. Track all the keyboard events and log them in a "txt" file
7. Developed to run on startup

## Spicyware Limitations
1. The spyware only runs on windows machines because the "pyinstaller" only merge the python scripts to "exe" file.
2. Only the login data file is sent via email and not the video, audio, history, and key logs.

## Spicyware Future Work
As a future work I would like to do the following:
1. Develop the spyware to run on different Operating Systems
2. Send all the files accessed by the spyware via email or to a server
3. Run the spyware in background
4. Hide the program inside a "jpg" or "pdf"
