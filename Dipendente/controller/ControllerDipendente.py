class ControllerDipendente:
    def __init__(self, dipendente):
        self.model = dipendente

    # Funzione che ritorna l'id del dipendente
    def get_id_dipendente(self):
        return self.model.id

    # Funzione che ritorna il nome del dipendente
    def get_nome_dipendente(self):
        return self.model.nome

    # Funzione che ritorna il cognome del dipendente
    def get_cognome_dipendente(self):
        return self.model.cognome

    # Funzione che ritorna la data di nascita del dipendente

    def get_data_di_nascita_dipendente(self):
        return self.model.data_di_nascita

    # Funzione che ritorna il luogo di nascita del dipendente
    def get_luogo_di_nascita_dipendente(self):
        return self.model.luogo_di_nascita

    # Funzione che ritorna il codice fiscle del dipendente
    def get_codice_fiscale_dipendente(self):
        return self.model.codice_fiscale

    # Funzione che ritorna il numero di telefono  del dipendente
    def get_telefono_dipendente(self):
        return self.model.telefono

    # Funzione che ritorna l'email del dipendente
    def get_email_dipendente(self):
        return self.model.email

    # Funzione che ritorna la licenza del dipendente
    def get_licenza_dipendente(self):
        return self.model.licenza
