from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from Dipendente.controller.ControllerDipendente import ControllerDipendente


# Andiamo ad inserire tutto nel costruttore;
# Con "elimina_callback" andiamo a definire cosa andremo a fare dopo aver eliminato un dipendente
class VistaDipendente(QWidget):
    def __init__(self, dipendente, elimina_dipendente, elimina_callback, parent=None):
        super(VistaDipendente, self).__init__(parent)
        self.controller = ControllerDipendente(dipendente)
        self.elimina_dipendente = elimina_dipendente
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_dipendente() + " " + self.controller.get_cognome_dipendente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("Codice Fiscale: {}".format(self.controller.get_codice_fiscale_dipendente())))
        v_layout.addWidget(self.get_info("Data Nascita: {}".format(self.controller.get_data_di_nascita_dipendente())))
        v_layout.addWidget(self.get_info("Luogo Nascita: {}".format(self.controller.get_luogo_di_nascita_dipendente())))
        v_layout.addWidget(self.get_info("Email: {}".format(self.controller.get_email_dipendente())))
        v_layout.addWidget(self.get_info("Telefono: {}".format(self.controller.get_telefono_dipendente())))
        v_layout.addWidget(self.get_info("Licenza: {}".format(self.controller.get_licenza_dipendente())))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_dipendente_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_dipendente())

    # Funzione che permette di aggiungre una label con le info del dipendente;
    # Essa prende come valore il testo che dovrà comparire a schermo una volta richiamata la funzione
    def get_info(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    # Funzione che elimina il dipendente successivamente al click sul bottone "Elimina"
    def elimina_dipendente_click(self):
        self.elimina_dipendente(self.controller.get_id_dipendente())
        self.elimina_callback()
        self.close()
