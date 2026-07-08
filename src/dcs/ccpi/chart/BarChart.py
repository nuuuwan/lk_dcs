from abc import abstractmethod

from matplotlib.ticker import PercentFormatter

from dcs.ccpi.chart.AbstractChart import AbstractChart

X_ROTATION = 45


class BarChart(AbstractChart):

    @classmethod
    @abstractmethod
    def get_field_to_label(cls):
        pass

    def get_ylabel(self):
        return ""

    def is_percent(self):
        return False

    def draw(self, ax):
        field_to_label = self.get_field_to_label()
        row = self.data_list[-1]
        values = [self.get_y([row], field)[0] for field in field_to_label]
        positions = list(range(len(field_to_label)))
        ax.bar(positions, values)
        ax.set_xticks(positions)
        ax.set_xticklabels(
            list(field_to_label.values()),
            rotation=X_ROTATION,
            ha="right",
        )
        ax.set_ylabel(self.get_ylabel())
        if self.is_percent():
            ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))
