from dcs.ccpi.chart.LineChart import LineChart
from dcs.ccpi.InflationByFoodAndNonFoodGroups import \
    InflationByFoodAndNonFoodGroups


class FoodNonFoodCCPIChart(LineChart):

    @classmethod
    def get_source_doc_cls(cls):
        return InflationByFoodAndNonFoodGroups

    @classmethod
    def get_name(cls):
        return "CCPI by Food and Non Food"

    @classmethod
    def get_field_to_label(cls):
        return {
            "all_ccpi": "All",
            "food_ccpi": "Food",
            "non_food_ccpi": "Non Food",
        }

    def get_ylabel(self):
        return "Index"
