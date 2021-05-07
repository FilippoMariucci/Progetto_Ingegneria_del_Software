import os
import pickle


class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.lista_dipendenti = []
        if os.path.isfile('ListaDipendenti/data/lista_dipendenti_salvata.pickle'):
            with open('ListaDipendenti/data/lista_dipendenti_salvata.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)

    # Funzione che permette di aggiungere un dipendente
    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

    # Funzione che permette di rimuovere un dipendente attraverso il suo id
    def rimuovi_dipendente_by_id(self, id):
        def is_selected_dipendente(dipendente):
            if dipendente.id == id:
                return True
            return False
        self.lista_dipendenti.remove(list(filter(is_selected_dipendente, self.lista_dipendenti))[0])

    # Funzione che permette di selezionare un dipendente in base alla sua posizione nella lista
    def get_dipendente_by_index(self, index):
        return self.lista_dipendenti[index]

    # Funzione che ritorna la lista completa dei dipendenti
    def get_lista_dipendenti(self):
        return self.lista_dipendenti

    # Funzione che salva la lista dei dipendenti
    def save_data(self):
        with open('ListaDipendenti/data/lista_dipendenti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_dipendenti, handle, pickle.HIGHEST_PROTOCOL)