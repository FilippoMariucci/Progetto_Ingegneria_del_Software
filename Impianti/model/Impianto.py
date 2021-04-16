class Impianto():

   # Costruttore con le informazioni di un impianto
    def __init__(self, id, nome, tipo, posizione, prezzo) :
        super(Impianto, self).__init__()
        self.id = id
        self.nome = nome

        self.tipo = tipo
        self.posizione = posizione
        self.prezzo = prezzo
        self.disponibilità = True

    # Funzione che ci indica se un impianto è disponibile o no
    def is_disponibile(self):
        return self.disponibilità
    # Funzione che rende l'impiato prenotato non più disponibile
    def prenota(self):
        self.disponibilità = False