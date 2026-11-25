class App:
    def __init__(self, viittaus_kirjasto, io):
        self.viittaus_kirjasto = viittaus_kirjasto
        self.io = io

    def run(self):
        self.io.write("Tervetuloa viittauskirjastoon!")
        while True:
            komento = self.io.read("Anna komento (lisaa, poista, nayta, lopeta): ")
            if komento == "lisaa":
                teos = self.io.read("Anna teoksen nimi: ")
                vuosiluku = self.io.read("Anna vuosiluku: ")
                kirjoittaja = self.io.read("Anna kirjoittaja: ")
                self.viittaus_kirjasto.lisaa_viite(teos, vuosiluku, kirjoittaja)

                self.io.write("Viite lisätty.")
            elif komento == "poista":
                teos = self.io.read("Anna poistettavan teoksen nimi: ")
                if self.viittaus_kirjasto.poista_viite(teos):
                    self.io.write("Viite poistettu.")
                else:
                    self.io.write("Viitettä ei löytynyt.")
            elif komento == "nayta":
                for viite in self.viittaus_kirjasto.viitteet:
                    self.io.write(viite)
            elif komento == "lopeta":
                return
            else:
                self.io.write("Tuntematon komento.")
