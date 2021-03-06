class ControllerPrenotazione:
    def __init__(self, prenotazione):
        self.model = prenotazione

    def get_id_prenotazione(self):
        print(self.model.id)
        return self.model.id

    def get_cliente_prenotazione(self):
        return self.model.cliente

    def get_impianto_prenotazione(self):
        return self.model.impianto

    def get_attrezzatura_prenotazione(self):
        return self.model.attrezzatura

    def get_data_prenotazione(self):
        return self.model.data

    def get_orario_prenotazione(self):
        return self.model.orario

    def get_numero_ore_prenotazione(self):
        return self.model.num_ore

    def get_totale_prenotazione(self):
        return self.model.totale
