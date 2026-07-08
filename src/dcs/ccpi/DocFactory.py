from dcs.ccpi.CCPI import CCPI
from dcs.ccpi.InflationByFoodAndNonFoodGroups import (
    InflationByFoodAndNonFoodGroups,
)


class DocFactory:
    @staticmethod
    def list():
        return [
            CCPI,
            InflationByFoodAndNonFoodGroups,
        ]
