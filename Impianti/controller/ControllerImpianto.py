class ControllorImpianto():
    def __init__(self, servizio):
        self.model = servizio

    #Restituisce il nome dell'Impianti
    def get_nome_impianto(self):
        return self.model.nome

    # Restituisce il tipo dell'Impianti
    def get_tipo_impianto(self):
        return self.model.tipo

    # Restituisce la posizione dell'Impianti
    def get_posizione_impianto(self):
        return self.model.posizione

    # Inseriamo un place-holder (le due parentesi graffe dentro gli apici);
    # quando richiameremo il metodo al posto delle graffe verrà inserito il prezzo dell'Impianti
    def get_prezzo_impianto(self):
        return "{}".format(self.model.prezzo)

    # Richiamando il metodo il programma restiruirà "Disponibile" se l'Impianti è libero;
    # altrienti restituirà "Non disponibile"
    def get_impianto_disponibile(self):
        if self.model.is_disponibile():
            return "Disponibile"
        else:
            return "Non Disponibile"