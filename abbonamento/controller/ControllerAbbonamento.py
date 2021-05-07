# Libreria che gestisce le date
from datetime import datetime


class ControllerAbbonamento():
    def __init__(self, abbonamento):
        self.model = abbonamento

    # Funzione che ci ritorna se il model è nullo o meno;
    # se il cliente non è abbonato gli passo NONE ovvere un valore nullo come abbonamento
    def is_abbonato(self):
        return self.model is not None

    # Funzione che ci permette di ottenere la scadenza come stringa
    def get_scadenza_string(self):
        print("TIMESTAMP: {}".format(self.model.scadenza))

        # Ci crea una data dal timestamp
        scadenza_data = datetime.fromtimestamp(self.model.scadenza)
        return "Scadenza {}/{}/{}".format(scadenza_data.day, scadenza_data.month, scadenza_data.year)
