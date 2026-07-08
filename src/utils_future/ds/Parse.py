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

    @staticmethod
    def custom(type_label, x):
        if type_label == "float":
            return Parse.float(x)
        if type_label == "percent":
            return Parse.percent(x)
        raise ValueError(f"Unknown type label: {type_label}")
