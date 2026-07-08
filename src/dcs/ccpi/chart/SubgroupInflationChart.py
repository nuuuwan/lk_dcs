from dcs.ccpi.CCPISubgroups import CCPISubgroups
from dcs.ccpi.chart.BarChart import BarChart
from dcs.ccpi.chart.SubgroupFieldsMixin import SubgroupFieldsMixin


class SubgroupInflationChart(SubgroupFieldsMixin, BarChart):

    @classmethod
    def get_source_doc_cls(cls):
        return CCPISubgroups

    @classmethod
    def get_name(cls):
        return "Inflation by Subgroup"

    @classmethod
    def get_field_to_label(cls):
        return cls.fields_for("inflation_year_to_year")

    def get_ylabel(self):
        return "Inflation (Year on Year)"

    def is_percent(self):
        return True
