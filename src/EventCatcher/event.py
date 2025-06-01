from enum import Enum, auto
from dataclasses import dataclass
from typing import Any, Dict, Optional


class EventType(Enum):
    # 系统事件
    FOCUS_CHANGED = auto()  # 焦点变化
    WINDOW_CHANGED = auto()  # 窗口切换
    CONTENT_UPDATED = auto()  # 内容更新
    SYSTEM_ALERT = auto()  # 系统警报

    # 用户输入事件
    KEY_PRESS = auto()  # 按键事件
    BRAILLE_INPUT = auto()  # 盲文输入
    GESTURE_RECOGNIZED = auto()  # 手势识别

    # TTS事件
    TTS_STARTED = auto()  # TTS开始
    TTS_COMPLETED = auto()  # TTS完成
    TTS_INTERRUPTED = auto()  # TTS中断

    # 内部事件
    CONFIG_UPDATED = auto()  # 配置更新
    CONTEXT_CHANGED = auto()  # 上下文变化


class EventPriority(Enum):
    CRITICAL = 0  # 系统警报、用户中断
    HIGH = 1  # 焦点变化、导航命令
    NORMAL = 2  # 内容更新
    LOW = 3  # 配置更新、后台任务


@dataclass
class UIElement:
    id: str
    role: str  # "button", "text", "link"等
    name: str
    value: Optional[str] = None
    state: Optional[str] = None  # "focused", "selected", etc.
    position: Optional[Dict[str, int]] = None  # {"x":10, "y":20, "width":100, "height":30}

class EventSource(Enum):
    SYSTEM = auto()
    KEYBOARD = auto()
    BRAILLE = auto()
    TTS = auto()
    INTERNAL = auto()


@dataclass
class Event:
    #event_id: str  # 事件ID
    type: EventType  # 事件类型
    source: EventSource  # "system", "keyboard", "braille", etc. 事件来源
    timestamp: float  # 事件时间戳
    priority: EventPriority  # 事件优先级
    data: Dict[str, Any]=None  # 事件特定数据
    context: Dict[str, Any] = None  # 运行时上下文