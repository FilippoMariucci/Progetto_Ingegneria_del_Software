from ListaImpianti.model.ListaImpianti import ListaImpianti


class ControllerListaImpianti():

    def __init__(self):
        super(ControllerListaImpianti, self).__init__()
        self.model = ListaImpianti()

    #Funzione che restituisce la lista completa degli impianti
    def get_lista_degli_impianti(self):
        return self.model.get_lista_impianti()

    #Funzione che restituisce l'Impianti attraverso un indice passatogli come riferimento
    def get_impianto_by_index(self, index):
        return self.model.get_impianto_by_index(index)

    #Funzione che salva i dati presenti nella lista
    def save_data(self):
        self.model.save_data()