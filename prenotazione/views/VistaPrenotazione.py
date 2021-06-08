from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from prenotazione.controller.ControllerPrenotazione import ControllerPrenotazione


class VistaPrenotazione(QWidget):
    def __init__(self, prenotazione, disdici_prenotazione, elimina_callback, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        self.controller = ControllerPrenotazione(prenotazione)
        self.disdisci_prenotazione = disdici_prenotazione
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_impianto_prenotazione().nome + " " +
                            self.controller.get_impianto_prenotazione().posizione)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(QtGui.QFont("Times New Roman", 24, QtGui.QFont.Bold))
        label_nome.setAlignment(QtCore.Qt.AlignCenter)

        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_cliente = QLabel("Cliente: {} {}".format(self.controller.get_cliente_prenotazione().nome,
                                                       self.controller.get_cliente_prenotazione().cognome))
        font_cliente = label_cliente.font()
        font_cliente.setPointSize(30)
        label_cliente.setFont(QtGui.QFont("Times New Roman", 16))
        v_layout.addWidget(label_cliente)

        label_data = QLabel("Data: {}".format(self.controller.get_data_prenotazione()))
        font_data = label_data.font()
        font_data.setPointSize(30)
        label_data.setFont(QtGui.QFont("Times New Roman", 16))
        v_layout.addWidget(label_data)

        label_orario = QLabel("Orario: {}:00    Numero ore: {}".format(self.controller.get_orario_prenotazione(),
                                                                       self.controller.get_numero_ore_prenotazione()))
        font_orario = label_orario.font()
        font_orario.setPointSize(30)
        label_orario.setFont(QtGui.QFont("Times New Roman", 16))
        v_layout.addWidget(label_orario)

        label_att = QLabel("{}".format(self.controller.get_attrezzatura_prenotazione()))
        font_att = label_att.font()
        font_att.setPointSize(30)
        label_att.setFont(QtGui.QFont("Times New Roman", 16))
        v_layout.addWidget(label_att)

        label_tot = QLabel("Totale €{}".format(self.controller.get_totale_prenotazione()))
        font_tot = label_tot.font()
        font_tot.setPointSize(30)
        label_tot.setFont(QtGui.QFont("Times New Roman", 16))
        v_layout.addWidget(label_tot)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_disdici = QPushButton("Disdici")
        btn_disdici.setStyleSheet(
            'QPushButton {background-color: 	#FF0000 ; color: black; border-style: outset;border-width: 4px;'
            'border-radius: 15px;border-color: #FA8072;padding: 4px}')
        btn_disdici.clicked.connect(self.disdici_prenotazione_click)
        v_layout.addWidget(btn_disdici)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_impianto_prenotazione().nome)

    def disdici_prenotazione_click(self):
        self.disdisci_prenotazione(self.controller.get_id_prenotazione())
        self.elimina_callback()
        self.close()
