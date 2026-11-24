import unittest
from viittauskirjasto import Viittauskirjasto
from lahdeviittaus import Lahdeviittaus

class TestViittauskirjasto(unittest.TestCase):
    def setUp(self):
        self.kirjasto = Viittauskirjasto()

    def test_uusi_kirjasto_on_tyhja(self):
        self.assertEqual(self.kirjasto.viitteet, [])