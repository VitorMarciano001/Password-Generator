import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QSize
from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETANDO NOME E TAMANHO DA JANELA
        #////////////////////////////////////////
        self.setWindowTitle("Password Generator")
        self.setFixedSize(QSize(740,520))
        #////////////////////////////////////////

        # INICIALIZANDO FRAME PRINCIPAL
        #////////////////////////////////////////
        self.main_layout = QWidget()
        self.main_layout.setStyleSheet("background-color: #0b0019")
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
        self.left_bar_layout.setStyleSheet("background-color: #0b0022")
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
        #////////////////////////////////////////

        # LAYOUT ONDE FICARAO OS WIDGETS DIREITO
        #////////////////////////////////////////
        self.right_bar = QVBoxLayout(self.right_bar_layout)
        #////////////////////////////////////////

        # ADICIONANDO WIDGETS A JANELA
        #////////////////////////////////////////
        self.horizontal_layout.addWidget(self.left_bar_layout)
        self.horizontal_layout.addWidget(self.right_bar_layout)
        #////////////////////////////////////////

        # INICIALIZANDO OS WIDGETS ESQUERDOS
        #////////////////////////////////////////
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
        self.password = QPushButton("Gerar Senha")
        #---------------------------------------------------------
        self.save = QPushButton("Salvar Senha")
        #---------------------------------------------------------
        self.seen = QLabel("")
        #---------------------------------------------------------
        self.formlayout = QFormLayout()
        self.formlayout.setVerticalSpacing(60)
        self.formlayout.addRow("Site/app", self.site_app)
        self.formlayout.addRow("Usuario", self.user)
        self.formlayout.addRow("N de caracteres", self.caracteres)
        self.formlayout.addRow(self.password)
        self.formlayout.addRow("Senha Criada:",self.seen)
        self.formlayout.addRow(self.save)
        #////////////////////////////////////////

        # INICIALIZANDO WIDGET DIREITO
        #////////////////////////////////////////
        self.table = QTableWidget()
        self.table.setRowCount(11)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Site/app","Usuario","Senha"])
        #////////////////////////////////////////

        # ADICIONANDO WIDGETS AO RIGHT_LAYOUT
        #////////////////////////////////////////
        self.right_bar.addWidget(self.table)
        #////////////////////////////////////////

        # ADICIONANDO WIDGETS AO LEFT_BAR
        #////////////////////////////////////////
        self.left_bar.addLayout(self.formlayout)
        #////////////////////////////////////////

        # ADICIONANDO LAYOUT AO CENTRAL WIDGET
        #////////////////////////////////////////
        self.setCentralWidget(self.main_layout)
        #////////////////////////////////////////


    def gerar_senha(self):
        pass

    def preencher_tabela(self):
        pass

app = QApplication(sys.argv)

apply_stylesheet(app, theme='dark_purple.xml')

window = MainWindow()
window.show()
app.exec()