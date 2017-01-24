from UI import *
import sys
import threading



def main():
    app = QApplication(sys.argv)

    #create ui window
    timer_ui = Interface()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = main()
    app.run()

# class ThreadStopper(Thread):
#
#     def __init__(self):
#         Thread.__init__()
#         self.stop_event = Event()
#
#     def stop(self):
#         if self.isAlive() == True:
#             self.stop_event.set()
#             self.join()
#
# class IntervalTimer(ThreadStopper):
#     def __init__(self, interval, func):
#         super().__init__()
#         self.interval = interval
#         self.func = func
#
#     def run(self):
#         while not self.stop_event.is_set():
#             self._func()
#             sleep(self._interval)