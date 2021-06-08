class Attrezzatura:

    # Costruttore con le informazioni di un Impianti
    def __init__(self, id, nome, prezzo):
        super(Attrezzatura, self).__init__()
        self.id = id
        self.nome = nome
        self.prezzo = prezzo
        self.disponibilita = True

    # Funzione che ci indica se un Impianti è disponibile o no
    def is_disponibile(self):
        return self.disponibilita

    # Funzione che rende l'impiato prenotato non più disponibile
    def prenota(self):
        self.disponibilita = False
