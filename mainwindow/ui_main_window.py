from qt_core import *


class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
            width = 150

            # Resetando o tamanho da janela
            parent.resize(880, 620)
            parent.setMinimumSize(320, 280)
            #------------------------------


            #///////////////////////////////////////////////////
            # Setando frame e layout principal da janela
            self.main_frame = QFrame()
            
            self.main_layout = QHBoxLayout(self.main_frame)
            self.main_layout.setContentsMargins(0,0,0,0)
            self.main_layout.setSpacing(0)
            #///////////////////////////////////////////////////


            #///////////////////////////////////////////////////
            # Setando barra esquerda, layout e seus widgets
            self.left_bar = QFrame()
            self.left_bar.setMinimumWidth(380)
            self.left_bar.setMaximumWidth(380)

            self.left_bar_layout = QVBoxLayout(self.left_bar)
            self.left_bar_layout.setContentsMargins(0,0,0,0)
            self.left_bar_layout.setSpacing(0)

            self.txt_site = QLineEdit()
            self.txt_site.setMinimumWidth(width)
            self.txt_site.setMaximumWidth(width)

            self.txt_email = QLineEdit()

            self.txt_senha = QLineEdit()

            self.cb_especial = QSpinBox()
            
            self.cb_num = QSpinBox()

            
            self.btn_pass_gen = QPushButton("Gerar Senha")
            self.btn_pass_gen.setMinimumWidth(width)
            self.btn_pass_gen.setMaximumWidth(width)

            self.lbl_site = QLabel()
            self.lbl_email = QLabel()
            self.lbl_senha = QLabel()

            self.btn_salvar = QPushButton("Salvar Senha")

            self.meu_layout = QFormLayout()
            self.meu_layout.addRow("Site/App", self.txt_site)
            self.meu_layout.addRow("E-mail", self.txt_email)
            self.meu_layout.addRow("Senha", self.txt_senha)
            self.meu_layout.addRow("QTD; Caracteres", self.cb_especial)
            self.meu_layout.addRow("QTD; Numeros", self.cb_num)
            self.meu_layout.addRow(self.btn_pass_gen)
            self.meu_layout.addRow("Site/App:", self.lbl_site)
            self.meu_layout.addRow("E-mail:", self.lbl_email)
            self.meu_layout.addRow("Senha:", self.lbl_senha)
            self.meu_layout.addRow(self.btn_salvar)

            self.left_bar_layout.addLayout(self.meu_layout)
            #///////////////////////////////////////////////////
            
            


            #///////////////////////////////////////////////////
            # Setando barra direita, layout e seus widgets
            self.right_bar = QFrame()

            self.right_bar_layout = QVBoxLayout(self.right_bar)
            self.right_bar_layout.setContentsMargins(0,0,0,0)
            self.right_bar_layout.setSpacing(0)




            #///////////////////////////////////////////////////








            self.main_layout.addWidget(self.left_bar)
            self.main_layout.addWidget(self.right_bar)

            parent.setCentralWidget(self.main_frame)