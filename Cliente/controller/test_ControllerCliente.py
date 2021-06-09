from unittest import TestCase

from Cliente.model.Cliente import Cliente
from abbonamento.model.Abbonamento import Abbonamento


class TestControllerCliente(TestCase):
    def test_aggiungi_nuovo_abbonamento_cliente(self):
        self.cliente = Cliente(id="test", nome="test", cognome="test", codice_fiscale="MRCFPP00D06A271U", telefono="1234569870", data_di_nascita="06/04/2000")
        self.assertIsNone(self.cliente.abbonamento)
        self.cliente.add_abbonamento(Abbonamento(scadenza="30/12/2022"))
        self.assertIsNotNone(self.cliente.abbonamento)
