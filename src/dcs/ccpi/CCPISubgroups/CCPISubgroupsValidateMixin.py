class CCPISubgroupsValidateMixin:

    @staticmethod
    def validate_not_empty(d_list):
        if not d_list:
            raise ValueError("No subgroup rows parsed")

    @staticmethod
    def validate_subgroups(d_list):
        subgroups = [d["subgroup"] for d in d_list]
        if "" in subgroups:
            raise ValueError("Empty subgroup name")
        if len(set(subgroups)) != len(subgroups):
            raise ValueError("Duplicate subgroup names")

    @staticmethod
    def validate_series(d_list):
        for d in d_list:
            if not d["series"]:
                raise ValueError(f"No values for subgroup {d['subgroup']}")

    @classmethod
    def validate_d_list(cls, d_list):
        cls.validate_not_empty(d_list)
        cls.validate_subgroups(d_list)
        cls.validate_series(d_list)
