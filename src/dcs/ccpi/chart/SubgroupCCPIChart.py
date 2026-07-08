from dcs.ccpi.CCPISubgroups import CCPISubgroups
from dcs.ccpi.chart.LineChart import LineChart
from dcs.ccpi.chart.SubgroupFieldsMixin import SubgroupFieldsMixin


class SubgroupCCPIChart(SubgroupFieldsMixin, LineChart):

    @classmethod
    def get_source_doc_cls(cls):
        return CCPISubgroups

    @classmethod
    def get_name(cls):
        return "CCPI by Subgroup"

    @classmethod
    def get_field_to_label(cls):
        return cls.fields_for("ccpi")

    def get_ylabel(self):
        return "Index"
