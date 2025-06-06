import time

import pyttsx3
import threading
engine = pyttsx3.init()


def word():
    global engine
    engine.runAndWait()

t=threading.Thread(target=word)
engine.say("Hello World!")


t.start()

engine.stop()
time.sleep(3)

print(engine.isBusy())
engine.endLoop()

