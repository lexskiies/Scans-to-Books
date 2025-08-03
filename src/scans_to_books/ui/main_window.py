# src/scans_to_books/ui/main_window.py

from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scans to Books")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()


        # Selection des chapitres
        self.label = QLabel("Range de chapitres: ")
        self.chapter_input_1 = QLineEdit()
        self.chapter_input_2 = QLineEdit()
        self.chapter_input_1.setPlaceholderText("Ex: 1")
        self.chapter_input_2.setPlaceholderText("Ex: 10")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.chapter_input_1)
        self.layout.addWidget(self.chapter_input_2)

        # Validation des entrées
        self.validate_button = QPushButton("Valider")
        self.validate_button.clicked.connect(self.on_validate)
        self.layout.addWidget(self.validate_button)


        self.central_widget.setLayout(self.layout)

    def on_validate(self):
        chapter_start = self.chapter_input_1.text()
        chapter_end = self.chapter_input_2.text()
        
        print(f"Chapitres sélectionnés: {chapter_start} à {chapter_end}")
