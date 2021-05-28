
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QHBoxLayout, QListView, QVBoxLayout

from attrezzatura.views.VistaAttrezzatura import VistaAttrezzatura
from listaattrezzatura.controller.ControllerListaAttrezzatura import ControllerListaAttrezzatura


class VistaListaAttrezzature(QWidget):
    def __init__(self, parent= None):
        super(VistaListaAttrezzature, self).__init__(parent)

        self.Controller = ControllerListaAttrezzatura()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.listview_Model = QStandardItemModel(self.list_view)
        for Attrezzatura in self.Controller.get_lista_delle_attrezzature():
            item = QStandardItem()
            item.setText(Attrezzatura.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_Model.appendRow(item)
        self.list_view.setModel(self.listview_Model)
        h_layout.addWidget(self.list_view)


        buttons_layout = QVBoxLayout()
        open_buttons = QPushButton("Apri")
        open_buttons.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_buttons)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle('Lista Attrezzature')

    def closeEvent(self, event):
        print("On close")
        self.Controller.save_data()
        event.accept()

    # Metodo che permette di visualizzare un Impianti attraverso l'indice
    def show_selected_info(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            selected = self.list_view.selectedIndexes()[0].row()
            attrezzatura_selezionata = self.Controller.get_attrezzatura_by_index(selected)
            self.vista_attrezzature= VistaAttrezzatura(attrezzatura_selezionata)
            self.vista_attrezzature.show()