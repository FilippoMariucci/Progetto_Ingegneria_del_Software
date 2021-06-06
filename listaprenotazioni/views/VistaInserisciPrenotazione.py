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
        v_layout.addWidget(QLabel("Impianto"))
        v_layout.addWidget(self.combo_impianti)

        n = [0]
        for i in range(1, 11):
            n.append(i)

        v_layout.addWidget(QLabel("Pallone"))
        self.combo_quantita_1 = QComboBox()
        self.comboquantita_1_model = QStandardItemModel(self.combo_quantita_1)
        for i in n:
            item = QStandardItem()
            item.setText(str(n[i]))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.comboquantita_1_model.appendRow(item)
        self.combo_quantita_1.setModel(self.comboquantita_1_model)
        v_layout.addWidget(self.combo_quantita_1)

        v_layout.addWidget(QLabel("Casacca"))
        self.combo_quantita_2 = QComboBox()
        self.comboquantita_2_model = QStandardItemModel(self.combo_quantita_2)
        for i in n:
            item = QStandardItem()
            item.setText(str(n[i]))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.comboquantita_2_model.appendRow(item)
        self.combo_quantita_2.setModel(self.comboquantita_2_model)
        v_layout.addWidget(self.combo_quantita_2)

        v_layout.addWidget(QLabel("Occhialini"))
        self.combo_quantita_3 = QComboBox()
        self.comboquantita_3_model = QStandardItemModel(self.combo_quantita_3)
        for i in n:
            item = QStandardItem()
            item.setText(str(n[i]))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.comboquantita_3_model.appendRow(item)
        self.combo_quantita_3.setModel(self.comboquantita_3_model)
        v_layout.addWidget(self.combo_quantita_3)

        v_layout.addWidget(QLabel("Asciugamano"))
        self.combo_quantita_4 = QComboBox()
        self.comboquantita_4_model = QStandardItemModel(self.combo_quantita_4)
        for i in n:
            item = QStandardItem()
            item.setText(str(n[i]))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.comboquantita_4_model.appendRow(item)
        self.combo_quantita_4.setModel(self.comboquantita_4_model)
        v_layout.addWidget(self.combo_quantita_4)

        v_layout.addWidget(QLabel("Cuffia"))
        self.combo_quantita_5 = QComboBox()
        self.comboquantita_5_model = QStandardItemModel(self.combo_quantita_5)
        for i in n:
            item = QStandardItem()
            item.setText(str(n[i]))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.comboquantita_5_model.appendRow(item)
        self.combo_quantita_5.setModel(self.comboquantita_5_model)
        v_layout.addWidget(self.combo_quantita_5)

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
        a = [self.combo_quantita_1.currentIndex(), self.combo_quantita_2.currentIndex(),
             self.combo_quantita_3.currentIndex(), self.combo_quantita_4.currentIndex(),
             self.combo_quantita_5.currentIndex()]
        att = {}
        i = 0
        if os.path.isfile('listaattrezzatura/data/lista_attrezzatura_salvata.pickle'):
            with open('listaattrezzatura/data/lista_attrezzatura_salvata.pickle', 'rb') as f:
                self.lista_attrezzatura_salvata = pickle.load(f)
            self.lista_attrezzatura_disponibile = [s for s in self.lista_attrezzatura_salvata if s.is_disponibile()]
            for attrezzatura in self.lista_attrezzatura_disponibile:
                att[attrezzatura.nome] = a[i]
                i += 1

        totale = float(impianto.prezzo)

        if data == "" or not cliente or not impianto:
            QMessageBox(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok,
                        QMessageBox.Ok)
        else:
            self.controller.aggiungi_prenotazione(
                Prenotazione((cliente.cognome + cliente.nome).lower(), cliente, impianto, data, att, totale))
            impianto.prenota()
            with open('ListaImpianti/data/Lista_Impianti_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_impianti_salvata, f, pickle.HIGHEST_PROTOCOL)
            self.callback()
            self.close()


