from dcs.ccpi.AbstractSourceDoc import AbstractSourceDoc
from dcs.ccpi.CCPICore.CCPICoreParseMixin import CCPICoreParseMixin
from dcs.ccpi.CCPICore.CCPICoreValidateMixin import CCPICoreValidateMixin
from utils_future import Log

log = Log("CCPICore")


class CCPICore(CCPICoreParseMixin, CCPICoreValidateMixin, AbstractSourceDoc):

    @classmethod
    def get_url(cls):
        return (
            "https://www.statistics.gov.lk"
            + "/Resource/en/InflationAndPrices/CCPI"
            + "/Movements_of_CCPI-CCPI_Core_2021.pdf"
        )

    @classmethod
    def get_name(cls):
        return "Movements of the CCPI Core"
