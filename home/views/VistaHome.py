from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QImage, QBrush, QPalette
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel

from ListaClienti.views.VistaListaClienti import VistaListaClienti
from ListaDipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from ListaImpianti.view.VistaListaImpianti import VistaListaImpianti
from listaattrezzatura.views.VistaListaAttrezzature import VistaListaAttrezzature
from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)

        info = "Impianto Sportivo S.O.F.T"
        h_layout = QHBoxLayout()
        buttons_layout = QVBoxLayout()

        self.label_1 = QLabel(info, self)
        self.label_1.setFont(QtGui.QFont("Times New Roman", 24, QtGui.QFont.Bold))
        self.label_1.move(160, 50)
        self.label_1.setStyleSheet(
            "background-color: #FFF380; border-style: outset;border-width: 6px;border-radius: 15px;border-color: #F0E68C;padding: 2px;")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.show()
        oImage = QImage("Sfondo Home.png")
        sImage = oImage.scaled(800, 700)  # resize Image to widgets size

        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.show()

        h_layout.addWidget(self.get_generic_button("Lista Impianti", self.go_lista_impianti))
        h_layout.addWidget(self.get_generic_button("Lista Clienti", self.go_lista_clienti))
        h_layout.addWidget(self.get_generic_button("Lista Dipendenti", self.go_lista_dipendenti))
        h_layout.addWidget(self.get_generic_button("Lista Prenotazioni", self.go_lista_prenotazioni))
        h_layout.addWidget(self.get_generic_button("Lista Atrezzature", self.go_lista_attrezzature))

        buttons_layout.addStretch()
        buttons_layout.addLayout(h_layout)
        self.setLayout(buttons_layout)
        self.resize(800, 700)
        self.setWindowTitle('Gestore Impianti')

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo, self)
        # button.setStyleSheet('QPushButton {background-color: #F5E216; color: black;}')
        button.setStyleSheet(
            'QPushButton {background-color: #F5E216; color: black; border-style: outset;border-width: 6px;'
            'border-radius: 15px;border-color: #F2BB66;padding: 6px;}')

        button.resize(50, 100)
        button.clicked.connect(on_click)
        return button

    def go_lista_impianti(self):
        self.vista_lista_impanti = VistaListaImpianti()
        self.vista_lista_impanti.show()

    def go_lista_clienti(self):
        self.vist_lista_clienti = VistaListaClienti()
        self.vist_lista_clienti.show()

    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazione = VistaListaPrenotazioni()
        self.vista_lista_prenotazione.show()

    def go_lista_attrezzature(self):
        self.vista_lista_attrezzature = VistaListaAttrezzature()
        self.vista_lista_attrezzature.show()
