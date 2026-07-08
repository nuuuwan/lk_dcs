from utils_future import Parse, TimeFormat


class CCPIParseMixin:

    @staticmethod
    def parse_date_str(year_str, month_str):
        return TimeFormat.DATE.format(
            TimeFormat("%Y-%B").parse(f"{year_str}-{month_str}")
        )

    @classmethod
    def parse_row(cls, arr, year_str):
        return dict(
            date_str=cls.parse_date_str(year_str, arr[1]),
            ccpi=Parse.float(arr[2]),
            change_month_to_month=Parse.percent(arr[3]),
            inflation_year_to_year=Parse.percent(arr[4]),
            inflation_12_month_moving_average=Parse.percent(arr[6]),
        )

    @classmethod
    def parse_d_list(cls, arr_list):
        year_str = None
        d_list = []
        for arr in arr_list:
            if year_str is None and arr[0] in ("Year", ""):
                continue
            if len(arr[0].strip()) not in [0, 4]:
                continue
            if arr[0] != "":
                year_str = arr[0]
            d_list.append(cls.parse_row(arr, year_str))
        return d_list
