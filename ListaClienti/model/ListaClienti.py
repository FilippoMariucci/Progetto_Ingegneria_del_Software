import os
import pickle


class ListaClienti():
    def __init__(self):
        super(ListaClienti, self).__init__()
        self.lista_clienti = []
        if os.path.isfile('ListaClienti/data/lista_clienti_salvata.pickle'):
            with open('ListaClienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)
    #Metodo che permette di aggiungere un cliente nell'apposita lista
    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)

    # Metodo che permette di rimuovere un cliente dall'apposita lista
    def rimuovi_cliente_by_id(self, id):
        def is_selected_cliente(cliente):
            if cliente.id == id:
                return True
            return False
        self.lista_clienti.remove(list(filter(is_selected_cliente, self.lista_clienti))[0])

    # Metodo che permette di individuare un cliente nell'apposita lista attraverso un indicatore
    def get_cliente_by_index(self, index):
        return self.lista_clienti[index]

    # Metodo che permette di ottenere la lista clienti
    def get_lista_clienti(self):
        return self.lista_clienti

    # Metodo che permette di salvare la lsita clienti in un file .pickle con il protocollo
    def save_data(self):
        with open('Listaclienti/data/lista_clienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)