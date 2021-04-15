from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()

        impianto_button = QPushButton("Lista Impianti")
        impianto_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #impianto_button.clicked.connect(self.go_lista_servizi)
        clienti_button = QPushButton('Lista Clienti')
        clienti_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #clienti_button.clicked.connect(self.go_lista_clienti)
        dipendenti_button = QPushButton('Lista Dipendenti')
        dipendenti_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #dipendenti_button.clicked.connect(self.go_lista_dipendenti)
        prenotazioni_button = QPushButton('Lista Prenotazioni')
        prenotazioni_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #prenotazioni_button.clicked.connect(self.go_lista_prenotazioni)

        grid_layout.addWidget(impianto_button, 0, 0)
        grid_layout.addWidget(clienti_button, 0, 1)
        grid_layout.addWidget(dipendenti_button, 1, 0)
        grid_layout.addWidget(prenotazioni_button, 1, 1)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle('Gestore Impianto')
