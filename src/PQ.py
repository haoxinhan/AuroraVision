import time

from EventCatcher import event
from typing import List



class PriorityQueue():
    """
    优先级队列
    """
    def __init__(self):
        self.queue:List = []
        self.index = 0
        self.max_index = 0
        self.size = 0
    def push(self, event):
        """
        添加事件
        :param event: 事件
        :return:
        """
        self.queue.append(event)
        self.size += 1
        self.index += 1
        self.max_index = max(self.max_index, self.index)
        # 先按照优先级的从小到大排序
        self.queue.sort(key=lambda x: x.priority.value)
        # 再按照时间戳的从小到大排序
        self.queue.sort(key=lambda x: x.timestamp)
    def pop(self):
        """
        弹出事件
        :return:
        """

        if self.size == 0:
            return None
        self.size -= 1
        self.index -= 1
        return self.queue.pop(0)

    #在队首添加
    def push_front(self, event):
        """
        添加事件
        :param event: 事件
        :return:
        """
        self.queue.insert(0, event)
        self.size += 1
        self.index += 1
        self.max_index = max(self.max_index, self.index)

    def isEmpty(self):
        return self.size == 0











