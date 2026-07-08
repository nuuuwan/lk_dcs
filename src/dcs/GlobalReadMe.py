from dcs.ccpi.DocFactory import DocFactory
from utils_future import File, Log, Time, TimeFormat

log = Log("GlobalReadMe")


class GlobalReadMe:
    @staticmethod
    def build_doc_line(doc_cls):
        return f"- [{doc_cls.get_name()}]({doc_cls.get_dir_cls_data()})"

    @staticmethod
    def get_lines_for_header() -> list[str]:
        time_str = TimeFormat.DATE.format(Time.now())
        time_str = time_str.replace("-", "--").replace(" ", "_")
        return [
            "![Last Updated](https://img.shields.io/badge/"
            + f"last_updated-{time_str}-green)",
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
