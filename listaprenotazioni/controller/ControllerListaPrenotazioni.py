from listaprenotazioni.model.ListaPrenotazioni import ListaPrenotazioni


class ControlloreListaPrenotazioni():
    def __init__(self):
        self.model = ListaPrenotazioni()

    # Funzione che permette di aggiungere una prenotazione
    def aggiungi_prenotazione(self, prenotazione):
        self.model.aggiungi_prenotazione(prenotazione)

    # Funzione che permette di ottenere la lista delle prenotazioni
    def get_lista_delle_prenotazioni(self):
        return self.model.get_lista_prenotazioni()

    # Funzione che permette di visualizzare a schermo la prenotazione selezionata
    def get_prenotazione_by_index(self, index):
        return self.model.get_prenotazione_by_index(index)

    # Funzione che permette di rimuovere una prenotazione attraverso il rispettivo id
    def elimina_prenotazione_by_id(self, id):
        self.model.rimuovi_prenotazione_by_id(id)

    # Funzione che salva i dati
    def save_data(self):
        self.model.save_data()