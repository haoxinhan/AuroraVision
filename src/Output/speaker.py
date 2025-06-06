import time

import pyttsx3 as tts
from src.PQ import PriorityQueue
import threading
from concurrent.futures import ThreadPoolExecutor




class Speaker:
    def __init__(self, engine):
        self.engine = engine
        self.runing = False
        self.priorityQueue = PriorityQueue()
        self.voice = tts.init()

        #线程池
        self.engine_lock = threading.Lock()
        self.speech_thread_pool = ThreadPoolExecutor(max_workers=1)
        self.stop_event = threading.Event()
        self.current_speech = None







    def run(self):
        self.runing = True
        self.workerThread = threading.Thread(target=self.worker)
        self.workerThread.start()

    def stop(self):
        self.runing = False

    #打断
    def interrupt(self):
        self.voice.stop()
    def addEvent(self,event):
        if(event.interrupt):
            self.priorityQueue.push_front(event)
            self.interrupt()
        else:
            self.priorityQueue.push(event)

    def worker(self):
        while self.runing:
            if not self.priorityQueue.isEmpty():
                event = self.priorityQueue.pop()

                if not self.current_speech==None:
                    while not self.current_speech.done():
                        time.sleep(0.1)
                try:
                    self.voice.endLoop()
                except:
                    pass
                self.current_speech = self.speech_thread_pool.submit(self._speak_text, event)




            else:
                continue
    def _speak_text(self,event):
        with self.engine_lock:
            self.voice.say(event.text)
            self.voice.runAndWait()
            self.voice.stop()
            self.current_speech = None
            print(event.text)





