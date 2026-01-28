from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from pyshorteners import Shortener
import qrcode
import os
import sys

def GET_PATH(myPath):
    return f''


class TelaPrograma(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("GEAR_URL.ui", self)
        
        self.shortener = Shortener()
        self.btn_gear.clicked.connect(self.on_btn_gear_clicked)
        #self.btn_save.clicked.connect(self.on_btnSalvar_clicked)

    def get_url(self):
        return self.insert_url.text()
        
    def set_url_curta(self, url):
        self.site_url.setText(url)

    def gerar_qrcode(self, url):
        img = qrcode.make(url)
        caminho = "qrcode.png"
        img.save(caminho)

        pixmap = QPixmap(caminho)
        self.lbl_qr.setPixmap(pixmap)
        self.lbl_qr.setScaledContents(True)


    @pyqtSlot()
    def on_btn_gear_clicked(self):

    
        valor = self.get_url()
        try:
            url_curta = self.shortener.tinyurl.short(valor)
            self.set_url_curta(url_curta)
            self.gerar_qrcode(url_curta)
        except Exception as e:
            print(f"Erro ao gerar URL: {e}")
            self.set_url_curta("Erro: URL inválida")
    
    #@pyqtSlot()
    #def on_btnSalvar_clicked(self, url_curta):
        #self.gerar_qrcode(url_curta)
        
if __name__ == "__main__":
    app = QApplication([])
    tela = TelaPrograma()
    tela.show()
    app.exec_()
