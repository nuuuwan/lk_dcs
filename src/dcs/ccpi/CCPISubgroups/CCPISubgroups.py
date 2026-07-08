from dcs.ccpi.AbstractSourceDoc import AbstractSourceDoc
from dcs.ccpi.CCPISubgroups.CCPISubgroupsParseMixin import (
    CCPISubgroupsParseMixin,
)
from dcs.ccpi.CCPISubgroups.CCPISubgroupsValidateMixin import (
    CCPISubgroupsValidateMixin,
)
from utils_future import Log

log = Log("CCPISubgroups")


class CCPISubgroups(
    AbstractSourceDoc,
    CCPISubgroupsParseMixin,
    CCPISubgroupsValidateMixin,
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

    @staticmethod
    def get_latest_date_str(d_list):
        dates = set()
        for d in d_list:
            dates.update(d["series"].keys())
        return max(dates)

    @classmethod
    def from_pdf_file(cls, pdf_file):
        arr_list = pdf_file.get_tables()[0].df.values.tolist()

        d_list = cls.parse_d_list(arr_list)
        cls.validate_d_list(d_list)

        doc = cls(cls.get_latest_date_str(d_list))

        doc.data_file.write(d_list)
        log.info(f"Wrote {doc.data_file}")

        return doc
