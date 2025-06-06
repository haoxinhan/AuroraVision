
import uiautomation as auto

class FocusHandler():
    def __init__(self, engine):
        self.engine = engine


    def handle(self, event):
        ui=auto.GetFocusedControl()
        #print(ui.Name)
        self.engine.out.toSperk(
            text=ui.Name,
            priority=event.priority,
            interrupt=True,
            interruptible=True
        )

        pass
