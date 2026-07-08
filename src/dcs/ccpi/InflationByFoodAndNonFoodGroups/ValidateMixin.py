from datetime import datetime


class ValidateMixin:

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
    def validate_d_list(cls, d_list):
        dates = [datetime.strptime(d["date_str"], "%Y-%m-%d") for d in d_list]
        cls.validate_months(dates)
