import io
import unittest
from unittest.mock import patch

import pandas as pd

from tvscreener import StockScreener, TimeInterval, SymbolType, SubMarket, Country, Exchange, MalformedRequestException, \
    Filter, FilterType, FilterOperator


class TestScreener(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_stdout(self, mock_stdout):
        ss = StockScreener()
        ss.get(print_request=True)
        self.assertIn("filter", mock_stdout.getvalue())

    def test_malformed_request(self):
        ss = StockScreener()
        fake_filter = Filter(FilterType.TYPE, FilterOperator.ABOVE_OR_EQUAL, "test")
        ss.add_filter(fake_filter)
        with self.assertRaises(MalformedRequestException):
            ss.get()

    def test_range(self):
        ss = StockScreener()
        df = ss.get()
        self.assertEqual(150, len(df))

    def test_time_interval(self):
        ss = StockScreener()
        df = ss.get(time_interval=TimeInterval.FOUR_HOURS)
        self.assertEqual(150, len(df))

    def test_search(self):
        ss = StockScreener()
        ss.set_subtypes(SymbolType.COMMON_STOCK)
        ss.search('AA')
        df = ss.get()
        self.assertEqual(102, len(df))

        self.assertEqual(df.loc[0, "Symbol"], "NASDAQ:AAPL")
        self.assertEqual(df.loc[0, "Name"], "AAPL")

    def test_column_order(self):
        ss = StockScreener()
        df = ss.get()

        self.assertEqual(df.columns[0], "Symbol")
        self.assertEqual(df.columns[1], "Name")
        self.assertEqual(df.columns[2], "Description")

        self.assertEqual(df.loc[0, "Symbol"], "NASDAQ:AAPL")
        self.assertEqual(df.loc[0, "Name"], "AAPL")

    def test_not_multiindex(self):
        ss = StockScreener()
        df = ss.get()
        self.assertIsInstance(df.index, pd.Index)

        self.assertEqual(df.columns[0], "Symbol")
        self.assertEqual(df.columns[1], "Name")
        self.assertEqual(df.columns[2], "Description")

        self.assertEqual(df.loc[0, "Symbol"], "NASDAQ:AAPL")
        self.assertEqual(df.loc[0, "Name"], "AAPL")

    def test_multiindex(self):
        ss = StockScreener()
        df = ss.get()
        df.set_technical_columns()
        self.assertNotIsInstance(df.index, pd.MultiIndex)

        self.assertEqual(df.columns[0], ("symbol", "Symbol"))
        self.assertEqual(df.columns[1], ("name", "Name"))
        self.assertEqual(df.columns[2], ("description", "Description"))

        self.assertEqual(df.loc[0, ("symbol", "Symbol")], "NASDAQ:AAPL")
        self.assertEqual(df.loc[0, ("name", "Name")], "AAPL")

    def test_technical_index(self):
        ss = StockScreener()
        df = ss.get()
        df.set_technical_columns(only=True)
        self.assertIsInstance(df.index, pd.Index)

        self.assertEqual(df.columns[0], "symbol")
        self.assertEqual(df.columns[1], "name")
        self.assertEqual(df.columns[2], "description")

        self.assertEqual(df.loc[0, "symbol"], "NASDAQ:AAPL")
        self.assertEqual(df.loc[0, "name"], "AAPL")

    def test_primary_filter(self):
        ss = StockScreener()
        ss.set_primary_listing()
        df = ss.get()
        self.assertEqual(150, len(df))

        self.assertEqual(df.loc[0, "Symbol"], "NASDAQ:AAPL")
        self.assertEqual(df.loc[0, "Name"], "AAPL")

    def test_submarket(self):
        ss = StockScreener()
        ss.set_submarkets(SubMarket.OTCQB)
        df = ss.get()
        self.assertEqual(150, len(df))

        self.assertEqual(df.loc[0, "Symbol"], "OTC:PLDGP")
        self.assertEqual(df.loc[0, "Name"], "PLDGP")

    def test_submarket_pink(self):
        ss = StockScreener()
        ss.set_submarkets(SubMarket.PINK)
        df = ss.get()
        self.assertEqual(150, len(df))

        self.assertEqual(df.loc[0, "Symbol"], "OTC:LVMHF")
        self.assertEqual(df.loc[0, "Name"], "LVMHF")

    def test_country(self):
        ss = StockScreener()
        ss.set_countries(Country.ARGENTINA)
        df = ss.get()
        self.assertEqual(17, len(df))

        self.assertEqual(df.loc[0, "Symbol"], "NYSE:YPF")
        self.assertEqual(df.loc[0, "Name"], "YPF")

    def test_countries(self):
        ss = StockScreener()
        ss.set_countries(Country.ARGENTINA, Country.BERMUDA)
        df = ss.get()
        self.assertEqual(106, len(df))

        # WARNING: Order is not guaranteed
        # self.assertEqual("NASDAQ:ACGL", df.loc[0, "Symbol"])
        # self.assertEqual("ACGL", df.loc[0, "Name"])

    def test_exchange(self):
        ss = StockScreener()
        ss.set_exchanges(Exchange.NYSE_ARCA)
        df = ss.get()
        self.assertEqual(150, len(df))

        self.assertEqual(df.loc[0, "Symbol"], "AMEX:LNG")
        self.assertEqual(df.loc[0, "Name"], "LNG")
