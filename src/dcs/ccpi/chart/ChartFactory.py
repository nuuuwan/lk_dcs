from dcs.ccpi.chart.AbstractChart import DIR_IMAGES
from dcs.ccpi.chart.CCPIChart import CCPIChart
from dcs.ccpi.chart.CCPIInflationChart import CCPIInflationChart
from dcs.ccpi.chart.FoodNonFoodCCPIChart import FoodNonFoodCCPIChart
from dcs.ccpi.chart.FoodNonFoodInflationChart import FoodNonFoodInflationChart
from dcs.ccpi.chart.SubgroupCCPIChart import SubgroupCCPIChart
from dcs.ccpi.chart.SubgroupInflationChart import SubgroupInflationChart
from utils_future import Log

log = Log("ChartFactory")


class ChartFactory:

    @staticmethod
    def list():
        return [
            CCPIChart,
            CCPIInflationChart,
            FoodNonFoodCCPIChart,
            FoodNonFoodInflationChart,
            SubgroupCCPIChart,
            SubgroupInflationChart,
        ]

    @staticmethod
    def build_all():
        chart_files = []
        for chart_cls in ChartFactory.list():
            chart = chart_cls.latest()
            chart_files.append(chart.build())
        return chart_files

    @staticmethod
    def get_readme_lines():
        lines = ["## Charts", ""]
        for chart_cls in ChartFactory.list():
            name = chart_cls.get_name()
            path = f"{DIR_IMAGES}/{chart_cls.get_chart_id()}.png"
            lines += [f"### {name}", "", f"![{name}]({path})", ""]
        return lines
