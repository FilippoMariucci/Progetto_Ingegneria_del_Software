import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QLabel, QSpacerItem, QSizePolicy, QPushButton, QLineEdit


class VistaInserisciAttrezzatura(QWidget):

    def __init__(self, controller, callback):
        super(VistaInserisciAttrezzatura, self).__init__(parent=None)
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()

        self.combo_attrezzatura_1 = QComboBox()
        self.comboattrezzatura1_model = QStandardItemModel(self.combo_attrezzatura_1)
        if os.path.isfile('listaattrezzatura/data/lista_attrezzatura_salvata.pickle'):
            with open('listaattrezzatura/data/lista_attrezzatura_salvata.pickle', 'rb') as f:
                self.lista_attrezzatura_salvata_1 = pickle.load(f)
            self.lista_attrezzatura_disponibile_1 = [s for s in self.lista_attrezzatura_salvata_1 if s.is_disponibile()]
            for attrezzatura in self.lista_attrezzatura_disponibile_1:
                item = QStandardItem()
                item.setText(attrezzatura.nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboattrezzatura1_model.appendRow(item)
            self.combo_attrezzatura_1.setModel(self.comboattrezzatura1_model)
        v_layout.addWidget(QLabel("Attrezzatura"))
        v_layout.addWidget(self.combo_attrezzatura_1)

        v_layout.addWidget(QLabel("Quantità"))
        self.quantita_1 = QLineEdit(self)
        v_layout.addWidget(self.quantita_1)

        self.combo_attrezzatura_2 = QComboBox()
        self.comboattrezzatura2_model = QStandardItemModel(self.combo_attrezzatura_2)
        if os.path.isfile('listaattrezzatura/data/lista_attrezzatura_salvata.pickle'):
            with open('listaattrezzatura/data/lista_attrezzatura_salvata.pickle', 'rb') as f:
                self.lista_attrezzatura_salvata_2 = pickle.load(f)
            self.lista_attrezzatura_disponibile_2 = [s for s in self.lista_attrezzatura_salvata_2 if s.is_disponibile()]
            for attrezzatura in self.lista_attrezzatura_disponibile_2:
                item = QStandardItem()
                item.setText(attrezzatura.nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboattrezzatura2_model.appendRow(item)
            self.combo_attrezzatura_2.setModel(self.comboattrezzatura2_model)
        v_layout.addWidget(QLabel("Attrezzatura"))
        v_layout.addWidget(self.combo_attrezzatura_2)

        v_layout.addWidget(QLabel("Quantità"))
        self.quantita_2 = QLineEdit(self)
        v_layout.addWidget(self.quantita_2)

        self.combo_attrezzatura_3 = QComboBox()
        self.comboattrezzatura3_model = QStandardItemModel(self.combo_attrezzatura_3)
        if os.path.isfile('listaattrezzatura/data/lista_attrezzatura_salvata.pickle'):
            with open('listaattrezzatura/data/lista_attrezzatura_salvata.pickle', 'rb') as f:
                self.lista_attrezzatura_salvata_3 = pickle.load(f)
            self.lista_attrezzatura_disponibile_3 = [s for s in self.lista_attrezzatura_salvata_3 if s.is_disponibile()]
            for attrezzatura in self.lista_attrezzatura_disponibile_3:
                item = QStandardItem()
                item.setText(attrezzatura.nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboattrezzatura3_model.appendRow(item)
            self.combo_attrezzatura_3.setModel(self.comboattrezzatura3_model)
        v_layout.addWidget(QLabel("Attrezzatura"))
        v_layout.addWidget(self.combo_attrezzatura_3)

        v_layout.addWidget(QLabel("Quantità"))
        self.quantita_3 = QLineEdit(self)
        v_layout.addWidget(self.quantita_3)

        self.combo_attrezzatura_4 = QComboBox()
        self.comboattrezzatura4_model = QStandardItemModel(self.combo_attrezzatura_4)
        if os.path.isfile('listaattrezzatura/data/lista_attrezzatura_salvata.pickle'):
            with open('listaattrezzatura/data/lista_attrezzatura_salvata.pickle', 'rb') as f:
                self.lista_attrezzatura_salvata_4 = pickle.load(f)
            self.lista_attrezzatura_disponibile_4 = [s for s in self.lista_attrezzatura_salvata_4 if s.is_disponibile()]
            for attrezzatura in self.lista_attrezzatura_disponibile_4:
                item = QStandardItem()
                item.setText(attrezzatura.nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboattrezzatura4_model.appendRow(item)
            self.combo_attrezzatura_4.setModel(self.comboattrezzatura4_model)
        v_layout.addWidget(QLabel("Attrezzatura"))
        v_layout.addWidget(self.combo_attrezzatura_4)

        v_layout.addWidget(QLabel("Quantità"))
        self.quantita_4 = QLineEdit(self)
        v_layout.addWidget(self.quantita_4)

        self.combo_attrezzatura_5 = QComboBox()
        self.comboattrezzatura5_model = QStandardItemModel(self.combo_attrezzatura_5)
        if os.path.isfile('listaattrezzatura/data/lista_attrezzatura_salvata.pickle'):
            with open('listaattrezzatura/data/lista_attrezzatura_salvata.pickle', 'rb') as f:
                self.lista_attrezzatura_salvata_5 = pickle.load(f)
            self.lista_attrezzatura_disponibile_5 = [s for s in self.lista_attrezzatura_salvata_5 if s.is_disponibile()]
            for attrezzatura in self.lista_attrezzatura_disponibile_5:
                item = QStandardItem()
                item.setText(attrezzatura.nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboattrezzatura5_model.appendRow(item)
            self.combo_attrezzatura_5.setModel(self.comboattrezzatura5_model)
        v_layout.addWidget(QLabel("Attrezzatura"))
        v_layout.addWidget(self.combo_attrezzatura_5)

        v_layout.addWidget(QLabel("Quantità"))
        self.quantita_5 = QLineEdit(self)
        v_layout.addWidget(self.quantita_5)
