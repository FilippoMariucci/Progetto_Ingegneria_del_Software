class ControllorImpianto():
    def __init__(self, servizio):
        self.model = servizio

    #Restituisce il nome dell'impianto
    def get_nome_impianto(self):
        return self.model.nome

    # Restituisce il tipo dell'impianto
    def get_tipo_impianto(self):
        return self.model.tipo

    # Restituisce la posizione dell'impianto
    def get_posizione_impianto(self):
        return self.model.posizione

    # Inseriamo un place-holder (le due parentesi graffe dentro gli apici);
    # quando richiameremo il metodo al posto delle graffe verrà inserito il prezzo dell'impianto
    def get_prezzo_impianto(self):
        return "{}".format(self.model.prezzo)

    # Richiamando il metodo il programma restiruirà "Disponibile" se l'impianto è libero;
    # altrienti restituirà "Non disponibile"
    def get_impianto_disponibile(self):
        if self.model.is_disponibile():
            return "Disponibile"
        else:
            return "Non Disponibile"