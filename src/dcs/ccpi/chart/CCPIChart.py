from dcs.ccpi.CCPI import CCPI
from dcs.ccpi.chart.LineChart import LineChart


class CCPIChart(LineChart):

    @classmethod
    def get_source_doc_cls(cls):
        return CCPI

    @classmethod
    def get_name(cls):
        return "CCPI"

    @classmethod
    def get_field_to_label(cls):
        return {"ccpi": "CCPI"}

    def get_ylabel(self):
        return "Index"

    def get_primary_colors(self):
        return ["C0"]

    def get_secondary_field_to_label(self):
        return {"change_month_to_month": "Change (Month on Month)"}

    def get_secondary_ylabel(self):
        return "Change (Month on Month)"

    def get_secondary_is_percent(self):
        return True

    def get_secondary_colors(self):
        return ["C1"]
