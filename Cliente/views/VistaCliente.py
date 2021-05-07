from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from Cliente.controller.ControllerCliente import ControllerCliente

# Andiamo ad inserire tutto nel costruttore;
# Con "elimina_callback" andiamo a definire cosa andremo a fare dopo aver eliminato un cliente
from abbonamento.views.VistaAbbonamento import VistaAbbonamento


class VistaCliente(QWidget):
    def __init__(self, cliente, elimina_cliente, elimina_callback, parent=None):
        super(VistaCliente, self).__init__(parent)
        self.controller = ControllerCliente(cliente)
        self.elimina_cliente = elimina_cliente
        self.elimina_callback = elimina_callback

    # Definiamo un layout verticale e la andiamo a argomentare con le lable(caselle di testo)
    # in cui scriviamo il nome, cognome, ... del cliente
        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

    # Aggiungiamo un QSpaceItem(spazio) che si espande all'allargare della finestra
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_label_info("Codice Fiscale", self.controller.get_codice_fiscale_cliente()))
        v_layout.addWidget(self.get_label_info("Telefono", self.controller.get_telefono_cliente()))
        v_layout.addWidget(self.get_label_info("Età", self.controller.get_data_di_nascita_cliente()))

    # Andiamo ad aggiungere un altro QSpaceItem
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_abbonamento = QPushButton("Visualizza abbonamento")
        btn_abbonamento.clicked.connect(self.check_abbonamento)
        v_layout.addWidget(btn_abbonamento)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina cliente")
        btn_elimina.clicked.connect(self.elimina_cliente_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente())

    # Funzione che permette di aggiungre una label con le info del cliente;
    # Essa prende due valori: il testo che deve essere visulizzato a schermo ed il valore
    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    # Funzione dove richiameremo VistaAbbonamento e gli passiamo .get_abbonamento_cliente()
    # e .aggiungi_nuovo_abbonamento_cliente poiche abbiamo un costruttore condizonato
    def check_abbonamento(self):
        self.vista_abbonamento = VistaAbbonamento(self.controller.get_abbonamento_cliente(),
                                                  self.controller.aggiungi_nuovo_abbonamento_cliente)
        self.vista_abbonamento.show()

    # Funzione che al click di "elimina cliente" elimina il cliente tramite id
    def elimina_cliente_click(self):
        self.elimina_cliente(self.controller.get_id_cliente())
        self.elimina_callback()
        self.close()
