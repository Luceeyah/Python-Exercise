import unittest
from config_parser import parse_config

class Test(unittest.TestCase):
  def test_example_case(self):
    """ example case """
    expected = {
      "owner": {
        "name": "John Doe",
        "organization": "Acme Widgets Inc.",
        "active": True,
        "rate": 2.03
      },
      "database": {
        "server": "192.0.2.62",
        "port": 143,
        "file": "\"payroll.dat\"",
        "connection": ""
      },
    }
    actual = parse_config("config_files/sample.ini")
    self.assertEqual(actual, expected)

  def test_generic_case(self):
    """ generic case """
    expected = {
      "section": {
        "b": False,
        "f": 206.201,
        "i": -55,
        "i1": 1,
        "b1": True,
        "b2": False,
        "s": "",
      },
    }
    actual = parse_config("config_files/generic.ini")
    self.assertEqual(actual, expected)