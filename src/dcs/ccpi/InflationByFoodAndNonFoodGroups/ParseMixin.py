from utils_future import Parse, TimeFormat


class ParseMixin:

    @staticmethod
    def parse_date_str(year_str, month_str):
        return TimeFormat.DATE.format(
            TimeFormat("%Y-%B").parse(f"{year_str}-{month_str}")
        )

    @classmethod
    def parse_row(cls, arr, year_str):
        if len(arr) != 14:
            raise ValueError(f"Unexpected row length: {len(arr)} for {arr}")
        return dict(
            date_str=cls.parse_date_str(year_str, arr[1]),
            # all
            all_ccpi=Parse.float(arr[2]),
            all_ccpi_change_month_to_month=Parse.percent(arr[3]),
            all_inflation_year_to_year=Parse.percent(arr[4]),
            all_inflation_12_month_moving_average=Parse.percent(arr[5]),
            # food
            food_ccpi=Parse.float(arr[6]),
            food_ccpi_change_month_to_month=Parse.percent(arr[7]),
            food_inflation_year_to_year=Parse.percent(arr[8]),
            food_inflation_12_month_moving_average=Parse.percent(arr[9]),
            # non-food
            non_food_ccpi=Parse.float(arr[10]),
            non_food_ccpi_change_month_to_month=Parse.percent(arr[11]),
            non_food_inflation_year_to_year=Parse.percent(arr[12]),
            non_food_inflation_12_month_moving_average=Parse.percent(arr[13]),
        )

    @classmethod
    def parse_d_list(cls, arr_list):
        year_str = None
        d_list = []
        for arr in arr_list:
            print(len(arr), arr)
            if year_str is None and ("Year" in arr[0] or "Base" in arr[0]):
                continue
            if arr[0] != "":
                year_str = arr[0]
            if arr[1] == "" or "Weight" in arr[1]:
                continue
            d_list.append(cls.parse_row(arr, year_str))
        return d_list
