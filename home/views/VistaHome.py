from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QBrush, QPalette
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout

from ListaClienti.views.VistaListaClienti import VistaListaClienti
from ListaDipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from ListaImpianti.view.VistaListaImpianti import VistaListaImpianti
from listaattrezzatura.views.VistaListaAttrezzature import VistaListaAttrezzature
from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)

        grid_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()


        oImage = QImage("Sfondo Home.png")
        sImage = oImage.scaled(800, 700)  # resize Image to widgets size

        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.show()

        grid_layout.addWidget(self.get_generic_button("Lista Impianti", self.go_lista_impianti))
        grid_layout.addWidget(self.get_generic_button("Lista Clienti", self.go_lista_clienti))
        grid_layout.addWidget(self.get_generic_button("Lista Dipendenti", self.go_lista_dipendenti))
        grid_layout.addWidget(self.get_generic_button("Lista Prenotazioni", self.go_lista_prenotazioni))
        grid_layout.addWidget(self.get_generic_button("Lista Atrezzature", self.go_lista_attrezzature))

        buttons_layout.addStretch()
        #grid_layout.addStretch()
        buttons_layout.addLayout(grid_layout)
        self.setLayout(buttons_layout)
        self.resize(800, 700)
        self.setWindowTitle('Gestore Impianti')

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo, self)

        button.resize(896454,1)
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