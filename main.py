from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from pyshorteners import Shortener
from PyQt5.QtCore import pyqtSlot

class TelaPrograma(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("GEAR_URL.ui", self)
        
        self.shortener = Shortener()
        
        self.btn_gear.clicked.connect(self.on_btn_gear_clicked)

    def get_url(self):
        return self.site_url.text()
        
    def set_url_curta(self, url):
        self.site_url.setText(url)
    
    @pyqtSlot()    
    def on_btn_gear_clicked(self):
        valor = self.get_url()
        try:
            url_curta = self.shortener.tinyurl.short(valor)
            self.set_url_curta(url_curta)
        except Exception as e:
            print(f"Erro ao gerar URL: {e}")
            self.set_url_curta("Erro: URL inválida")

if __name__ == "__main__":
    app = QApplication([])

    tela = TelaPrograma()
    tela.show()

    app.exec_()
