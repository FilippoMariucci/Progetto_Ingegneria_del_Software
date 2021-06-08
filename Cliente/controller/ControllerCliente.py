class ControllerCliente:
    def __init__(self, cliente):
        self.model = cliente

    # Funzione che restituisce l'id del cliente
    def get_id_cliente(self):
        return self.model.id

    # Funzione che restituisce il nome del cliente
    def get_nome_cliente(self):
        return self.model.nome

    # Funzione che restituisce il cognome del cliente
    def get_cognome_cliente(self):
        return self.model.cognome

    # Funzione che restituisce il codice fiscale del cliente
    def get_codice_fiscale_cliente(self):
        return self.model.codice_fiscale

    # Funzione che restituisce il numero di telefono del cliente
    def get_telefono_cliente(self):
        return self.model.telefono

    # Funzione che restituisce la data di nascita del cliente
    def get_data_di_nascita_cliente(self):
        return self.model.data_di_nascita

    # Funzione che restituisce l'abbonamento del cliente
    def get_abbonamento_cliente(self):
        return self.model.abbonamento

    # Funzione che aggiunge un nuovo abbonamento al cliente selezionato
    def aggiungi_nuovo_abbonamento_cliente(self, abbonamento):
        self.model.add_abbonamento(abbonamento)
