from ListaClienti.model.ListaClienti import ListaClienti


class ControllerListaClienti:
    def __init__(self):
        super(ControllerListaClienti, self).__init__()
        self.model = ListaClienti()

# Metodo che permette di aggiungere un Cliente
    def aggiungi_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente)

# Metodo che permette di ottenere la lista dei clienti
    def get_lista_dei_clienti(self):
        return self.model.get_lista_clienti()

    # Funzione che ritorna il cliente selezionato
    def get_cliente_by_index(self, index):
        return self.model.get_cliente_by_index(index)

    # Metodo che permette di rimuovere un Cliente attraverso il proprio codice identficativo
    def elimina_cliente_by_id(self, id):
        self.model.rimuovi_cliente_by_id(id)

# Metodo che permette di salvare i dati
    def save_data(self):
        self.model.save_data()
