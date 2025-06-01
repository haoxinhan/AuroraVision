import threading
import ctypes
from ctypes import wintypes
import time


# 定义 Windows 常量
EVENT_SYSTEM_FOREGROUND = 0x0003
EVENT_OBJECT_FOCUS = 0x8005
WINEVENT_OUTOFCONTEXT = 0x0000
WINEVENT_SKIPOWNPROCESS = 0x0002
WM_QUIT = 0x0012

# 定义回调函数类型
WINEVENTPROC = ctypes.WINFUNCTYPE(
    None,
    wintypes.HANDLE,
    wintypes.DWORD,
    wintypes.HWND,
    wintypes.LONG,
    wintypes.LONG,
    wintypes.DWORD,
    wintypes.DWORD
)

# 加载 user32.dll
user32 = ctypes.WinDLL('user32')
kernel32 = ctypes.WinDLL('kernel32')

# 定义函数原型
user32.SetWinEventHook.restype = wintypes.HANDLE
user32.SetWinEventHook.argtypes = [
    wintypes.DWORD, wintypes.DWORD, wintypes.HMODULE,
    WINEVENTPROC, wintypes.DWORD, wintypes.DWORD, wintypes.DWORD
]

user32.GetWindowTextW.argtypes = [wintypes.HWND, wintypes.LPWSTR, wintypes.INT]
user32.GetWindowTextW.restype = wintypes.INT

user32.PostThreadMessageW.argtypes = [wintypes.DWORD, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
user32.PostThreadMessageW.restype = wintypes.BOOL

user32.GetMessageW.argtypes = [ctypes.POINTER(wintypes.MSG), wintypes.HWND, wintypes.UINT, wintypes.UINT]
user32.GetMessageW.restype = wintypes.BOOL

user32.TranslateMessage.argtypes = [ctypes.POINTER(wintypes.MSG)]
user32.DispatchMessageW.argtypes = [ctypes.POINTER(wintypes.MSG)]

kernel32.GetCurrentThreadId.restype = wintypes.DWORD

# 全局变量，用于控制消息循环线程
message_loop_thread = None
hook_handles = []





class EventCatcher(object):

    def __init__(self, engine, content=None,debug=False):
        self._engine = engine
        self._debug = debug
        self.running = True
        self.context = content


    def start(self):
        #启动线程
        threading.Thread(target=self.run,daemon=True).start()

    #采集焦点改变事件
    def monitor_focus(self,interval=0.1):
        def callback(hWinEventHook, event, hwnd, idObject, idChild, dwEventThread, dwmsEventTime):
            """事件回调函数 - 在消息循环线程中执行"""
            self._engine.on_focus_change()
        return callback
    def run(self):
        # 获取当前线程ID
        event_proc = WINEVENTPROC(self.monitor_focus())
        thread_id = kernel32.GetCurrentThreadId()

        try:
            # 设置事件钩子
            """
                hook1 = user32.SetWinEventHook(
                EVENT_SYSTEM_FOREGROUND,
                EVENT_SYSTEM_FOREGROUND,
                None,
                event_proc,
                0,  # 所有进程
                0,  # 所有线程
                WINEVENT_OUTOFCONTEXT | WINEVENT_SKIPOWNPROCESS
            )
            """


            hook2 = user32.SetWinEventHook(
                EVENT_OBJECT_FOCUS,
                EVENT_OBJECT_FOCUS,
                None,
                event_proc,
                0,  # 所有进程
                0,  # 所有线程
                WINEVENT_OUTOFCONTEXT | WINEVENT_SKIPOWNPROCESS
            )

            # 消息循环
            msg = wintypes.MSG()
            while user32.GetMessageW(ctypes.byref(msg), 0, 0, 0):
                user32.TranslateMessage(ctypes.byref(msg))
                user32.DispatchMessageW(ctypes.byref(msg))


        except Exception as e:
            pass

        finally:
            pass





