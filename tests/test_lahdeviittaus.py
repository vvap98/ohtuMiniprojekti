import unittest
from lahdeviittaus import Lahdeviittaus

class TestLahdeviittaus(unittest.TestCase):

    def test_str_muotoilee_viitteen(self):
        viite = Lahdeviittaus("Lorem Ipsum")
        self.assertEqual(str(viite), "Viite: Lorem Ipsum")