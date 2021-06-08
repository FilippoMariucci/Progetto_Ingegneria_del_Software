import time


class Abbonamento:
    def __init__(self, scadenza):
        self.scadenza = scadenza

    # Funzione che indentifica se l'abbonamento è scaduto o meno.
    # Il timestamp è un'intero che rappresenta i secondi passati da un particolare giorno
    # ( quello che si usa di più è lo unit timestamp che rappresenta il umero di secondi passati dal 1 Gennaio 1970,)
    def is_scaduto(self):
        timestamp = int(time.time())
        return timestamp > self.scadenza
