import unittest

from dcs.ccpi.CCPICore.CCPICoreParseMixin import CCPICoreParseMixin


class TestCCPICoreParseMixin(unittest.TestCase):
    def test_parse_d_list_normalizes_eleven_column_rows(self):
        row = [
            "2026",
            "September",
            "209.1",
            "190.9",
            "0.1%",
            "",
            "0.4%",
            "8.0%",
            "5.4%",
            "4.5%",
            "3.4%",
        ]
        parsed = CCPICoreParseMixin.parse_d_list(
            [["Year Month"] + [""] * 10, row]
        )

        self.assertEqual(len(parsed), 1)
        self.assertEqual(parsed[0]["date_str"], "2026-09-01")
        self.assertAlmostEqual(
            parsed[0]["ccpi_core_change_month_to_month"], 0.004
        )
