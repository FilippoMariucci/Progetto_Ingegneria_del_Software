class Cliente():
    def __init__(self, id, nome, cognome, codice_fiscale,indirizzo, email, telefono, eta):
        super(Cliente, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.indirizzo= indirizzo
        self.emil=email
        self.telefono = telefono
        self.eta= eta
        self.abbonamento = None

    #Metodo per aggiunngere un abbonamento ad un cliente
    def add_abbonamento(self, abbonamento):
        self.abbonamento = abbonamento
        
    #Metodo che restituisce i dati di un abbonamento
    def get_abbonamento(self):
        if self.abbonamento.is_scaduto():
            self.abbonamento = None
            return None
        else:
            return self.abbonamento