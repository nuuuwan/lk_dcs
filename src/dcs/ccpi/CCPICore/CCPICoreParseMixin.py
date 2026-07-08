from utils_future import Parse, TimeFormat


class CCPICoreParseMixin:

    @staticmethod
    def parse_date_str(year_str, month_str):
        return TimeFormat.DATE.format(
            TimeFormat("%Y-%B").parse(f"{year_str}-{month_str}")
        )

    @classmethod
    def parse_row(cls, arr, year_str):
        # remove null row
        arr = arr[:5] + arr[6:]

        if len(arr) != 10:
            raise ValueError("Invalid row format: " + str(arr))

        return dict(
            date_str=cls.parse_date_str(year_str, arr[1]),
            #
            ccpi=Parse.float(arr[2]),
            ccpi_core=Parse.float(arr[3]),
            #
            ccpi_change_month_to_month=Parse.percent(arr[4]),
            ccpi_core_change_month_to_month=Parse.percent(arr[5]),
            #
            inflation_ccpi_year_to_year=Parse.percent(arr[6]),
            inflation_ccpi_core_year_to_year=Parse.percent(arr[7]),
            inflation_ccpi_12_month_moving_average=Parse.percent(arr[8]),
            inflation_ccpi_core_12_month_moving_average=Parse.percent(arr[9]),
        )

    @classmethod
    def parse_d_list(cls, arr_list):
        year_str = None
        d_list = []
        for arr in arr_list:
            if year_str is None and ("Year" in arr[0] or arr[0] == ""):
                continue
            if arr[0] != "":
                year_str = arr[0]
            if len(arr[0].strip()) not in [0, 4]:
                continue
            if arr[1] == "":
                continue
            d_list.append(cls.parse_row(arr, year_str))
        return d_list
