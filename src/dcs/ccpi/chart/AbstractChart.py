import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from functools import cached_property

import matplotlib

matplotlib.use("Agg")
from matplotlib import pyplot as plt  # noqa: E402

from utils_future import File, Log  # noqa: E402

log = Log("AbstractChart")

FIG_SIZE = (12, 6.75)
DPI = 100
DATE_FORMAT = "%Y-%m-%d"
DIR_IMAGES = os.path.join("images", "ccpi")


@dataclass
class AbstractChart(ABC):
    source_docs: list

    @classmethod
    @abstractmethod
    def get_source_doc_cls(cls):
        pass

    @classmethod
    @abstractmethod
    def get_name(cls):
        pass

    @abstractmethod
    def draw(self, ax):
        pass

    @classmethod
    def latest(cls):
        return cls([cls.get_source_doc_cls().latest()])

    @classmethod
    def get_chart_id(cls):
        return cls.get_name().replace(" ", "-").lower()

    @property
    def chart_file(self):
        os.makedirs(DIR_IMAGES, exist_ok=True)
        return File(os.path.join(DIR_IMAGES, f"{self.get_chart_id()}.png"))

    @cached_property
    def data_list(self):
        data_by_date = {}
        for doc in self.source_docs:
            for data in doc.data_list:
                data_by_date[data["date_str"]] = data
        return [data_by_date[date_str] for date_str in sorted(data_by_date)]

    @cached_property
    def dates(self):
        return [
            datetime.strptime(data["date_str"], DATE_FORMAT)
            for data in self.data_list
        ]

    @staticmethod
    def get_y(data_list, field):
        return [
            float("nan") if data.get(field) is None else data[field]
            for data in data_list
        ]

    def build(self):
        fig, ax = plt.subplots(figsize=FIG_SIZE)
        self.draw(ax)
        ax.set_title(self.get_name())
        ax.grid(True, linestyle="--", alpha=0.5)
        fig.tight_layout()
        fig.savefig(self.chart_file.path, dpi=DPI)
        plt.close(fig)
        log.info(f"Wrote {self.chart_file}")
        return self.chart_file
