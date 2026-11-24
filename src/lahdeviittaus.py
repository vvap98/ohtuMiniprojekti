
class Lahdeviittaus:
    def __init__(self, teos, vuosiluku, kirjoittaja):
        self.teos = teos
        self.vuosiluku = vuosiluku
        self.kirjoittaja = kirjoittaja

    def __str__(self):
        return f"Teos: {self.teos}, Vuosi: {self.vuosiluku}, Kirjoittaja: {self.kirjoittaja}"