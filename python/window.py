from PySide2 import QtCore
from PySide2.QtWidgets import QVBoxLayout, QLabel, QWidget, QPushButton


class Window(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()

        title = QLabel()
        title.setText("Test to update value")

        button_add_one = self._set_button("+1", self._callback_add_one)
        button_minus_one = self._set_button("-1", self._callback_minus_one)

        self.label = QLabel()
        self.label.setText("0")

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(button_add_one)
        layout.addWidget(button_minus_one)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def _set_button(self, name, callback, *args):
        button = QPushButton(name)
        button.clicked.connect(callback)

        return button

    @QtCore.Slot()
    def _callback_add_one(self):
        value = int(self.label.text())
        self.label.setText(str(value + 1))

    @QtCore.Slot()
    def _callback_minus_one(self):
        value = int(self.label.text())
        self.label.setText(str(value - 1))
