import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QSpacerItem, QSizePolicy, QPushButton, \
    QMessageBox

from listaprenotazioni.views.VistaInserisciAttrezzatura import VistaInserisciAttrezzatura
from prenotazione.model.Prenotazione import Prenotazione


class VistaScegliPrenotazione(QWidget):


    def __init__(self, controller, callback):
        super(VistaScegliPrenotazione, self).__init__(parent=None)
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()

        self.combo_prenotazioni = QComboBox()
        self.comboprenotazioni_model = QStandardItemModel(self.combo_prenotazioni)
        if os.path.isfile('listaprenotazioni/data/lista_prenotazioni_salvata.pickle'):
            with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'rb') as f:
                self.lista_prenotazioni_salvata = pickle.load(f)
            self.lista_prenotazioni_disponibili = [s for s in self.lista_prenotazioni_salvata]
            for prenotazione in self.lista_prenotazioni_salvata:
                item = QStandardItem()
                item.setText(prenotazione.cliente.cognome + " " + prenotazione.cliente.nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboprenotazioni_model.appendRow(item)
            self.combo_prenotazioni.setModel(self.comboprenotazioni_model)
        v_layout.addWidget(QLabel("Prenotazione"))
        v_layout.addWidget(self.combo_prenotazioni)




        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect()
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuova Prenotazione')

    def add_prenotazione(self):
        data = self.text_data.text()
        cliente = self.lista_clienti_abbonati[self.combo_clienti.currentIndex()]
        impianto = self.lista_impianti_disponibili[self.combo_impianti.currentIndex()]

        if data == "" or not cliente or not impianto:
            QMessageBox(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok,
                        QMessageBox.Ok)
        else:
            self.controller.aggiungi_prenotazione(
                Prenotazione((cliente.cognome + cliente.nome).lower(), cliente, impianto, data
                             ))
            impianto.prenota()
            with open('ListaImpianti/data/Lista_Impianti_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_impianti_salvata, f, pickle.HIGHEST_PROTOCOL)
            self.callback()
            self.close()

