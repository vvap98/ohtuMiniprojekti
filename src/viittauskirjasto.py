from lahdeviittaus import Lahdeviittaus

class Viittauskirjasto:
    def __init__(self):
        self.viitteet = []

    def lisaa_viite(self, teksti):
        lahde_viittaus = Lahdeviittaus(teksti)
        self.viitteet.append(lahde_viittaus)