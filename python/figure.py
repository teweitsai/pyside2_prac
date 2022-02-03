from PySide2.QtWidgets import QVBoxLayout, QLabel, QWidget


class Figure(QWidget):
    """
    This "figure" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()

        title = QLabel()
        title.setText("Test to show the figure")

        self.data = QLabel()
        self.data.setText("0")

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(self.data)
        self.setLayout(layout)
