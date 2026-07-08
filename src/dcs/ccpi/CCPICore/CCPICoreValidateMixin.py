from datetime import datetime

TOLERANCE = 0.001

KEYS = ["ccpi", "ccpi_core"]


class CCPICoreValidateMixin:

    @staticmethod
    def check(date_str, field, expected, actual):
        if abs(expected - actual) > TOLERANCE:
            raise ValueError(
                f"{date_str}: {field} "
                f"expected ~{expected:.1f}%, got {actual:.1f}%"
            )

    @staticmethod
    def validate_months(dates):
        year, month = dates[0].year, dates[0].month
        for dt in dates:
            if (dt.year, dt.month) != (year, month):
                raise ValueError(
                    "Missing/out-of-order month: expected "
                    f"{year}-{month:02d}, got {dt.year}-{dt.month:02d}"
                )
            year, month = (year + 1, 1) if month == 12 else (year, month + 1)

    @classmethod
    def validate_change_month_to_month(cls, d_list, values, field):
        for i in range(1, len(d_list)):
            actual = d_list[i][field]
            if None in (values[i], values[i - 1], actual):
                continue
            expected = (values[i] - values[i - 1]) / values[i - 1]
            cls.check(d_list[i]["date_str"], field, expected, actual)

    @classmethod
    def validate_inflation_year_to_year(cls, d_list, values, field):
        for i in range(12, len(d_list)):
            actual = d_list[i][field]
            if None in (values[i], values[i - 12], actual):
                continue
            expected = (values[i] - values[i - 12]) / values[i - 12]
            cls.check(d_list[i]["date_str"], field, expected, actual)

    @staticmethod
    def is_window_valid(actual, recent, prev):
        return not (actual is None or None in recent or None in prev)

    @classmethod
    def validate_inflation_12mma(cls, d_list, values, field):
        for i in range(23, len(d_list)):
            actual = d_list[i][field]
            a, b, c = i - 23, i - 11, i + 1
            prev, recent = values[a:b], values[b:c]
            if not cls.is_window_valid(actual, recent, prev):
                continue
            expected = sum(recent) / sum(prev) - 1
            cls.check(d_list[i]["date_str"], field, expected, actual)

    @classmethod
    def validate_key(cls, d_list, key):
        values = [d[key] for d in d_list]
        cls.validate_change_month_to_month(
            d_list, values, f"{key}_change_month_to_month"
        )
        cls.validate_inflation_year_to_year(
            d_list, values, f"inflation_{key}_year_to_year"
        )
        cls.validate_inflation_12mma(
            d_list, values, f"inflation_{key}_12_month_moving_average"
        )

    @classmethod
    def validate_d_list(cls, d_list):
        dates = [datetime.strptime(d["date_str"], "%Y-%m-%d") for d in d_list]
        cls.validate_months(dates)
        for key in KEYS:
            cls.validate_key(d_list, key)
