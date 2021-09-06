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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test Application")

        # Set the central widget of the Window
        container = QWidget()

        layout = self._set_layout()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self._add_toolbar("Toolbar")
        self.setStatusBar(QStatusBar(self))

        self.window = Window()

    def _set_layout(self):
        button_press = self._set_button("Press", self._callback_press)
        button_new_window = self._set_button(
            "New Window", self._callback_new_window, is_checkable=True
        )
        button_exit = self._set_button("Exit", self._callback_exit)

        layout = QVBoxLayout()
        layout.addWidget(button_press)
        layout.addWidget(button_new_window)
        layout.addWidget(button_exit)

        return layout

    def _set_button(self, name, callback, is_checkable=False):
        button = QPushButton(name)
        button.clicked.connect(callback)

        if is_checkable:
            button.setCheckable(is_checkable)

        return button

    @QtCore.Slot()
    def _callback_press(self):
        print("Clicked!")

    @QtCore.Slot()
    def _callback_new_window(self, checked):
        if checked:
            self.window.show()
        else:
            self.window.hide()

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
