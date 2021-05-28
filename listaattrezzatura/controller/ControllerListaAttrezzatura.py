from listaattrezzatura.model.ListaAttrezzatura import ListaAttrezzatura


class ControllerListaAttrezzatura():

    def __init__(self):
        super(ControllerListaAttrezzatura, self).__init__()
        self.model = ListaAttrezzatura()

    #Funzione che restituisce la lista completa degli impianti
    def get_lista_delle_attrezzature(self):
        return self.model.get_lista_attrezzature()

    #Funzione che restituisce l'Impianti attraverso un indice passatogli come riferimento
    def get_attrezzatura_by_index(self, index):
        return self.model.get_attrezzatura_by_index(index)

    #Funzione che salva i dati presenti nella lista
    def save_data(self):
        self.model.save_data()