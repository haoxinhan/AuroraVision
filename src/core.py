
from typing import List
from EventCatcher.event import Event, EventType, EventSource, EventPriority
import time
from EventCatcher import EventCatcher,EventAssembler
import context
from Config import config
from PQ import PriorityQueue
from Output import outputer




class EventProcessor():
    """
    事件处理器
    """
    def __init__(self):
        #事件队列
        self.event_queue = PriorityQueue()
        #事件处理函数
        self.event_handlers = {}
        #过滤器
        self.filters = []

        self.running = True
        #上下文
        self.context= context.Context()
        #事件组装器
        self.ea = EventAssembler.EventAssembler(self)
        #事件捕捉器
        self.ec = EventCatcher.EventCatcher(self.ea)



        #加载配置
        self.config = config.Config()
        self.config.loadConfig()
        self.context.setConfig(self.config)

        self.out = outputer.Outputer(self)







    def getContext (self):
        return self.context


    def run(self):
        """
        运行事件处理器
        :return:
        """
        # 启动事件捕捉器
        self.ec.start()
        self.out.run()



        #是否过滤
        isRun=True
        #是否运行
        while self.running:
            isRun=True
            if(not self.event_queue.isEmpty()):
                event = self.event_queue.pop()
                if event is None:
                    continue
                #对事件进行过滤
                for filter in self.filters:
                    if not filter(event,self.context):
                      isRun=False
                      break
                if not isRun:
                    continue
                #处理事件
                self.process_event(event)
            else:
                pass
    def  process_event(self, event: Event):
        """
        处理事件
        :param event: 事件
        :return:
        """
        if event.type in self.event_handlers:
            for handler in self.event_handlers[event.type]:
                handler.handle(event)

# 定义一个名为get_timestamp的函数，用于获取当前时间戳
    def get_timestamp(self):
        # 返回当前时间戳
        return time.time()
    def add_event(self, event: Event):
        # 将事件添加到事件队列中
        self.event_queue.push(event)
    def register_handler(self, event_type: EventType, handler):
        # 如果事件类型不在事件处理器字典中，则创建一个新的列表
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        # 将处理器添加到事件类型的列表中
        self.event_handlers[event_type].append(handler)
    def stop(self):
        # 停止事件处理器
        self.running = False
        self.ec.stop()
        self.out.speaker.stop()


ep= EventProcessor()
from Handers import FocusHandler
import Filter
ep.register_handler(EventType.FOCUS_CHANGED, FocusHandler.FocusHandler(ep))
ep.filters=Filter.filters

ep.run()