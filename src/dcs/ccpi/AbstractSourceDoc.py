import os
import tempfile
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property

from utils_future import WWW, JSONFile, Log, PDFFile, TSVFile

log = Log("AbstractSourceDoc")


@dataclass
class AbstractSourceDoc(ABC):
    date_str: str

    @property
    def year_str(self):
        return self.date_str[:4]

    @property
    def dir_data(self):
        dir_data = os.path.join(
            "data", "ccpi", self.get_class_id(), self.year_str, self.date_str
        )
        os.makedirs(dir_data, exist_ok=True)
        return dir_data

    @classmethod
    @abstractmethod
    def from_pdf_file(cls, pdf_file):
        pass

    @classmethod
    @abstractmethod
    def get_url(cls):
        pass

    @classmethod
    @abstractmethod
    def get_name(cls):
        pass

    @property
    def original_file(self):
        return PDFFile(os.path.join(self.dir_data, "original.pdf"))

    @property
    def data_file(self):
        return JSONFile(os.path.join(self.dir_data, "data.json"))

    @property
    def tsv_data_file(self):
        return TSVFile(os.path.join(self.dir_data, "data.tsv"))

    @classmethod
    def get_class_id(cls):
        return cls.get_name().replace(" ", "-").lower()

    @classmethod
    def download_latest(cls, force=False):
        temp_dir = os.path.join(
            tempfile.gettempdir(), "dcs", cls.get_class_id()
        )
        os.makedirs(temp_dir, exist_ok=True)
        temp_file_path = os.path.join(temp_dir, f"{cls.get_class_id()}.pdf")

        if os.path.exists(temp_file_path) and not force:
            return temp_file_path

        WWW(cls.get_url()).download_binary(temp_file_path)

        return temp_file_path

    @cached_property
    def data_list(self):
        return self.data_file.read()

    def build_tsv_data(self):
        self.tsv_data_file.write(self.data_list)
        log.info(f"Wrote {self.tsv_data_file}")

    def copy_original(self, temp_pdf_file):
        self.original_file.copy_from(temp_pdf_file)
        log.info(f"Wrote {self.original_file}")

    @classmethod
    def build_latest(cls):
        log.debug(f"Building latest {cls.get_name()}")
        temp_pdf_file = PDFFile(cls.download_latest())
        doc = cls.from_pdf_file(temp_pdf_file)
        doc.build_tsv_data()
        doc.copy_original(temp_pdf_file)
        return doc
