from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy

from Impianti.controller.ControllerImpianto import ControllorImpianto


class VistaImpianti(QWidget):
    def __init__(self, impianto, parent=None):
        super(VistaImpianti, self).__init__(parent)
        self.controller = ControllorImpianto(impianto)

        # Andiamo a creare due layout verticali: uno a dx e una a sx

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_impianto())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)

        v_layout.addWidget(label_nome)
        label_nome.setFont(QtGui.QFont("Times New Roman", 24, QtGui.QFont.Bold))
        label_nome.move(100, 40)
        label_nome.setAlignment(QtCore.Qt.AlignCenter)

        label_prezzo = QLabel("Prezzo: {}€".format(self.controller.get_prezzo_impianto()))
        font_prezzo = label_prezzo.font()
        font_prezzo.setPointSize(25)
        label_prezzo.setFont(font_prezzo)
        label_prezzo.setFont(QtGui.QFont("Times New Roman", 16))
        v_layout.addWidget(label_prezzo)

        label_disponibile = QLabel(self.controller.get_impianto_disponibile())
        font_disponibile = label_disponibile.font()
        font_disponibile.setPointSize(25)
        label_disponibile.setFont(font_disponibile)
        label_disponibile.setFont(QtGui.QFont("Times New Roman", 16))
        v_layout.addWidget(label_disponibile)

        v_layout.addItem(QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_tipo = QLabel("Tipo: {}".format(self.controller.get_tipo_impianto()))
        font_tipo = label_tipo.font()
        font_tipo.setPointSize(17)
        label_tipo.setFont(font_tipo)
        label_tipo.setFont(QtGui.QFont("Times New Roman", 16))
        v_layout.addWidget(label_tipo)

        label_posizione = QLabel("Posizione: {}".format(self.controller.get_posizione_impianto()))
        font_posizione = label_posizione.font()
        font_posizione.setPointSize(17)
        label_posizione.setFont(font_posizione)
        label_posizione.setFont(QtGui.QFont("Times New Roman", 16))
        v_layout.addWidget(label_posizione)

        v_layout.addStretch()

        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)
        self.setWindowTitle(impianto.nome)
