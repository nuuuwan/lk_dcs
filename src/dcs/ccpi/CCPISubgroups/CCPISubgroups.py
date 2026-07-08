from dcs.ccpi.AbstractSourceDoc import AbstractSourceDoc
from dcs.ccpi.CCPISubgroups.CCPISubgroupsParseMixin import \
    CCPISubgroupsParseMixin
from dcs.ccpi.CCPISubgroups.CCPISubgroupsValidateMixin import \
    CCPISubgroupsValidateMixin
from utils_future import Log

log = Log("CCPISubgroups")


class CCPISubgroups(
    CCPISubgroupsParseMixin,
    CCPISubgroupsValidateMixin,
    AbstractSourceDoc,
):

    @classmethod
    def get_url(cls):
        return (
            "https://www.statistics.gov.lk"
            + "/Resource/en/InflationAndPrices/CCPI"
            + "/CCPI_2021_InflationSubGroupwiseChart.pdf"
        )

    @classmethod
    def get_name(cls):
        return "CCPI by subgroup"
