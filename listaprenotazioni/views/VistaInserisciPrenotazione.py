import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QSpacerItem, QSizePolicy, QPushButton, \
    QMessageBox

from prenotazione.model.Prenotazione import Prenotazione


class VistaInserisciPrenotazione(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazione, self).__init__(parent=None)
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("Data (dd/MM/yyyy)"))
        self.text_data = QLineEdit(self)
        v_layout.addWidget(self.text_data)

        self.combo_clienti = QComboBox()
        self.comboclienti_model = QStandardItemModel(self.combo_clienti)
        if os.path.isfile('ListaClienti/data/lista_clienti_salvata.pickle'):
            with open('ListaClienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti_salvata = pickle.load(f)
            self.lista_clienti_abbonati = [c for c in self.lista_clienti_salvata if c.get_abbonamento()]
            for cliente in self.lista_clienti_abbonati:
                item = QStandardItem()
                item.setText(cliente.nome + " " + cliente.cognome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboclienti_model.appendRow(item)
            self.combo_clienti.setModel(self.comboclienti_model)
        v_layout.addWidget(QLabel("Cliente"))
        v_layout.addWidget(self.combo_clienti)

        self.combo_impianti = QComboBox()
        self.comboimpianti_model = QStandardItemModel(self.combo_impianti)
        if os.path.isfile('ListaImpianti/data/Lista_Impianti_salvata.pickle'):
            with open('ListaImpianti/data/Lista_Impianti_salvata.pickle', 'rb') as f:
                self.lista_impianti_salvata = pickle.load(f)
            self.lista_impianti_disponibili = [s for s in self.lista_impianti_salvata if s.is_disponibile()]
            for impianto in self.lista_impianti_disponibili:
                item = QStandardItem()
                item.setText(impianto.nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboimpianti_model.appendRow(item)
            self.combo_impianti.setModel(self.comboimpianti_model)
        v_layout.addWidget(QLabel("impianto"))
        v_layout.addWidget(self.combo_impianti)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_prenotazione)
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
                Prenotazione((cliente.cognome + cliente.nome).lower(), cliente, impianto, data))
            impianto.prenota()
            with open('ListaImpianti/data/Lista_Impianti_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_impianti_salvata, f, pickle.HIGHEST_PROTOCOL)
            self.callback()
            self.close()