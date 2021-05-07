from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QBrush, QPalette
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton

from ListaClienti.views.VistaListaClienti import VistaListaClienti
from ListaDipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from ListaImpianti.view.VistaListaImpianti import VistaListaImpianti


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()
        #buttons_layout = QVBoxLayout()

        oImage = QImage("test.png")
        sImage = oImage.scaled(800,700)  # resize Image to widgets size

        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)



        self.show()

        grid_layout.addWidget(self.get_generic_button("Lista Impianti", self.go_lista_impianti),0,0)
        grid_layout.addWidget(self.get_generic_button("Lista Clienti", self.go_lista_clienti),0,1)
        grid_layout.addWidget(self.get_generic_button("Lista Dipendenti", self.go_lista_dipendenti),0,2)
        grid_layout.addWidget(self.get_generic_button("Lista Prenotazioni", self.go_lista_prenotazioni),0,3)

        self.setLayout(grid_layout)
        self.resize(800, 700)
        self.setWindowTitle('Gestore Impianti')

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo,self)
        button.setGeometry(400,400,300,260)
        button.move(700, 150)
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
        pass
