import pickle
import os.path

class ListaImpianti():

#Costruttore con visualizzazione del file presente in ListaImpianti/Data

    def __init__(self):
        super(ListaImpianti, self).__init__()
        self.lista_impianti = []
        if os.path.isfile('ListaImpianti/Data/Lista_Impianti_salvata.pickle'):
            with open('ListaImpianti/Data/Lista_Impianti_salvata.pickle','rb') as f:
                self.lista_impianti= pickle.load(f)

    # Funzione per aggiungere un impianto alla lista
    def aggiungi_impianto(self, impianto):
        self.lista_impianti.append(impianto)

    # Funzione per individuare un impianto nella list attraverso un indicatore
    def get_impianto_by_index(self, index):
        return self.lista_impianti[index]

    # Funzione che restituisce la lista degli impianti
    def get_lista_impianti(self):
        return self.lista_impianti

    # Funzione che salva la lista cosi come è
    def save_data(self):
        with open('ListaImpianti/Data/Lista_Impianti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_impianti, handle, pickle.HIGHEST_PROTOCOL)