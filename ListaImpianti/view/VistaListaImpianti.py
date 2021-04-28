import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QHBoxLayout, QListView, QVBoxLayout
from PyQt5.uic.properties import QtGui

from ListaImpianti.controller.ControllerListaImpianti import ControllerListaImpianti


class VistaListaImpianti(QWidget):
    def __init__(self, parent= None):
        super(VistaListaImpianti, self).__init__(parent)

        self.Controller = ControllerListaImpianti()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.listview_Model = QStandardItemModel(self.list_view)
        for Impianto in self.Controller.get_lista_degli_impianti():
            item = QStandardItem()
            item.setText(Impianto.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_Model.appendRow(item)
        self.list_view.setModel(self.listview_Model)
        h_layout.addWidget(self.list_view)


        buttons_layout = QVBoxLayout()
        open_buttons = QPushButton("Apri")
        buttons_layout.addWidget(open_buttons)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle('Lista Impianti')

    def closeEvent(self, event):
        print("On close")
        self.Controller.save_data()
        event.accept()


