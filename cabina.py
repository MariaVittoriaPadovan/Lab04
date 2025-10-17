class Cabina:
    def __init__(self, codice, numLetti, ponte, prezzo_base):
        self.codice = codice
        self.numLetti = numLetti
        self.ponte = ponte
        self.prezzo_base = prezzo_base

        self.disponibile= True #inizializzo la cabina a libera per poi gestire le prenotazioni
        self.passeggero= None #all'inizio non ho nessun passeggero nella cabina


    def prezzo_finale(self):
        return self.prezzo_base

    def assegna_passeggero(self, passeggero):
        self.disponibile = False
        self.passeggero = passeggero


class CabinaAnimale(Cabina):
    def __init__(self, codice, numLetti, ponte, prezzo_base, numAnimali):
        super().__init__(codice, numLetti, ponte, prezzo_base)

        self.numAnimali = numAnimali

    def prezzo_finale(self):

        prezzo_finale= self.prezzo_base * (1 + 0.10 * self.numAnimali)
        return prezzo_finale


class CabinaDeluxe(Cabina):
    def __init__(self, codice, numLetti, ponte, prezzo_base, tipo):
        super().__init__(codice, numLetti, ponte, prezzo_base)

        self.tipo = tipo

    def prezzo_finale(self):
        prezzo_finale = self.prezzo_base * 1.20
        return prezzo_finale