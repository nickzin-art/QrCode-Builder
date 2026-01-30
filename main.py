from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from pyshorteners import Shortener
from PyQt5.QtCore import QDateTime
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter
import qrcode
import os
from os import path
import sys


class TelaPrograma(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("GEAR_URL.ui", self)
        
        self.shortener = Shortener()
        self.btn_gear.clicked.connect(self.on_btn_gear_clicked)
        self.btn_save.clicked.connect(self.on_btnSalvar_clicked)
        self.btn_save.setEnabled(True)

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

    def salvar(self):
        nome_arquivo , _ = QFileDialog.getSaveFileName(self, "Salvar Imagem")
        if nome_arquivo:
            caminho = path.dirname(nome_arquivo)
            nome = nome_arquivo.removeprefix(caminho)

            with open("qrcode.png", "rb") as fotoQr:
                Qrcode = fotoQr.read()

            with open(caminho+f"{nome}.png", "wb") as foto:
                foto.write(Qrcode)

            self.ShowMessage("Imagem", "Imagem salva com sucesso")
            self.reset()


    def reset(self):
        self.btn_save.setEnabled(False)
        self.insert_url.setText("")
        self.site_url.setText("")
        self.lbl_qr.clear()

    def ShowMessage(self, title, message):
        QMessageBox.information(self, title, message)



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
    
    @pyqtSlot()
    def on_btnSalvar_clicked(self):
        self.salvar()



        

        

        
if __name__ == "__main__":
    app = QApplication([])
    tela = TelaPrograma()
    tela.show()
    app.exec_()
