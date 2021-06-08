from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

from attrezzatura.controller.ControllerAttrezzatura import ControllerAttrezzatura


class VistaAttrezzatura(QWidget):
    def __init__(self, attrezzatura, parent=None):
        super(VistaAttrezzatura, self).__init__(parent)
        self.controller = ControllerAttrezzatura(attrezzatura)

        # Andiamo a creare due layout verticali: uno a dx e una a sx

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_attrezzatura())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        v_layout.addWidget(label_nome)
        label_nome.setAlignment(QtCore.Qt.AlignCenter)
        label_nome.setFont(QtGui.QFont("Times New Roman", 24, QtGui.QFont.Bold))
        v_layout.addWidget(label_nome)

        label_prezzo = QLabel("Prezzo: {}€".format(self.controller.get_prezzo_attrezzatura()))
        font_prezzo = label_prezzo.font()
        font_prezzo.setPointSize(25)
        label_prezzo.setFont(QtGui.QFont("Times New Roman", 16))
        v_layout.addWidget(label_prezzo)

        label_disponibile = QLabel(self.controller.get_attrezzatura_disponibile())
        font_disponibile = label_disponibile.font()
        font_disponibile.setPointSize(25)
        label_disponibile.setFont(QtGui.QFont("Times New Roman", 16))
        v_layout.addWidget(label_disponibile)

        v_layout.addStretch()

        h_layout.addLayout(v_layout)

        self.setLayout(h_layout)
        self.resize(300, 200)
        self.setWindowTitle(attrezzatura.nome)
