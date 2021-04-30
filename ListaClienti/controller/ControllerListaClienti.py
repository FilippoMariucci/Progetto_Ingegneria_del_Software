from ListaClienti.model.ListaClienti import ListaClienti


class ControllorListaClienti():
    def __init__(self):
        super(ControllorListaClienti, self).__init__()
        self.model = ListaClienti()

# Metodo che permette di aggiungere un cliente
    def aggiungi_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente)

# Metodo che permette di ottenere la lista dei clienti
    def get_lista_dei_clienti(self):
        return self.model.get_lista_clienti()

# Metodo che permette di rimuovere un cliente attraverso il proprio codice identficativo
    def elimina_cliente_by_id(self, id):
        self.model.rimuovi_cliente_by_id(id)

# Metodo che permette di salvare i dati
    def save_data(self):
        self.model.save_data()