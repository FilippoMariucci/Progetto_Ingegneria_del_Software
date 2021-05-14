class Dipendente():
    def __init__(self, id, nome, cognome, data_di_nascita, luogo_di_nascita, codice_fiscale, telefono, email, licenza):
        super(Dipendente, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.data_di_nascita = data_di_nascita
        self.luogo_di_nascita = luogo_di_nascita
        self.codice_fiscale = codice_fiscale
        self.telefono = telefono
        self.email = email
        self.licenza = licenza
