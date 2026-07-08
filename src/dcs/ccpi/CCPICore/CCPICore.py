from dcs.ccpi.AbstractSourceDoc import AbstractSourceDoc
from dcs.ccpi.CCPICore.CCPICoreParseMixin import CCPICoreParseMixin
from dcs.ccpi.CCPICore.CCPICoreValidateMixin import CCPICoreValidateMixin
from utils_future import Log

log = Log("CCPICore")


class CCPICore(AbstractSourceDoc, CCPICoreParseMixin, CCPICoreValidateMixin):

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

    @classmethod
    def from_pdf_file(cls, pdf_file):
        arr_list = pdf_file.get_tables()[0].df.values.tolist()

        d_list = cls.parse_d_list(arr_list)
        cls.validate_d_list(d_list)

        doc = cls(d_list[-1]["date_str"])

        doc.data_file.write(d_list)
        log.info(f"Wrote {doc.data_file}")

        return doc
