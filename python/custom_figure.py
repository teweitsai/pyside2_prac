from PySide2.QtWidgets import QVBoxLayout, QLabel, QWidget
import matplotlib

matplotlib.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402


class CustomFigure(QWidget):
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

        self.mpl_canvas = MplCanvas(width=5, height=4, dpi=100)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(self.data)
        layout.addWidget(self.mpl_canvas)
        self.setLayout(layout)


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)

        self._axes = self.fig.add_subplot(111)
        self._axes.set_ylim([-0.5, 0.5])
        self._data = [0] * 100
        self._plot_ref = self._axes.plot(self._data, "b")[0]

    def update_new_data(self, new_data, refresh=False):

        self._data.pop(0)
        self._data.append(new_data)

        self._plot_ref.set_ydata(self._data)

        # Trigger the canvas to update and redraw
        if refresh:
            self.draw()
