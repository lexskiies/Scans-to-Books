from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,  QVBoxLayout, QMainWindow
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Scans to Books')
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        

        



        