from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy

from attrezzatura.controller.ControllerAttrezzatura import ControllerAttrezzatura


class VistaAttrezzatura(QWidget):
    def __init__(self, attrezzatura , parent=None):
        super(VistaAttrezzatura, self).__init__(parent)
        self.controller = ControllerAttrezzatura(attrezzatura)

    #Andiamo a creare due layout verticali: uno a dx e una a sx

        h_layout = QHBoxLayout()

        v_layout = QVBoxLayout()
        label_nome = QLabel(self.controller.get_nome_attrezzatura())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)


        h_layout.addItem(QSpacerItem(50, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout2 = QVBoxLayout()
        label_prezzo = QLabel("Prezzo {}€".format(self.controller.get_prezzo_attrezzatura()))
        font_prezzo = label_prezzo.font()
        font_prezzo.setPointSize(25)
        label_prezzo.setFont(font_prezzo)
        v_layout2.addWidget(label_prezzo)

        label_disponibile = QLabel(self.controller.get_attrezzatura_disponibile())
        font_disponibile = label_disponibile.font()
        font_disponibile.setPointSize(25)
        label_disponibile.setFont(font_disponibile)
        v_layout2.addWidget(label_disponibile)

        h_layout.addLayout(v_layout2)

        self.setLayout(h_layout)
        self.setWindowTitle(attrezzatura.nome)