from qt_core import *


class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

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
            self.left_bar.setStyleSheet("background: red")

            self.left_bar_layout = QVBoxLayout(self.left_bar)
            self.left_bar_layout.setContentsMargins(0,0,0,0)
            self.left_bar_layout.setSpacing(0)

            self.txt_site = QLineEdit()

            self.txt_email = QLineEdit()

            self.txt_senha = QLineEdit()

            self.btn_pass_gen = QPushButton("Gerar Senha")
            self.lbl_site = QLabel()
            self.lbl_email = QLabel()
            self.lbl_senha = QLabel()

            self.meu_layout = QFormLayout()
            self.meu_layout.addRow("Site/App", self.txt_site)
            

            self.left_bar_layout.addItem(self.meu_layout)
            #///////////////////////////////////////////////////
            
            


            #///////////////////////////////////////////////////
            # Setando barra direita, layout e seus widgets
            self.right_bar = QFrame()
            self.right_bar.setStyleSheet("background: blue")

            self.right_bar_layout = QVBoxLayout(self.right_bar)
            self.right_bar_layout.setContentsMargins(0,0,0,0)
            self.right_bar_layout.setSpacing(0)




            #///////////////////////////////////////////////////








            self.main_layout.addWidget(self.left_bar)
            self.main_layout.addWidget(self.right_bar)

            parent.setCentralWidget(self.main_frame)