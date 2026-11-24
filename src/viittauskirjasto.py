from lahdeviittaus import Lahdeviittaus

class Viittauskirjasto:
    def __init__(self):
        self.viitteet = []

    def lisaa_viite(self, teos, vuosiluku, kirjoittaja):
        lahde_viittaus = Lahdeviittaus(teos, vuosiluku, kirjoittaja)
        self.viitteet.append(lahde_viittaus)