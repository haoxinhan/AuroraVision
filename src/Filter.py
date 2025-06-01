"""
过滤器
负责对事件进行过滤
"""

import time
from EventCatcher import event


def debounce(e:event.Event,context):
    """
    防抖动
    :param e: 事件实例
    :param context: 上下文实例
    :return: 是否需要被过滤
    """
    #检查是否是焦点改变事件
    if e.type ==event.EventType.FOCUS_CHANGED:
        #如果距离上次焦点改变时间小于0.1秒，则过滤掉该事件
        if e.timestamp - context.get_last_focus_change_time()> 0.10:
            context.set_last_focus_change_time(e.timestamp)
            return True
        context.set_last_focus_change_time(e.timestamp)

        return False
    return True

#防超时
def timeout(e:event.Event,context):
    """
    防超时
    :param e: 事件实例
    :param context: 上下文实例
    :return:    是否需要被过滤
    """
    #检查是否是焦点改变事件
    if e.type ==event.EventType.FOCUS_CHANGED:
        #如果距离上次焦点改变时间小于1秒，则过滤掉该事件
        if not time.time()- e.timestamp > 1:
            context.set_last_focus_change_time(e.timestamp)
            return True
        context.set_last_focus_change_time(e.timestamp)
        return False
    return True


filters=[
    debounce,
    timeout
]
