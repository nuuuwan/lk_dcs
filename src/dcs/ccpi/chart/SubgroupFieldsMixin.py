from dcs.ccpi.CCPISubgroups import CCPISubgroups


class SubgroupFieldsMixin:

    @staticmethod
    def label_of(slug):
        return slug.replace("-", " ").title()

    @classmethod
    def fields_for(cls, suffix):
        return {
            f"{slug}_{suffix}": cls.label_of(slug)
            for slug in CCPISubgroups.SUBGROUP_LABELS
        }
