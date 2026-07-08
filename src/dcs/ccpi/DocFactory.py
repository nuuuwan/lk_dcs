from dcs.ccpi.CCPI import CCPI
from dcs.ccpi.CCPICore import CCPICore
from dcs.ccpi.CCPISubgroups import CCPISubgroups
from dcs.ccpi.InflationByFoodAndNonFoodGroups import \
    InflationByFoodAndNonFoodGroups


class DocFactory:
    @staticmethod
    def list():
        return [
            CCPI,
            CCPICore,
            CCPISubgroups,
            InflationByFoodAndNonFoodGroups,
        ]
