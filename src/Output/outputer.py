
import time
from . import speaker
from src.EventCatcher import event
from dataclasses import dataclass

@dataclass()
class speakEvent:
    text:str
    #是否打断
    interrupt:bool
    #是否可被打断
    interruptible:bool
    timestamp: float  # 事件时间戳
    priority: event.EventPriority  # 事件优


class Outputer:
    def __init__(self,engine):
        self.engine = engine
        self.speaker = speaker.Speaker(engine)
    def toSperk(self,
                priority,
                text,
                interrupt,
                interruptible
                ):
        e=speakEvent(
            text=text,
            interrupt=interrupt,
            timestamp=time.time(),
            priority=priority,
            interruptible=interruptible

        )
        self.speaker.addEvent(e)

    def run(self):
        self.speaker.run()
    def stop(self):
        self.speaker.stop()
