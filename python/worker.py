from PySide2 import QtCore

import time


class Worker(QtCore.QRunnable):
    def __init__(self):
        super().__init__()
        self.run_forever = True
        self.data = 0
        self.data_signal = WorkerSignal()

    @QtCore.Slot()
    def run(self):
        print("Thread start")
        while self.run_forever:
            time.sleep(1)
            self.data += 1
            self.data_signal.data.emit(self.data)
        print("Thread complete")


class WorkerSignal(QtCore.QObject):
    data = QtCore.Signal(int)
