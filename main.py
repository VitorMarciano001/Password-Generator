import sys
import csv
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QSize
from qt_material import apply_stylesheet
from random import choice


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lista_senhas = []

        # SETANDO NOME E TAMANHO DA JANELA
        #////////////////////////////////////////
        self.setWindowTitle("Password Generator")
        self.setFixedSize(QSize(753,520)) #753 tamanho horizontal e 520 tamanho vertical
        #////////////////////////////////////////

        # INICIALIZANDO FRAME PRINCIPAL
        #////////////////////////////////////////
        self.main_layout = QWidget()
        #////////////////////////////////////////

        # ADICIONANDO LAYOUT HORIZONTAL PRINCIPAL
        #////////////////////////////////////////
        self.horizontal_layout = QHBoxLayout(self.main_layout)
        self.horizontal_layout.setContentsMargins(0,0,0,0)
        self.horizontal_layout.setSpacing(0)
        #////////////////////////////////////////

        # SETANDO BARRA ESQUERDA, ONDE ESTARAO LINE EDIT E LABELS 
        #////////////////////////////////////////
        self.left_bar_layout = QWidget()
        self.left_bar_layout.setStyleSheet("background: #0b0022")
        self.left_bar_layout.setMinimumWidth(300)
        self.left_bar_layout.setMaximumWidth(300)
        #////////////////////////////////////////

        

        # LAYOUT ONDE FICARAO OS WIDGETS ESQUERDO
        #////////////////////////////////////////
        self.left_bar = QVBoxLayout(self.left_bar_layout)
        #////////////////////////////////////////

        # LAYOUT ONDE FICARAO OS DEMAIS WIDGETS
        #////////////////////////////////////////
        self.right_bar_layout = QWidget()
        self.right_bar_layout.setStyleSheet("background: #0b0019")
        #////////////////////////////////////////

        # LAYOUT ONDE FICARAO OS WIDGETS DIREITO
        #////////////////////////////////////////
        self.right_bar = QVBoxLayout(self.right_bar_layout)
        self.right_bar.setContentsMargins(0,0,0,0)
        self.right_bar.setSpacing(0)
        #////////////////////////////////////////

        # ADICIONANDO WIDGETS A JANELA
        #////////////////////////////////////////
        self.horizontal_layout.addWidget(self.left_bar_layout)
        self.horizontal_layout.addWidget(self.right_bar_layout)
        #////////////////////////////////////////

        # INICIALIZANDO OS WIDGETS ESQUERDOS
        #////////////////////////////////////////
        #---------------------------------------------------------
        self.site_app = QLineEdit()
        self.site_app.setPlaceholderText("Nome do site/app")
        #---------------------------------------------------------
        self.user = QLineEdit()
        self.user.setPlaceholderText("Usuario")
        #---------------------------------------------------------
        self.caracteres = QSpinBox()
        self.caracteres.setRange(0,12)
        self.caracteres.setValue(8)
        #---------------------------------------------------------
        self.senha = QPushButton("Gerar Senha")
        #---------------------------------------------------------
        self.endereco = QLabel()
        #---------------------------------------------------------
        self.usuario = QLabel()
        #---------------------------------------------------------
        self.senha_criada = QLabel()
        #---------------------------------------------------------
        self.save = QPushButton("Salvar Senha")
        #---------------------------------------------------------
        self.formlayout = QFormLayout()
        self.formlayout.setVerticalSpacing(40)
        self.formlayout.addRow("Site/app", self.site_app)
        self.formlayout.addRow("Usuario", self.user)
        self.formlayout.addRow("N de caracteres", self.caracteres)
        self.formlayout.addRow(self.senha)
        self.formlayout.addRow("Endereco:", self.endereco)
        self.formlayout.addRow("Usuario:", self.usuario)
        self.formlayout.addRow("Senha Criada:",self.senha_criada)
        self.formlayout.addRow(self.save)
        #////////////////////////////////////////

        # INICIALIZANDO WIDGET DIREITO
        #////////////////////////////////////////
        #---------------------------------------------------------  
        self.table = QTableWidget()
        if(self.lista_senhas != ''):
            with open("arquivos-leitura/senhas.csv") as arquivo:
                leitura = csv.reader(arquivo)
                for iterador in leitura:
                    self.lista_senhas.append(iterador)
            for row, text in enumerate(self.lista_senhas):
                for colum, data in enumerate(text):
                    self.table.setHorizontalHeaderLabels(["Site/app","Usuario","Senha"])
                    self.table.setColumnWidth(0,130)
                    self.table.setColumnWidth(1,130)
                    self.table.setColumnWidth(2,130)
                    self.table.setRowCount(len(self.lista_senhas))
                    self.table.setColumnCount(len(self.lista_senhas[0]))
                    self.table.setItem(row, colum, QTableWidgetItem(str(data)))
        #---------------------------------------------------------
        #////////////////////////////////////////

        # ADICIONANDO WIDGETS AO RIGHT_LAYOUT
        #////////////////////////////////////////
        self.right_bar.addWidget(self.table)
        #////////////////////////////////////////

        # ADICIONANDO WIDGETS AO LEFT_BAR
        #////////////////////////////////////////
        self.left_bar.addLayout(self.formlayout)
        #////////////////////////////////////////

        # CONECTANDO FUNCOES AOS BOTOES
        #////////////////////////////////////////
        self.senha.clicked.connect(self.gerar_senha)
        self.save.clicked.connect(self.update_status)
        #////////////////////////////////////////

        # ADICIONANDO LAYOUT AO CENTRAL WIDGET
        #////////////////////////////////////////
        self.setCentralWidget(self.main_layout)
        #////////////////////////////////////////


    def gerar_senha(self):
        lista_caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%&*0123456789"
        self.nova_senha = ''
        escolha_anterior = ''
        self.gerar_endereco = self.site_app.text()
        self.gerar_user = self.user.text()
        

        for i in range (0, int(self.caracteres.text())+1):
            escolha_anterior = choice(lista_caracteres)
            self.nova_senha = self.nova_senha + escolha_anterior
        

        if (self.gerar_endereco != '' and self.gerar_user != ''):
            self.endereco.setText(self.gerar_endereco)
            self.usuario.setText(self.gerar_user)
            self.senha_criada.setText(str(self.nova_senha))
    

    def update_status(self):        
        #---------------------------------------------------------
        # Inicio de variaveis
        self.lista_senhas = []
        self.minha_senha = self.gerar_endereco + "," + self.gerar_user + "," + self.nova_senha + "\n"
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Adicionando endereco, usuario e senha ao CSV
        with open("arquivos-leitura/senhas.csv", "a") as self.senha:
            self.senha.write(self.minha_senha)
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Lendo CSV e preenchendo a tabela
        with open("arquivos-leitura/senhas.csv") as arquivo:
            leitura = csv.reader(arquivo)
            for iterador in leitura:
                self.lista_senhas.append(iterador)
        for row, text in enumerate(self.lista_senhas):
            for colum, data in enumerate(text):
                self.table.setHorizontalHeaderLabels(["Site/app","Usuario","Senha"])
                self.table.setColumnWidth(0,130)
                self.table.setColumnWidth(1,130)
                self.table.setColumnWidth(2,130)
                self.table.setRowCount(len(self.lista_senhas))
                self.table.setColumnCount(len(self.lista_senhas[0]))
                self.table.setItem(row, colum, QTableWidgetItem(str(data)))
        #---------------------------------------------------------

app = QApplication(sys.argv)

apply_stylesheet(app, theme='dark_purple.xml')

window = MainWindow()
window.show()
app.exec()