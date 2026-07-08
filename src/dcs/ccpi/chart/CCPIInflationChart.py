from dcs.ccpi.CCPI import CCPI
from dcs.ccpi.chart.LineChart import LineChart


class CCPIInflationChart(LineChart):

    @classmethod
    def get_source_doc_cls(cls):
        return CCPI

    @classmethod
    def get_name(cls):
        return "CCPI Inflation"

    @classmethod
    def get_field_to_label(cls):
        return {
            "inflation_year_to_year": "Inflation (Year on Year)",
            "inflation_12_month_moving_average": "Inflation (12 Month MA)",
        }

    def get_ylabel(self):
        return "Inflation"

    def is_percent(self):
        return True
