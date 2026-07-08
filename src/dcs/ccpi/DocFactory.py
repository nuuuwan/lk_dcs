from dcs.ccpi.CCPI import CCPI
from dcs.ccpi.CCPISubgroups import CCPISubgroups


class DocFactory:
    @staticmethod
    def list():
        return [
            CCPI,
            CCPISubgroups,
        ]
