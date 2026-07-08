import os

from utils_future import Log
from utils_future.file.File import File

log = Log("ReadmeMixin")


class ReadmeMixin:

    @property
    def readme_file(self):
        return File(os.path.join(self.dir_data, "README.md"))

    @staticmethod
    def format_cell(value):
        if value is None:
            return ""
        return str(value)

    def get_lines_for_header(self):
        return [
            f"# {self.get_name()}",
            "",
            f"Latest Version **{self.date_str}** from <{self.get_url()}>",
            "",
        ]

    def get_lines_for_table(self):
        if not self.data_list:
            return []
        field_names = list(self.data_list[0].keys())
        lines = [
            "| " + " | ".join(field_names) + " |",
            "| " + " | ".join(["---"] * len(field_names)) + " |",
        ]
        for data in self.data_list:
            cells = [self.format_cell(data[name]) for name in field_names]
            lines.append("| " + " | ".join(cells) + " |")
        return lines

    def get_lines(self):
        return self.get_lines_for_header() + self.get_lines_for_table()

    def build_readme(self):
        self.readme_file.write_lines(self.get_lines())
        log.info(f"Wrote {self.readme_file}")
