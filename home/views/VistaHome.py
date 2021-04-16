from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()


        grid_layout.addWidget(self.get_generic_button("Lista Impianti"),0 , 0)
        grid_layout.addWidget(self.get_generic_button("Lista Clienti"), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Lista Dipendenti"), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Prenotazioni"), 1, 1)

        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle('Gestore Impianto')

    def get_generic_button(self , titolo):
            button = QPushButton(titolo)
            button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
            return button
