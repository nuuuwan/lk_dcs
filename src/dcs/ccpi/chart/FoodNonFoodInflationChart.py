from dcs.ccpi.chart.LineChart import LineChart
from dcs.ccpi.InflationByFoodAndNonFoodGroups import \
    InflationByFoodAndNonFoodGroups


class FoodNonFoodInflationChart(LineChart):

    @classmethod
    def get_source_doc_cls(cls):
        return InflationByFoodAndNonFoodGroups

    @classmethod
    def get_name(cls):
        return "Inflation by Food and Non Food"

    @classmethod
    def get_field_to_label(cls):
        return {
            "all_inflation_year_to_year": "All",
            "food_inflation_year_to_year": "Food",
            "non_food_inflation_year_to_year": "Non Food",
        }

    def get_ylabel(self):
        return "Inflation"

    def is_percent(self):
        return True
