from dcs.ccpi.DocFactory import DocFactory
from utils_future import File, Log, Time, TimeFormat

log = Log("GlobalReadMe")


class GlobalReadMe:
    @staticmethod
    def build_doc_line(doc_cls):
        latest_doc = doc_cls.latest()
        return f"- [{latest_doc.label}]({latest_doc.dir_data})"

    @staticmethod
    def get_last_update_date_str():
        latest_date_str = None
        for doc_cls in DocFactory.list():
            latest_doc = doc_cls.latest()
            date_str = latest_doc.date_str
            if latest_date_str is None or date_str > latest_date_str:
                latest_date_str = date_str
        return latest_date_str

    @staticmethod
    def get_lines_for_header() -> list[str]:
        latest_date_str = TimeFormat("%Y %b").format(
            TimeFormat.DATE.parse(GlobalReadMe.get_last_update_date_str())
        )
        latest_date_str = latest_date_str.replace("-", "--").replace(" ", "_")
        update_date_str = TimeFormat.DATE.format(Time.now())
        update_date_str = update_date_str.replace("-", "--").replace(" ", "_")
        return [
            "![Latest Data](https://img.shields.io/badge/"
            + f"latest_data-{latest_date_str}-green)",
            "![Last Checked](https://img.shields.io/badge/"
            + f"last_checked-{update_date_str}-purple)",
            "",
        ]

    @staticmethod
    def get_lines_for_introduction() -> list[str]:
        return [
            "This repo contains public data parsed from"
            + " [https://www.statistics.gov.lk/]"
            + "(https://www.statistics.gov.lk/).",
            "",
        ]

    @staticmethod
    def get_lines_for_ccpi() -> list[str]:
        lines = [
            "## Colombo Consumer Price Index (CCPI)",
            "",
        ]
        for doc_cls in DocFactory.list():
            lines.append(GlobalReadMe.build_doc_line(doc_cls))
        lines.append("")
        return lines

    @staticmethod
    def get_lines_for_footer() -> list[str]:
        return [
            "![Maintainer]"
            + "(https://img.shields.io/badge/maintainer-nuuuwan-red)",
            "![MadeWith](https://img.shields.io/badge/made_with-python-blue)",
            "[![License: MIT]"
            + "(https://img.shields.io/badge/License-MIT-yellow.svg)]"
            + "(https://opensource.org/licenses/MIT)",
        ]

    @staticmethod
    def get_lines():
        lines = [
            "# Department of Census and Statistics, Sri Lanka 🇱🇰",
            "",
        ]
        lines.extend(GlobalReadMe.get_lines_for_header())
        lines.extend(GlobalReadMe.get_lines_for_introduction())
        lines.extend(GlobalReadMe.get_lines_for_ccpi())
        lines.extend(GlobalReadMe.get_lines_for_footer())
        return lines

    @staticmethod
    def build():
        readme_file = File("README.md")
        content = "\n".join(GlobalReadMe.get_lines()) + "\n"
        readme_file.write(content)
        log.info(f"Wrote {readme_file}")
        return readme_file
