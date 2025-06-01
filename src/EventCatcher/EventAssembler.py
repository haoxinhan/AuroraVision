from .event  import Event,EventType,EventSource,EventPriority

class EventAssembler:
    # 初始化EventAssembler类，传入engine参数
    def __init__(self,engine):
        self.engine = engine

    # 当焦点改变时，调用该方法
    def on_focus_change(self):
        # 创建一个Event对象，类型为FOCUS_CHANGED，来源为SYSTEM，优先级为HIGH，时间戳为engine的get_timestamp()方法返回的值
        event= Event(
            type=EventType.FOCUS_CHANGED,
            source=EventSource.SYSTEM,
            priority=EventPriority.HIGH,
            timestamp=self.engine.get_timestamp()
        )
        # 将Event对象添加到engine的事件列表中
        self.engine.add_event(event)

