from lahdeviittaus import Lahdeviittaus
from viitteet_json import JsonHandler

class Viittauskirjasto:
    def __init__(self):
        self.viitteet = []

    def lisaa_viite(self, teos, vuosiluku, kirjoittaja):
        lahde_viittaus = Lahdeviittaus(teos, vuosiluku, kirjoittaja)
        self.viitteet.append(lahde_viittaus)
        self.tallenna()

    def poista_viite(self, teos):
        poistettu = False
        for lahde_viittaus in self.viitteet:
            if lahde_viittaus.teos == teos:
                self.viitteet.remove(lahde_viittaus)
                self.tallenna
                poistettu = True

        return poistettu

    def tallenna(self):
        json_kasittely = JsonHandler()
        json_kasittely.tallenna(self.viitteet)

    def lataa(self):
        json_kasittely = JsonHandler()
        print(json_kasittely.lataa())