class Parse:
    @staticmethod
    def float(s):
        try:
            return float(s)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def percent(s):
        try:
            return float(s.strip("%")) / 100.0
        except (ValueError, TypeError):
            return None
