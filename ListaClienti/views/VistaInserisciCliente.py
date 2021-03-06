from datetime import datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from Cliente.model.Cliente import Cliente


class VistaInserisciCliente(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciCliente, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_form_entry("Nome")
        self.get_form_entry("Cognome")
        self.get_form_entry("Codice Fiscale")
        self.get_form_entry("Telefono")
        self.get_form_entry("Data di nascita (dd/MM/yyyy)")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.setStyleSheet(
            "background-color: #F5E216; border-style: outset;border-width: 6px;"
            "border-radius: 15px;border-color: #F0E68C;padding: 2px;")
        btn_ok.clicked.connect(self.add_cliente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Cliente")

    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def add_cliente(self):
        nome = self.info["Nome"].text()
        cognome = self.info["Cognome"].text()
        codice_fiscale = self.info["Codice Fiscale"].text()
        telefono = self.info["Telefono"].text()
        data_di_nascita = self.info["Data di nascita (dd/MM/yyyy)"].text()

        if nome == "" or cognome == "" or codice_fiscale == "" or telefono == "" or data_di_nascita == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            if len(codice_fiscale) != 16:
                QMessageBox.critical(self, 'Errore',
                                     'Per favore, inserisci il codice fiscale correttamente correttamente',
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:

                if len(telefono) != 10:
                    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci il numero di telefono correttamente',
                                         QMessageBox.Ok, QMessageBox.Ok)
                else:

                    try:
                        date = datetime.strptime(data_di_nascita, '%d/%m/%Y')
                        attuale = datetime.now()
                        if date <= attuale:
                            self.controller.aggiungi_cliente(Cliente((nome + cognome).lower(), nome, cognome,
                                                                     codice_fiscale, telefono, data_di_nascita))
                            self.callback()
                            self.close()
                        else:
                            QMessageBox.critical(self, 'Errore', 'La data inserita ?? futura', QMessageBox.Ok,
                                                 QMessageBox.Ok)
                    except:
                        QMessageBox.critical(self, 'Errore', 'Inserisci la data nel formato richiesto: dd/MM/yyyy',
                                             QMessageBox.Ok,
                                             QMessageBox.Ok)
