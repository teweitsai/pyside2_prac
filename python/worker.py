from PySide2 import QtCore

import time


class Worker(QtCore.QRunnable):

    def __init__(self):
        super().__init__()
        self.run_forever = True

    @QtCore.Slot()
    def run(self):
        print("Thread start")
        while self.run_forever:
            time.sleep(1)
        print("Thread complete")
