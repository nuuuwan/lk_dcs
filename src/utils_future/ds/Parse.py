class Parse:
    PRECISION_FLOAT = 1
    PRECISION_PERCENT = 3

    @staticmethod
    def float(s):
        try:
            return round(float(s), Parse.PRECISION_FLOAT)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def percent(s):
        try:
            return round(float(s.strip("%")) / 100.0, Parse.PRECISION_PERCENT)
        except (ValueError, TypeError):
            return None
