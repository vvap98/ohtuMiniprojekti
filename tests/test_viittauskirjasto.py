import unittest
import os
import tempfile
from viittauskirjasto import Viittauskirjasto
from lahdeviittaus import Lahdeviittaus

class TestViittauskirjasto(unittest.TestCase):
    def setUp(self):
        self.alkuperainen_kansio = os.getcwd()
        self.tmp = tempfile.TemporaryDirectory()
        os.chdir(self.tmp.name)
        os.makedirs("data")
        self.kirjasto = Viittauskirjasto()

    def tearDown(self):
        os.chdir(self.alkuperainen_kansio)
        self.tmp.cleanup()

    def test_uusi_kirjasto_on_tyhja(self):
        self.assertEqual(self.kirjasto.viitteet, [])

    def test_poista_viite(self):
        self.kirjasto.lisaa_viite("Teos1", 2026, "Kirjoittaja1")
        self.kirjasto.lisaa_viite("Teos2", 2026, "Kirjoittaja2")

        self.kirjasto.poista_viite("Teos2")

        self.assertEqual(len(self.kirjasto.viitteet), 1)

    def test_virheellinen_poisto_ei_onnistu(self):
        self.kirjasto.lisaa_viite("Teos1", 2026, "Kirjoittaja1")
        self.kirjasto.lisaa_viite("Teos2", 2026, "Kirjoittaja2")

        self.kirjasto.poista_viite("Teos")

        self.assertEqual(len(self.kirjasto.viitteet), 2)