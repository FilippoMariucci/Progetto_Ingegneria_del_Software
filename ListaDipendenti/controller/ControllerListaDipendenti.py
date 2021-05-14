from ListaDipendenti.model.ListaDipendenti import ListaDipendenti


class ControllerListaDipendenti():
    def __init__(self):
        super(ControllerListaDipendenti, self).__init__()
        self.model = ListaDipendenti()

    # Metodo che permette di aggiungere un dipendente
    def aggiungi_dipendente(self, dipendente):
        self.model.aggiungi_dipendente(dipendente)

    # Metodo che permette di ottenere la lista dei dipendenti
    def get_lista_dipendenti(self):
        return self.model.get_lista_dipendenti()

    # Funzione che ritorna il dipendente selezionato
    def get_dipendente_by_index(self, index):
        return self.model.get_dipendente_by_index(index)

    # Metodo che permette di rimuovere un dipendente attraverso il proprio codice identficativo
    def elimina_dipendente_by_id(self, id):
        self.model.rimuovi_dipendente_by_id(id)

    # Metodo che permette di salvare i dati
    def save_data(self):
        self.model.save_data()
