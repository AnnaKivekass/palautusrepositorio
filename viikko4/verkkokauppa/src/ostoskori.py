class Ostoskori:
    def __init__(self):
        self._tuotteet = []

    def lisaa(self, tuote):
        self._tuotteet.append(tuote)

    def poista(self, tuote):
        for t in self._tuotteet:
            if t.id == tuote.id:
                self._tuotteet.remove(t)
                break

    def hinta(self):
        return sum(t.hinta for t in self._tuotteet)
