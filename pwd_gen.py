import platform, string, secrets, os
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIcon

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # Lädt die UI-Datei
        uic.loadUi("interface.ui", self)

        # Setzt das Fenster-Icon
        self.setWindowIcon(QIcon("icon.ico"))

        # Verbinde den Button mit einer Funktion
        self.generateButton = self.findChild(QtWidgets.QPushButton, "generateButton")
        self.outputTextEdit = self.findChild(QtWidgets.QPlainTextEdit, "outputTextEdit")
        self.lengthInput = self.findChild(QtWidgets.QLineEdit, "lengthInput")
        self.generateButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        # Generiert ein Passwort und zeigt es im PlainTextEdit an
        try:
            USERINPUT = int(self.lengthInput.text())
            CHARACTERS = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
            PASSWD = "".join(secrets.choice(CHARACTERS) for _ in range(USERINPUT))
            self.outputTextEdit.setPlainText(PASSWD)
        except ValueError:
            self.outputTextEdit.setPlainText("Please enter a valid number")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
