from datetime import datetime

TOLERANCE = 0.1


class CCPIValidateMixin:

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

    @staticmethod
    def check(date_str, field, expected, actual):
        if abs(expected - actual) > TOLERANCE:
            raise ValueError(
                f"{date_str}: {field} "
                f"expected ~{expected:.1f}, got {actual}"
            )

    @classmethod
    def validate_change_month_to_month(cls, d_list, ccpi):
        for i in range(1, len(d_list)):
            actual = d_list[i]["change_month_to_month"]
            if None in (ccpi[i], ccpi[i - 1], actual):
                continue
            expected = (ccpi[i] - ccpi[i - 1]) / ccpi[i - 1] * 100
            cls.check(
                d_list[i]["date_str"],
                "change_month_to_month",
                expected,
                actual,
            )

    @classmethod
    def validate_inflation_year_to_year(cls, d_list, ccpi):
        for i in range(12, len(d_list)):
            actual = d_list[i]["inflation_year_to_year"]
            if None in (ccpi[i], ccpi[i - 12], actual):
                continue
            expected = (ccpi[i] - ccpi[i - 12]) / ccpi[i - 12] * 100
            cls.check(
                d_list[i]["date_str"],
                "inflation_year_to_year",
                expected,
                actual,
            )

    @staticmethod
    def is_window_valid(actual, recent, prev):
        return not (actual is None or None in recent or None in prev)

    @classmethod
    def validate_inflation_12mma(cls, d_list, ccpi):
        for i in range(23, len(d_list)):
            actual = d_list[i]["inflation_12_month_moving_average"]
            a, b, c = i - 23, i - 11, i + 1
            prev, recent = ccpi[a:b], ccpi[b:c]
            if not cls.is_window_valid(actual, recent, prev):
                continue
            expected = (sum(recent) / sum(prev) - 1) * 100
            cls.check(
                d_list[i]["date_str"],
                "inflation_12_month_moving_average",
                expected,
                actual,
            )

    @classmethod
    def validate_d_list(cls, d_list):
        dates = [datetime.strptime(d["date_str"], "%Y-%m-%d") for d in d_list]
        ccpi = [d["ccpi"] for d in d_list]
        cls.validate_months(dates)
        cls.validate_change_month_to_month(d_list, ccpi)
        cls.validate_inflation_year_to_year(d_list, ccpi)
        cls.validate_inflation_12mma(d_list, ccpi)
