from PySide2.QtWidgets import QApplication

# Only needed for access to command line arguments
import sys

from main_window import MainWindow

if __name__ == "__main__":

    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works
    # too.
    app = QApplication(sys.argv)

    # Create a Qt main window, which will be our window.
    window_main = MainWindow()
    window_main.show()

    # Start the event loop.
    app.exec_()

    # Your application won't reach here until you exit and the event
    # loop has stopped.
