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

from PySide2.QtCore import QCoreApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test Application")

        self.button_press = self._set_button("Press", self._callback_press)
        button_exit = self._set_button("Exit", self._callback_exit)

        layout = QVBoxLayout()
        layout.addWidget(self.button_press)
        layout.addWidget(button_exit)

        # Set the central widget of the Window
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self._add_toolbar("Toolbar")

        self.setStatusBar(QStatusBar(self))

    def _set_button(self, name, callback, is_checkable=False):
        button = QPushButton(name)
        button.clicked.connect(callback)

        if is_checkable:
            button.setCheckable(is_checkable)

        return button

    def _callback_press(self):
        print("Clicked!")

    def _callback_exit(self):
        app = QCoreApplication.instance()
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
