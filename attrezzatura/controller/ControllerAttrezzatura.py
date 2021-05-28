class ControllerAttrezzatura():
    def __init__(self, attrezzatura):
        self.model = attrezzatura

    #Restituisce il nome dell'Impianti
    def get_nome_attrezzatura(self):
        return self.model.nome


    # Inseriamo un place-holder (le due parentesi graffe dentro gli apici);
    # quando richiameremo il metodo al posto delle graffe verrà inserito il prezzo dell'Impianti
    def get_prezzo_attrezzatura(self):
        return "{}".format(self.model.prezzo)

    # Richiamando il metodo il programma restiruirà "Disponibile" se l'Impianti è libero;
    # altrienti restituirà "Non disponibile"
    def get_attrezzatura_disponibile(self):
        if self.model.is_disponibile():
            return "Disponibile"
        else:
            return "Non Disponibile"