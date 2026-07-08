import camelot

from utils_future.file.File import File, Log

log = Log("PDFFile")


class PDFFile(File):

    def get_tables(self):
        tables = camelot.read_pdf(
            self.path, pages="all", flavor="stream", edge_tol=500
        )
        shapes = [t.df.shape for t in tables]
        log.debug(f"Extracted {len(tables)} tables {shapes} from {self}")
        return tables
