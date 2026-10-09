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

    @staticmethod
    def _is_valid_year_candidate(year_candidate):
        return not year_candidate or (
            len(year_candidate) == 4 and year_candidate.isdigit()
        )

    @staticmethod
    def _should_skip_row(arr):
        return arr[1] == "" or "Weight" in arr[1]

    @classmethod
    def parse_d_list(cls, arr_list):
        year_str = None
        d_list = []
        for arr in arr_list:
            year_candidate = arr[0].strip()
            if not cls._is_valid_year_candidate(year_candidate):
                continue
            if year_candidate:
                year_str = year_candidate
            if cls._should_skip_row(arr):
                continue
            d_list.append(cls.parse_row(arr, year_str))
        return d_list
