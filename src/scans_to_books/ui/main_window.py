# src/scans_to_books/ui/main_window.py

from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QTextEdit,
    QVBoxLayout, QHBoxLayout
)
from scans_to_books.downloader import WeebCentralDownloader
import threading


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scans to Books")

        # Champs pour chapitres
        self.start_chapter_input = QLineEdit()
        self.start_chapter_input.setPlaceholderText("Chapitre début (ex: 32)")

        self.end_chapter_input = QLineEdit()
        self.end_chapter_input.setPlaceholderText("Chapitre fin (ex: 60)")

        # Champ pour URL
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("URL du manga")

        # Bouton
        self.download_button = QPushButton("Télécharger")
        self.download_button.clicked.connect(self.on_download_clicked)

        # Zone messages
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)

        # Layout
        chapter_layout = QHBoxLayout()
        chapter_layout.addWidget(QLabel("Chapitres:"))
        chapter_layout.addWidget(self.start_chapter_input)
        chapter_layout.addWidget(self.end_chapter_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(chapter_layout)
        main_layout.addWidget(QLabel("URL:"))
        main_layout.addWidget(self.url_input)
        main_layout.addWidget(self.download_button)
        main_layout.addWidget(QLabel("Messages:"))
        main_layout.addWidget(self.log_output)

        self.setLayout(main_layout)

    def log(self, message: str):
        """Affiche un message dans la zone de logs."""
        self.log_output.append(message)

    def on_download_clicked(self):
        """Déclenche le téléchargement via le Downloader."""
        url = self.url_input.text().strip()
        start = self.start_chapter_input.text().strip()
        end = self.end_chapter_input.text().strip()

        if not url:
            self.log("❌ Merci de saisir une URL.")
            return

        # Construire la plage de chapitres si renseignée
        chapter_range = None
        if start and end:
            chapter_range = f"{start}-{end}"

        self.log(f"⏳ Téléchargement en cours depuis {url} (chapitres {chapter_range})...")

        # Lancer dans un thread pour ne pas bloquer l’UI
        thread = threading.Thread(
            target=self.run_download,
            args=(url, chapter_range),
            daemon=True
        )
        thread.start()

    def run_download(self, url: str, chapter_range: str | None):
        try:
            downloader = WeebCentralDownloader(output_dir="./downloads", chapter_range=chapter_range)
            path = downloader.download(url)
            self.log(f"✅ Téléchargement terminé dans {path}")
        except Exception as e:
            self.log(f"❌ Erreur: {e}")
