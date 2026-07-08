from utils_future import Parse, TimeFormat


class CCPISubgroupsParseMixin:
    SUBGROUP_LABELS = [
        "all",
        "food",
        "non-food",
        "alcoholic-beverages-and-tobacco",
        "clothing-and-footwear",
        "housing-water-electricity-gas-and-other-fuels",
        "furnishings-household-equipment-and-routine-household-maintenance",
        "health",
        "transport",
        "communication",
        "recreation-and-culture",
        "education",
        "restaurants-and-hotels",
        "miscellaneous-goods-and-services",
    ]

    INNER_FIELDS = {
        "ccpi": "float",
        "change_month_to_month": "percent",
        "inflation_year_to_year": "percent",
        "inflation_12_month_moving_average": "percent",
    }

    @classmethod
    def parse_row(cls, arr, year_str):
        month_part = arr[1].strip()
        date_str = TimeFormat.DATE.format(
            TimeFormat("%Y-%B").parse(f"{year_str}-{month_part}")
        )
        d = {
            "date_str": date_str,
        }
        for i, subgroup in enumerate(cls.SUBGROUP_LABELS):
            for j, (field, type_label) in enumerate(cls.INNER_FIELDS.items()):
                value = Parse.custom(
                    type_label, arr[2 + i * len(cls.INNER_FIELDS) + j]
                )
                d[f"{subgroup}_{field}"] = value
        return d

    @classmethod
    def parse_d_list(cls, arr_list):
        d_list = []
        year_str = None
        for arr in arr_list:
            if (
                (arr[0] == "" and year_str is None)
                or "Base" in arr[0]
                or "Year" in arr[0]
                or "Weight" in arr[0]
            ):
                continue

            if arr[0].strip() != "":
                year_str = arr[0].strip()

            if arr[1].strip() == "":
                continue

            d_list.append(cls.parse_row(arr, year_str))
        return d_list
