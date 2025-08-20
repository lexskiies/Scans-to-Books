# src/scans_to_books/downloader.py

import pathlib
import logging
from abc import ABC, abstractmethod
from gallery_dl import job, config

logger = logging.getLogger(__name__)


class DownloadError(Exception):
    """Erreur lors du téléchargement avec gallery-dl."""


class Downloader(ABC):
    """
    Classe abstraite pour gérer un téléchargement avec gallery-dl.
    Chaque extracteur spécifique doit hériter de cette classe.
    """

    def __init__(self, output_dir: str):
        self.output_path = pathlib.Path(output_dir).absolute()
        self.output_path.mkdir(parents=True, exist_ok=True)

        # Configuration globale
        config.set(("extractor",), "base-directory", str(self.output_path))

        # Configuration spécifique à l’extracteur
        self._configure_extractor()

    @abstractmethod
    def _configure_extractor(self):
        """Configurer les paramètres spécifiques à l’extracteur."""
        pass

    def download(self, url: str) -> pathlib.Path:
        """
        Télécharge depuis l’URL donnée avec l’extracteur configuré.

        Args:
            url: URL cible (manga, galerie, etc.)

        Returns:
            pathlib.Path: dossier contenant les fichiers téléchargés
        """
        logger.info(f"Téléchargement depuis {url} vers {self.output_path}")
        try:
            j = job.DownloadJob(url)
            j.run()
        except Exception as e:
            logger.error(f"Erreur gallery-dl: {e}")
            raise DownloadError(str(e)) from e

        return self.output_path


class WeebCentralDownloader(Downloader):
    """
    Téléchargeur spécialisé pour l’extracteur weebcentral.
    """

    def __init__(self, output_dir: str, chapter_range: str | None = None):
        self.chapter_range = chapter_range
        super().__init__(output_dir)

    def _configure_extractor(self):
        if self.chapter_range:
            config.set(("extractor", "weebcentral"), "chapter-range", self.chapter_range)
