import json


class JsonHandler:
    def __init__(self):
        pass

    def tallenna(self, viitteet):
        data = []
        for viite in viitteet:
            viite_data = {
                "teos": viite.teos,
                "vuosiluku": viite.vuosiluku,
                "kirjoittaja": viite.kirjoittaja
            }
            data.append(viite_data)

        with open("data/viitteet.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

    def lataa(self):
        try:
            with open("data/viitteet.json", 'r', encoding="utf-8") as f:
                viite_data = json.load(f)
                return viite_data
        except FileNotFoundError:
            return []