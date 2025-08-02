# src/scans_to_books/ui/main_window.py

from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("scans_to_books")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.label = QLabel("Bonjour, monde!")
        self.layout.addWidget(self.label)

        self.button = QPushButton("Cliquez-moi!")
        self.button.clicked.connect(self.on_button_click)
        self.layout.addWidget(self.button)

        self.central_widget.setLayout(self.layout)

    def on_button_click(self):
        self.label.setText("Bouton cliqué!")
