from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from Dipendente.views.VistaDipendente import VistaDipendente
from ListaDipendenti.controller.ControllerListaDipendenti import ControllerListaDipendenti
from ListaDipendenti.views.VistaInserisciDipendente import VistaInserisciDipendente


class VistaListaDipendenti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaDipendenti, self).__init__(parent)

        self.controller = ControllerListaDipendenti()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Visualizza informazioni')
        open_button.setStyleSheet(
            'QPushButton {background-color: 	#E9CFEC ; color: black; border-style: outset;border-width: 6px;'
            'border-radius: 15px;border-color: #FA8072;padding: 6px}')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)
        new_button = QPushButton("Inserisci dipendente")
        new_button.setStyleSheet(
            'QPushButton {background-color: 	#C3FDB8; color: black; border-style: outset;border-width: 6px;'
            'border-radius: 15px;border-color: #3EB489;padding: 6px}')
        new_button.clicked.connect(self.show_new_dipendente)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Dipendenti')

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for dipendente in self.controller.get_lista_dipendenti():
            item = QStandardItem()
            item.setText(dipendente.nome + " " + dipendente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

        # Funzione che mostra a schermo le informazioni del cliente selezionato

    def show_selected_info(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            dipendente_selezionato = self.controller.get_dipendente_by_index(selected)
            self.vista_dipendente = VistaDipendente(dipendente_selezionato, self.controller.elimina_dipendente_by_id,self.update_ui)
            self.vista_dipendente.show()

    def show_new_dipendente(self):
        self.vista_inserisci_dipendente = VistaInserisciDipendente(self.controller, self.update_ui)
        self.vista_inserisci_dipendente.show()

    def closeEvent(self, event):
        self.controller.save_data()
