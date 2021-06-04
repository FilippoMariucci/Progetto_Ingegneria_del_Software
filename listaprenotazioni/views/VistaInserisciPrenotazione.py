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

        self.num = [0]
        for i in range(1, 20):
            self.num.append(i)

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
        v_layout.addWidget(QLabel("Impianto"))
        v_layout.addWidget(self.combo_impianti)

        self.combo_num = QComboBox()
        self.combo_num_model = QStandardItemModel(self.combo_num)
        for i in self.num:
            n = i
            item = QStandardItem()
            item.setText(str(n))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.combo_num_model.appendRow(item)
        self.combo_num.setModel(self.combo_num_model)
        v_layout.addWidget(QLabel("Numero attrezzature"))
        v_layout.addWidget(self.combo_num)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_attrezzatura = QPushButton("Inserisci attrezzatura/e")
        btn_attrezzatura.clicked.connect(self.add_attrezzatura)
        v_layout.addWidget(btn_attrezzatura)
        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_prenotazione)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuova Prenotazione')

    def add_prenotazione(self):
        data = self.text_data.text()
        cliente = self.lista_clienti_abbonati[self.combo_clienti.currentIndex()]
        impianto = self.lista_impianti_disponibili[self.combo_impianti.currentIndex()]
        attrezzatura = self.lista_attrezzatura_disponibile[self.combo_attrezzature.currentIndex()]
        num_att = self.num[self.combo_num.currentIndex()]

        if data == "" or not cliente or not impianto:
            QMessageBox(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok,
                        QMessageBox.Ok)
        else:
            self.controller.aggiungi_prenotazione(
                Prenotazione((cliente.cognome + cliente.nome).lower(), cliente, impianto, data, attrezzatura,
                             num_att))
            impianto.prenota()
            with open('ListaImpianti/data/Lista_Impianti_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_impianti_salvata, f, pickle.HIGHEST_PROTOCOL)
            self.callback()
            self.close()

    def add_attrezzatura(self):
        num_att = self.num[self.combo_num.currentIndex()]

        if num_att != 0:

            a_layout = QVBoxLayout()
            i = 0
            while i < num_att:

                self.combo_attrezzature = QComboBox()
                self.comboattrezzature_model = QStandardItemModel(self.combo_attrezzature)
                if os.path.isfile('listaattrezzatura/data/lista_attrezzatura_salvata.pickle'):
                    with open('listaattrezzatura/data/lista_attrezzatura_salvata.pickle', 'rb') as f:
                        self.lista_attrezzatura_salvata = pickle.load(f)
                    self.lista_attrezzatura_disponibile = [r for r in self.lista_attrezzatura_salvata if
                                                           r.is_disponibile()]
                    for attrezzatura in self.lista_attrezzatura_disponibile:
                        item = QStandardItem()
                        item.setText(attrezzatura.nome)
                        item.setEditable(False)
                        font = item.font()
                        font.setPointSize(18)
                        item.setFont(font)
                        self.comboattrezzature_model.appendRow(item)
                    self.combo_attrezzature.setModel(self.comboattrezzature_model)
                    a_layout.addWidget(QLabel("Aggiungi attrezzatura"))
                    a_layout.addWidget(self.combo_attrezzature)
                i += 1

            a_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

            btn_ok = QPushButton("OK")
            btn_ok.clicked.connect(self.add_prenotazione)
            a_layout.addWidget(btn_ok)
            self.setLayout(a_layout)
            self.setWindowTitle('Nuova Prenotazione')
        else:
            self.add_prenotazione()