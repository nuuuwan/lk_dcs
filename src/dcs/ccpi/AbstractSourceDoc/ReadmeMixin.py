import json
import os

from utils_future import File, Log, Time, TimeFormat

log = Log("ReadmeMixin")


class ReadmeMixin:

    @property
    def readme_file(self):
        return File(os.path.join(self.dir_data, "README.md"))

    @staticmethod
    # flake8: noqa: CFQ004
    def format_cell(value, name):
        if value is None:
            return "`-`"
        if name == "date_str":
            return f"`{value[:7]}`"
        value = float(value)
        if "inflation" in name:
            return f"{value:+.1%}"
        if "change" in name:
            return f"{value:+.1%}"
        return f"{value:.1f}"

    def get_lines_for_header(self) -> list[str]:
        latest_date_str = TimeFormat("%Y %b").format(
            TimeFormat.DATE.parse(self.date_str)
        )
        latest_date_str = latest_date_str.replace("-", "--").replace(" ", "_")
        update_date_str = TimeFormat.DATE.format(Time.now())
        update_date_str = update_date_str.replace("-", "--").replace(" ", "_")
        return [
            f"# {self.label}",
            "",
            "![Latest Data](https://img.shields.io/badge/"
            + f"latest_data-{latest_date_str}-green)",
            "![Last Checked](https://img.shields.io/badge/"
            + f"last_checked-{update_date_str}-purple)",
            "",
        ]

    def get_lines_for_files(self):
        lines = ["## Files", ""]
        for label, file in [
            ("Original PDF", self.original_file),
            ("Data JSON", self.data_file),
            ("Data TSV", self.tsv_data_file),
        ]:
            lines.append(f"- [{label}](../../../../../{file.path})")
        lines.append("")
        return lines

    def get_lines_for_latest(self):
        lines = [
            "## Latest Data",
            "",
            "```json",
            json.dumps(
                self.data_list[-1],
                indent=4,
            ),
            "```",
            "",
        ]

        return lines

    def get_lines_for_table(self):
        field_names = list(self.data_list[0].keys())
        field_name_labels = [n.replace("_", " ").title() for n in field_names]
        lines = [
            "## Data Table",
            "",
            "| " + " | ".join(field_name_labels) + " |",
            "| " + " | ".join(["--:"] * len(field_name_labels)) + " |",
        ]
        for data in self.data_list:
            cells = [
                self.format_cell(data[name], name) for name in field_names
            ]
            lines.append("| " + " | ".join(cells) + " |")

        lines.extend(["", f"Source: <{self.get_url()}>", ""])
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

    def get_lines(self):
        return (
            self.get_lines_for_header()
            + self.get_lines_for_files()
            + self.get_lines_for_latest()
            + self.get_lines_for_table()
            + self.get_lines_for_footer()
        )

    def build_readme(self):
        self.readme_file.write_lines(self.get_lines())
        log.info(f"Wrote {self.readme_file}")
