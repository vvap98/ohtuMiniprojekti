import unittest
from lahdeviittaus import Lahdeviittaus

class TestLahdeviittaus(unittest.TestCase):

    def test_str_muotoilee_viitteen(self):
        viite = Lahdeviittaus("Tuntematon sotilas", "1954", "Väinö Linna")
        self.assertEqual(str(viite), "Teos: Tuntematon sotilas, Vuosi: 1954, Kirjoittaja: Väinö Linna")