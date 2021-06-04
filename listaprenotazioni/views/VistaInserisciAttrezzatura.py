import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QLabel, QSpacerItem, QSizePolicy, QPushButton


class VistaInserisciAttrezzatura(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciAttrezzatura, self).__init__(parent=None)
        self.controller = controller
        self.callback = callback

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