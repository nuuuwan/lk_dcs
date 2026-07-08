from dcs.ccpi.AbstractSourceDoc import AbstractSourceDoc
from dcs.ccpi.InflationByFoodAndNonFoodGroups.ParseMixin import ParseMixin
from dcs.ccpi.InflationByFoodAndNonFoodGroups.ValidateMixin import \
    ValidateMixin
from utils_future import Log

log = Log("InflationByFoodAndNonFoodGroups")


class InflationByFoodAndNonFoodGroups(
    ParseMixin, ValidateMixin, AbstractSourceDoc
):

    @classmethod
    def get_url(cls):
        return (
            "https://www.statistics.gov.lk"
            + "/Resource/en/InflationAndPrices/CCPI"
            + "/CCPI_2021_InflationFoodAndNonFood.pdf"
        )

    @classmethod
    def get_name(cls):
        return "Inflation by Food and Non Food Groups"
