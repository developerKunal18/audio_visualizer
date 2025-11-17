import sounddevice as sd
import numpy as np
import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def visualize_audio(duration=30, samplerate=44100, bars=60):
    print("🎧 Listening... Speak or play music!")
    time.sleep(1)

    def callback(indata, frames, time, status):
        clear()
        volume = np.linalg.norm(indata) * 20
        level = int(volume / 2)

        for i in range(bars):
            height = int(level * np.sin(i / 4))
            print("█" * max(0, height))
        print("\nCtrl+C to exit")

    with sd.InputStream(callback=callback, channels=1, samplerate=samplerate):
        time.sleep(duration)

if __name__ == "__main__":
    try:
        visualize_audio()
    except KeyboardInterrupt:
        clear()
        print("👋 Exiting Audio Visualizer")
