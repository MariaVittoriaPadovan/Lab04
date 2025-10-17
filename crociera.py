import csv

from cabina import Cabina, CabinaAnimale, CabinaDeluxe

from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome=nome

        self.cabine=[]
        self.passeggeri=[]

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""

        try:
            with open(file_path, 'r', encoding='utf-8') as f:

                reader = csv.reader(f)

                righe = [riga for riga in reader]

                for riga in righe:
                    codice = riga[0]

                    if codice.starswith("P"):
                        codice_passeggero = riga[0]
                        nome = riga[1]
                        cognome = riga[2]

                        passeggero= Passeggero(codice_passeggero, nome, cognome)
                        self.passeggeri.append(passeggero)

                    else:
                        numLetti=int(riga[1])
                        ponte=int(riga[2])
                        prezzo_base=int(riga[3])

                        if len(riga)==4:
                            cabina = Cabina(codice, numLetti, ponte, prezzo_base)
                            self.cabine.append(cabina)

                        else:
                            valore=riga[4]
                            if valore.isdigit():
                                numAnimali = int(riga[4])
                                cabinaAnimale = CabinaAnimale(codice, numLetti, ponte, prezzo_base, numAnimali)
                                self.cabine.append(cabinaAnimale)

                            if valore.isalpha():
                                tipo = riga[4]
                                cabinaDeluxe = CabinaDeluxe(codice, numLetti, ponte, prezzo_base, tipo)
                                self.cabine.append(cabinaDeluxe)

                return self.cabine, self.passeggeri

        except FileNotFoundError:
            print(f'File {file_path} non trovato.')
            return None


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""

        for c in self.cabine:
            if codice_cabina == c.codice:
                cabina=c
                break
        for p in self.passeggeri:
            if codice_passeggero == p.codice:
                passeggero=p
                break

        if cabina is None:
            raise Exception('Cabina non trovata')
        if passeggero is None:
            raise Exception('Passeggero non trovato')
        if not cabina.disponibile:
            raise Exception('Cabina non disponibile')
        if passeggero.cabina is not None:
            raise Exception('Passeggero ha già la cabina')

        cabina.assegna_passeggero(passeggero)
        passeggero.assegna_cabina(cabina)


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

