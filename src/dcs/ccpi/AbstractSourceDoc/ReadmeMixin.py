import os

from utils_future import File, Log, TimeFormat

log = Log("ReadmeMixin")


class ReadmeMixin:

    @property
    def readme_file(self):
        return File(os.path.join(self.dir_data, "README.md"))

    @staticmethod
    def format_cell(value, name):
        if value is None:
            return "`-`"
        if name == "date_str":
            return TimeFormat("%Y %b").format(TimeFormat.DATE.parse(value))

        value = float(value)
        if "inflation" in name:
            return f"{value:+.1%}"
        if "change" in name:
            return f"{value:+.1%}"
        return f"{value:.1f}"

    def get_lines_for_header(self):
        return [
            f"# {self.get_name()}",
            "",
            f"Latest Version **{self.date_str}** from <{self.get_url()}>",
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
        return lines

    def get_lines(self):
        return (
            self.get_lines_for_header()
            + self.get_lines_for_files()
            + self.get_lines_for_table()
        )

    def build_readme(self):
        self.readme_file.write_lines(self.get_lines())
        log.info(f"Wrote {self.readme_file}")
