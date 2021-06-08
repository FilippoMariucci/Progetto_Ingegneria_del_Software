import json
import os
import pickle

from attrezzatura.model.Attrezzatura import Attrezzatura


class ListaAttrezzatura:

    # Costruttore con visualizzazione del file presente in ListaImpianti/data

    def __init__(self):
        super(ListaAttrezzatura, self).__init__()
        self.lista_attrezzatura = []
        if os.path.isfile('listaattrezzatura/data/lista_attrezzatura_salvata.pickle'):
            with open('listaattrezzatura/data/lista_attrezzatura_salvata.pickle', 'rb') as f:
                self.lista_attrezzatura = pickle.load(f)
        else:
            with open('listaattrezzatura/data/lista_attrezzatura_iniziale.json') as f:
                Lista_attrezzatura_inziale = json.load(f)
            for attrezzatura_iniziale in Lista_attrezzatura_inziale:
                self.aggiungi_attrezzatura(Attrezzatura(attrezzatura_iniziale["id"], attrezzatura_iniziale["nome"],
                                                        attrezzatura_iniziale["prezzo"], ))

    # Funzione per aggiungere un Impianti alla lista
    def aggiungi_attrezzatura(self, attrezzatura):
        self.lista_attrezzatura.append(attrezzatura)

    # Funzione per individuare un Impianti nella list attraverso un indicatore
    def get_attrezzatura_by_index(self, index):
        return self.lista_attrezzatura[index]

    # Funzione che restituisce la lista degli impianti
    def get_lista_attrezzature(self):
        return self.lista_attrezzatura

    # Funzione che salva la lista cosi come è
    def save_data(self):
        with open('listaattrezzatura/data/lista_attrezzatura_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_attrezzatura, handle, pickle.HIGHEST_PROTOCOL)
