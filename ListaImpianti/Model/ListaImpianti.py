import pickle
import os.path

class ListaImpianti():

    def __init__(self):
        super(ListaImpianti, self).__init__()
        self.lista_impianti = []

    # Funzione per aggiungere un impianto alla lista
    def aggiungi_impianto(self, impianto):
        self.lista_impianti.append(impianto)

    # Funzione per individuare un impianto nella list attraverso un indicatore
    def get_impianto_by_index(self, index):
        return self.lista_impianti[index]

    # Funzione che restituisce la lista degli impianti
    def get_lista_impianti(self):
        return self.lista_impianti