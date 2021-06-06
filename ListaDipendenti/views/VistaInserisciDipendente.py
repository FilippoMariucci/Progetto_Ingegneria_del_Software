from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from Dipendente.model.Dipendente import Dipendente
from datetime import datetime

class VistaInserisciDipendente(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciDipendente, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_form_entry("Nome")
        self.get_form_entry("Cognome")
        self.get_form_entry("Data di nascita (dd/MM/yyyy)")
        self.get_form_entry("Luogo di nascita")
        self.get_form_entry("Codice Fiscale")
        self.get_form_entry("Telefono")
        self.get_form_entry("Email")
        self.get_form_entry("Licenza")


        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_dipendente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Dipendente")

    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def add_dipendente(self):
        nome = self.info["Nome"].text()
        cognome = self.info["Cognome"].text()
        data_di_nascita = self.info["Data di nascita"].text()
        luogo_di_nascita = self.info["Luogo di nascita"].text()
        codice_fiscale = self.info["Codice Fiscale"].text()
        telefono = self.info["Telefono"].text()
        email = self.info["Email"].text()
        licenza = self.info["Licenza"].text()


        if nome == "" or cognome == ""  or data_di_nascita == "" or luogo_di_nascita == "" or codice_fiscale == "" \
                or telefono == "" or email == "" or licenza == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            if len(codice_fiscale) != 16 :
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci il codice fiscale correttamente correttamente',
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
                            self.controller.aggiungi_dipendente(Dipendente((nome + cognome).lower(), nome, cognome, data_di_nascita,
                                                                           luogo_di_nascita, codice_fiscale, telefono, email, licenza
                                                                           ))
                            self.callback()
                            self.close()
                        else:
                            QMessageBox.critical(self, 'Errore', 'La data inserita è futura', QMessageBox.Ok,
                                             QMessageBox.Ok)
                    except:
                        QMessageBox.critical(self, 'Errore', 'Inserisci la data nel formato richiesto: dd/MM/yyyy',
                                         QMessageBox.Ok,
                                         QMessageBox.Ok)