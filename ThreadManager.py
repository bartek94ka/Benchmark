from threading import Thread, Event
import time
import DiscSpaceInfoProvider
class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(0.5):
            print("my thread")
            # call a function

def copyTask():
    #measureThread.start()
    print("CopyTask")
    #measureThread.join()
    stopFlag = Event()
    thread = MyThread(stopFlag)
    thread.start()
    # this will stop the timer
    thread._stop()
    #stopFlag.set()

def measureTask():
    print("Measure")

copyThread = Thread(name="Copy", target=copyTask)
measureThread = Thread(name="Measure", target=measureTask)

copyThread.start()
copyThread.join()