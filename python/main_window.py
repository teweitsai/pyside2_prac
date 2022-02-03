from functools import partial
from PySide2 import QtCore

from PySide2.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QMenu,
    QAction,
    QToolBar,
    QStatusBar,
)

from window import Window
from custom_figure import CustomFigure
from worker import Worker


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test Application")

        self.button_new_window = None
        self.button_new_figure = None

        # Set the central widget of the Window
        container = QWidget()

        layout = self._set_layout()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self._add_toolbar("Toolbar")
        self.setStatusBar(QStatusBar(self))

        self.window = Window()
        self.figure = CustomFigure()

        # Run the worker in another thread
        self.threadpool = QtCore.QThreadPool()
        self.threadpool.setMaxThreadCount(2)

        self._worker = Worker()
        self._worker.data_signal.data.connect(self._callback_signal)
        self.threadpool.start(self._worker)

    def _set_layout(self):
        button_press = self._set_button("Press", self._callback_press)

        self.button_new_window = self._set_button(
            "Window", self._callback_new_window, *["abc"], is_checkable=True
        )

        self.button_new_figure = self._set_button(
            "Figure", self._callback_new_figure, is_checkable=True
        )

        button_exit = self._set_button("Exit", self._callback_exit)

        layout = QVBoxLayout()
        layout.addWidget(button_press)
        layout.addWidget(self.button_new_window)
        layout.addWidget(self.button_new_figure)
        layout.addWidget(button_exit)

        return layout

    def _set_button(self, name, callback, *args, is_checkable=False):
        button = QPushButton(name)
        if is_checkable:
            button.setCheckable(is_checkable)

        button.clicked.connect(partial(callback, *args))

        return button

    @QtCore.Slot()
    def _callback_press(self):
        print("Clicked!")

    @QtCore.Slot()
    def _callback_new_window(self, value):
        print(f"Set the input: {value}")

        if self.button_new_window.isChecked():
            self.window.show()
        else:
            self.window.hide()

    @QtCore.Slot()
    def _callback_new_figure(self):

        if self.button_new_figure.isChecked():
            self.figure.show()
        else:
            self.figure.hide()

    @QtCore.Slot()
    def _callback_exit(self):
        self._worker.run_forever = False

        msecs = 2000
        isDone = self.threadpool.waitForDone(msecs)
        if isDone:
            print("The worker is done.")
        else:
            print("The worker is not done.")

        app = QtCore.QCoreApplication.instance()
        app.quit()

    @QtCore.Slot()
    def _callback_signal(self, new_value):

        refresh = False
        if self.button_new_figure.isChecked():
            refresh = True
            self.figure.data.setText(str(new_value))

        self.figure.mpl_canvas.update_new_data(new_value, refresh=refresh)

    def contextMenuEvent(self, event):
        context = QMenu(self)

        action_exit = self._set_action("Exit", self._callback_exit)
        context.addAction(action_exit)

        context.exec_(event.globalPos())

    def _set_action(self, name, callback):

        action = QAction(name, self)
        action.triggered.connect(callback)

        return action

    def _add_toolbar(self, name):

        toolbar = QToolBar(name)

        button_exit = self._set_action("Exit", self._callback_exit)
        toolbar.addAction(button_exit)

        self.addToolBar(toolbar)
