from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from Cliente.views.VistaCliente import VistaCliente
from ListaClienti.controller.ControllerListaClienti import ControllerListaClienti
from ListaClienti.views.VistaInserisciCliente import VistaInserisciCliente


class VistaListaClienti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaClienti, self).__init__(parent)

        self.controller = ControllerListaClienti()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Visualizza informazioni")
        open_button.setStyleSheet(
            'QPushButton {background-color: 	#E9CFEC ; color: black; border-style: outset;border-width: 6px;'
            'border-radius: 15px;border-color: #FA8072;padding: 6px}')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton("Inserisci cliente")
        new_button.clicked.connect(self.show_new_cliente)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        new_button.setStyleSheet(
            'QPushButton {background-color: 	#C3FDB8; color: black; border-style: outset;border-width: 6px;'
            'border-radius: 15px;border-color: #3EB489;padding: 6px}')
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 400)
        self.setWindowTitle("Lista Clienti")

    # Funzione che mostra a schermo le informazioni del cliente selezionato
    def show_selected_info(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            selected = self.list_view.selectedIndexes()[0].row()
            cliente_selezionato = self.controller.get_cliente_by_index(selected)
            self.vista_cliente = VistaCliente(cliente_selezionato, self.controller.elimina_cliente_by_id,
                                              self.update_ui)
            self.vista_cliente.show()

    def show_new_cliente(self):
        self.vista_inserisci_cliente = VistaInserisciCliente(self.controller, self.update_ui)
        self.vista_inserisci_cliente.show()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.controller.get_lista_dei_clienti():
            item = QStandardItem()
            item.setText(cliente.nome + " " + cliente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()
