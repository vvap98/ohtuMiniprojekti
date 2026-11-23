class App:
    def __init__(self, viittaus_kirjasto, io):
        self.viittaus_kirjasto = viittaus_kirjasto
        self.io = io

    def run(self):
        self.io.write("Tervetuloa viittauskirjastoon!")
        while True:
            komento = self.io.read("Anna komento (lisaa, nayta, lopeta): ")
            if komento == "lisaa":
                teksti = self.io.read("Anna viitteen teksti: ")
                self.viittaus_kirjasto.lisaa_viite(teksti)

                self.io.write("Viite lisätty.")
            elif komento == "nayta":
                for viite in self.viittaus_kirjasto.viitteet:
                    self.io.write(viite)
            elif komento == "lopeta":
                return
            else:
                self.io.write("Tuntematon komento.")
