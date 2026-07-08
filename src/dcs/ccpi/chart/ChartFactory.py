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
            for chart in chart_cls.latest_list():
                chart_files.append(chart.build())
        return chart_files

    @staticmethod
    def chart_lines(chart):
        name = chart.name
        path = f"{DIR_IMAGES}/{chart.chart_id}.png"
        return [f"### {name}", "", f"![{name}]({path})", ""]

    @staticmethod
    def get_readme_lines():
        lines = ["## Charts", ""]
        for chart_cls in ChartFactory.list():
            for chart in chart_cls.latest_list():
                lines += ChartFactory.chart_lines(chart)
        return lines
