from lahdeviittaus import Lahdeviittaus
from viitteet_json import JsonHandler

class Viittauskirjasto:
    def __init__(self):
        self.viitteet = []

    def lisaa_viite(self, teos, vuosiluku, kirjoittaja):
        lahde_viittaus = Lahdeviittaus(teos, vuosiluku, kirjoittaja)
        self.viitteet.append(lahde_viittaus)
        self.tallenna()

    def tallenna(self):
        json_kasittely = JsonHandler()
        json_kasittely.tallenna(self.viitteet)

    def lataa(self):
        json_kasittely = JsonHandler()
        print(json_kasittely.lataa())