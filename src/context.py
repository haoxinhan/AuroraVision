import time


class Context(object):
    def __init__(self, **kwargs):
        #焦点最后改变时间
        self.last_focus_change_time = time.time()
    def set_last_focus_change_time(self, time):
        self.last_focus_change_time = time
    def get_last_focus_change_time(self):
        return self.last_focus_change_time