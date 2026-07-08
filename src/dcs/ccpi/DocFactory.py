from dcs.ccpi.CCPI import CCPI
from dcs.ccpi.CCPICore import CCPICore


class DocFactory:
    @staticmethod
    def list():
        return [
            CCPI,
            CCPICore,
        ]
