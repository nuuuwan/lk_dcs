from dcs.ccpi.AbstractSourceDoc import AbstractSourceDoc
from dcs.ccpi.CCPI.CCPIParseMixin import CCPIParseMixin
from dcs.ccpi.CCPI.CCPIValidateMixin import CCPIValidateMixin
from utils_future import Log, PDFFile

log = Log("CCPI")


class CCPI(AbstractSourceDoc, CCPIParseMixin, CCPIValidateMixin):

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

    @classmethod
    def from_file_path(cls, file_path):
        temp_pdf_file = PDFFile(file_path)
        arr_list = temp_pdf_file.get_tables()[0].df.values.tolist()

        d_list = cls.parse_d_list(arr_list)
        cls.validate_d_list(d_list)

        doc = cls(d_list[-1]["date_str"])

        doc.data_file.write(d_list)
        log.info(f"Wrote {doc.data_file}")

        doc.original_file.copy_from(temp_pdf_file)
        log.info(f"Wrote {doc.original_file}")

        return doc
