from datetime import datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from abbonamento.controller.ControllerAbbonamento import ControllerAbbonamento
from abbonamento.model.Abbonamento import Abbonamento


# E' un costruttore condizionale poichè nel caso in cui l'utente ha un abbonamento comparirà sullo schermo la data di
# scadenza di quest'ultimo; altrimenti ci sarà una schermata per inserire la data di scadenza del nuovo abbonamento

# Il costruttore prende due parametri: l'abbonamento e callback_inserisci_abbonamento.
# Callback_inserisci_abbonamento verrà utilizzato nel caso in cui l'utente non abbia un abbonamento assegnato

class VistaAbbonamento(QWidget):
    def __init__(self, abbonamento, callback_inserici_abbonamento):
        super(VistaAbbonamento, self).__init__()
        self.controller = ControllerAbbonamento(abbonamento)
        self.callback_inserisci_abbonamento = callback_inserici_abbonamento

        v_layout = QVBoxLayout()
        if self.controller.is_abbonato():
            v_layout.addWidget(QLabel(self.controller.get_scadenza_string()))
        else:
            v_layout.addWidget(QLabel("Il cliente non è abbonato"))

            # La cosa più corretta da fare qui era quela di creare tre caselle di testo con in mezzo delle lable a "/"
            # in modo tale che l'utente è costretto a scrivere la data di scandeza come voglio io

            v_layout.addWidget(QLabel("Aggiungi una nuova data di scadenza abbonamento (dd/MM/yyyy)"))
            self.text_scadenza = QLineEdit()
            v_layout.addWidget(self.text_scadenza)
            btn_inserisci = QPushButton("Inserisci il nuovo abbonamento")
            btn_inserisci.clicked.connect(self.add_abbonamento_click)
            v_layout.addWidget(btn_inserisci)

        self.setLayout(v_layout)

    # Funzione di inerimento dell'abbonamento
    def add_abbonamento_click(self):
        try:
            # Tramite la funzione .strptime mi trasforma la stringa in un oggetto di tipo datetime
            # e gli diciamo che il formato deve essere giorno,mese,anno
            date = datetime.strptime(self.text_scadenza.text(), '%d/%m/%Y')
            attuale = datetime.now()
            if(date >= attuale):
                self.callback_inserisci_abbonamento(Abbonamento(date.timestamp()))
                self.close()
            else:
                QMessageBox.critical(self, 'Errore', 'La data inserita è passata',QMessageBox.Ok,QMessageBox.Ok)
        except:
            # Nel caso in cui l'utente abbia sbagliato a scrivere il formato della data gli apparirà a schermo
            # questo QMessageBox.critical con un solo pulsante che può premere(OK)
            QMessageBox.critical(self, 'Errore', 'Inserisci la data nel formato richiesto: dd/MM/yyyy', QMessageBox.Ok,
                                 QMessageBox.Ok)



