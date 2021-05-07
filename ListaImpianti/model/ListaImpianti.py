import json
import pickle
import os.path

from Impianti.model.Impianto import Impianto


class ListaImpianti():

#Costruttore con visualizzazione del file presente in ListaImpianti/data

    def __init__(self):
        super(ListaImpianti, self).__init__()
        self.lista_impianti = []
        if os.path.isfile('ListaImpianti/data/Lista_Impianti_salvata.pickle'):
            with open('ListaImpianti/data/Lista_Impianti_salvata.pickle','rb') as f:
                self.lista_impianti= pickle.load(f)
        else:
            with open('ListaImpianti/data/Lista_impianti_iniziale.json') as f:
                Lista_impianti_inziale = json.load(f)
            for impianto_iniziale in  Lista_impianti_inziale:
                self.aggiungi_impianto(Impianto(impianto_iniziale["id"], impianto_iniziale["nome"],
                                                impianto_iniziale["tipo"],impianto_iniziale["posizione"],
                                                impianto_iniziale["prezzo"],))

    # Funzione per aggiungere un Impianti alla lista
    def aggiungi_impianto(self,impianto):
        self.lista_impianti.append(impianto)

    # Funzione per individuare un Impianti nella list attraverso un indicatore
    def get_impianto_by_index(self, index):
        return self.lista_impianti[index]

    # Funzione che restituisce la lista degli impianti
    def get_lista_impianti(self):
        return self.lista_impianti

    # Funzione che salva la lista cosi come è
    def save_data(self):
        with open('ListaImpianti/data/Lista_Impianti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_impianti, handle, pickle.HIGHEST_PROTOCOL)