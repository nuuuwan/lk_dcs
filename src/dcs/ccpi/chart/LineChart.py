from abc import abstractmethod

import matplotlib.dates as mdates
from matplotlib.ticker import PercentFormatter

from dcs.ccpi.chart.AbstractChart import AbstractChart

MARKER_SIZE = 3


class LineChart(AbstractChart):

    @classmethod
    @abstractmethod
    def get_field_to_label(cls):
        pass

    def get_ylabel(self):
        return ""

    def is_percent(self):
        return False

    def get_primary_colors(self):
        return None

    def get_secondary_field_to_label(self):
        return {}

    def get_secondary_ylabel(self):
        return ""

    def get_secondary_is_percent(self):
        return False

    def get_secondary_colors(self):
        return None

    def plot_fields(self, ax, field_to_label, colors=None):
        for i, (field, label) in enumerate(field_to_label.items()):
            kwargs = {}
            if colors:
                kwargs["color"] = colors[i % len(colors)]
            ax.plot(
                self.dates,
                self.get_y(self.data_list, field),
                marker="o",
                markersize=MARKER_SIZE,
                label=label,
                **kwargs,
            )

    @staticmethod
    def format_axis(ax, ylabel, is_percent):
        ax.set_ylabel(ylabel)
        if is_percent:
            ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))

    @staticmethod
    def format_x_dates(ax):
        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    @staticmethod
    def combined_legend(ax, secondary_ax):
        handles, labels = ax.get_legend_handles_labels()
        handles2, labels2 = secondary_ax.get_legend_handles_labels()
        ax.legend(handles + handles2, labels + labels2)

    def draw(self, ax):
        self.plot_fields(
            ax, self.get_field_to_label(), self.get_primary_colors()
        )
        self.format_axis(ax, self.get_ylabel(), self.is_percent())
        self.format_x_dates(ax)
        secondary = self.get_secondary_field_to_label()
        if not secondary:
            ax.legend()
            return
        secondary_ax = ax.twinx()
        self.plot_fields(secondary_ax, secondary, self.get_secondary_colors())
        self.format_axis(
            secondary_ax,
            self.get_secondary_ylabel(),
            self.get_secondary_is_percent(),
        )
        self.combined_legend(ax, secondary_ax)
