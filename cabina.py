class Cabina:
    def __init__(self, codice, numLetti, ponte, prezzo):
        self.codice = codice
        self.numLetti = numLetti
        self.ponte = ponte
        self.prezzo = prezzo


class CabinaAnimale(Cabina):
    def __init__(self, codice, numLetti, ponte, prezzo, numAnimali):
        super().__init__(codice, numLetti, ponte, prezzo)

        self.numAnimali = numAnimali


class CabinaDeluxe(Cabina):
    def __init__(self, codice, numLetti, ponte, prezzo, tipo):
        super().__init__(codice, numLetti, ponte, prezzo)

        self.tipo = tipo