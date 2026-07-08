from dcs.ccpi.AbstractSourceDoc import AbstractSourceDoc
from dcs.ccpi.CCPI.CCPIParseMixin import CCPIParseMixin
from dcs.ccpi.CCPI.CCPIValidateMixin import CCPIValidateMixin
from utils_future import Log

log = Log("CCPI")


class CCPI(CCPIParseMixin, CCPIValidateMixin, AbstractSourceDoc):

    @classmethod
    def get_url(cls):
        return (
            "https://www.statistics.gov.lk"
            + "/Resource/en/InflationAndPrices/CCPI"
            + "/MOVEMENTS_of_CCPI_with_MV_Base2021.pdf"
        )

    @classmethod
    def get_name(cls):
        return "Movements of the CCPI"
