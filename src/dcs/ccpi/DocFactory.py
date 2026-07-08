from dcs.ccpi.CCPI import CCPI
from dcs.ccpi.CCPICore import CCPICore
from dcs.ccpi.InflationByFoodAndNonFoodGroups import (
    InflationByFoodAndNonFoodGroups,
)


class DocFactory:
    @staticmethod
    def list():
        return [
            CCPI,
            CCPICore,
            InflationByFoodAndNonFoodGroups,
        ]
