from utils_future import Parse, TimeFormat

MONTH_FORMATS = [
    "%b-%y",
    "%b-%Y",
    "%B-%Y",
    "%Y-%b",
    "%Y-%B",
    "%b %Y",
    "%B %Y",
]


class CCPISubgroupsParseMixin:

    @staticmethod
    def parse_month_label(label):
        for fmt in MONTH_FORMATS:
            try:
                return TimeFormat.DATE.format(
                    TimeFormat(fmt).parse(label.strip())
                )
            except (ValueError, AttributeError):
                continue
        return None

    @classmethod
    def parse_col_dates(cls, arr):
        col_dates = {}
        for i, label in enumerate(arr):
            date_str = cls.parse_month_label(label)
            if date_str is not None:
                col_dates[i] = date_str
        return col_dates

    @classmethod
    def find_header(cls, arr_list):
        for index, arr in enumerate(arr_list):
            col_dates = cls.parse_col_dates(arr)
            if len(col_dates) >= 2:
                return index, col_dates
        return None, {}

    @classmethod
    def parse_row(cls, arr, col_dates):
        return dict(
            subgroup=arr[0].strip(),
            series={
                date_str: Parse.float(arr[i])
                for i, date_str in col_dates.items()
            },
        )

    @classmethod
    def parse_d_list(cls, arr_list):
        header_index, col_dates = cls.find_header(arr_list)
        if header_index is None:
            return []
        d_list = []
        start = header_index + 1
        for arr in arr_list[start:]:
            if arr[0].strip() == "":
                continue
            d_list.append(cls.parse_row(arr, col_dates))
        return d_list
