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
from figure import Figure


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
        self.figure = Figure()

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
        print(value)

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
        app = QtCore.QCoreApplication.instance()
        app.quit()

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
