from dataclasses import dataclass

from dcs.ccpi.CCPISubgroups import CCPISubgroups
from dcs.ccpi.chart.LineChart import LineChart
from dcs.ccpi.chart.SubgroupFieldsMixin import SubgroupFieldsMixin


@dataclass
class SubgroupCCPIChart(SubgroupFieldsMixin, LineChart):
    subgroup: str = "all"

    @classmethod
    def get_source_doc_cls(cls):
        return CCPISubgroups

    @classmethod
    def get_name(cls):
        return "CCPI by Subgroup"

    @classmethod
    def latest_list(cls):
        doc = cls.get_source_doc_cls().latest()
        return [cls([doc], slug) for slug in CCPISubgroups.SUBGROUP_LABELS]

    @property
    def name(self):
        return f"CCPI - {self.label_of(self.subgroup)}"

    @property
    def chart_id(self):
        return f"ccpi-by-subgroup-{self.subgroup}"

    def get_field_to_label(self):
        fields = {f"{self.subgroup}_ccpi": self.label_of(self.subgroup)}
        if self.subgroup != "all":
            fields["all_ccpi"] = "Overall CCPI"
        return fields

    def get_ylabel(self):
        return "Index"

    def get_primary_colors(self):
        return ["C0", "C2"]

    def get_secondary_field_to_label(self):
        field = f"{self.subgroup}_change_month_to_month"
        return {field: "Change (Month on Month)"}

    def get_secondary_ylabel(self):
        return "Change (Month on Month)"

    def get_secondary_is_percent(self):
        return True

    def get_secondary_colors(self):
        return ["C1"]
