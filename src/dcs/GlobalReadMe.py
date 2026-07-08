from dcs.ccpi.DocFactory import DocFactory
from utils_future import Log
from utils_future.file.File import File

log = Log("GlobalReadMe")


class GlobalReadMe:
    @staticmethod
    def build_doc_line(cls):
        return f"- [{cls.get_name()}]({cls.get_url()})"

    @staticmethod
    def build_lines():
        lines = ["# lk_dcs", "", "## Documents", ""]
        for cls in DocFactory.list():
            lines.append(GlobalReadMe.build_doc_line(cls))
        return lines

    @staticmethod
    def build():
        readme_file = File("README.md")
        content = "\n".join(GlobalReadMe.build_lines()) + "\n"
        readme_file.write(content)
        log.info(f"Wrote {readme_file}")
        return readme_file
