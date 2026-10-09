import unittest

from dcs.ccpi.InflationByFoodAndNonFoodGroups.ParseMixin import ParseMixin


class TestParseMixin(unittest.TestCase):
    def test_parse_d_list_skips_metadata_and_year_header(self):
        row = [
            "2026",
            "September",
            "209.1",
            "0.1%",
            "8.0%",
            "4.5%",
            "100.0",
            "0.0%",
            "8.0%",
            "4.5%",
            "100.0",
            "0.0%",
            "8.0%",
            "4.5%",
        ]
        parsed = ParseMixin.parse_d_list(
            [["Base Value"], ["Year", "Month"], row]
        )

        self.assertEqual(len(parsed), 1)
        self.assertEqual(parsed[0]["date_str"], "2026-09-01")
        self.assertEqual(parsed[0]["all_ccpi"], 209.1)
