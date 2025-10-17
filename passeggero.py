class Passeggero:
    def __init__(self, codice_passeggero, nome, cognome):
        self.codice_passeggero = codice_passeggero
        self.nome = nome
        self.cognome = cognome

        self.cabina= None #non ha assegnata nessuna cabina

    def assegna_cabina(self, cabina):
        self.cabina = cabina