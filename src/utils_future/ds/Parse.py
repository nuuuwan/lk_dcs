class Parse:
    @staticmethod
    def float(s):
        try:
            return float(s)
        except (ValueError, TypeError):
            return None
