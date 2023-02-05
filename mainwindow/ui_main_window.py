from qt_core import *


class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
            self.senhas = []

            

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
            self.left_bar.setContentsMargins(0,0,0,0)
            self.left_bar.setMinimumWidth(380)
            self.left_bar.setMaximumWidth(380)

            self.left_bar_layout = QVBoxLayout(self.left_bar)
            self.left_bar_layout.setContentsMargins(10,0,0,0)
            self.left_bar_layout.setSpacing(0)

            #--------------------------------------
            # Iniciando Frame da barra de temas
            self.theme_bar = QFrame()
            self.theme_bar.setMinimumHeight(60)
            self.theme_bar.setMaximumHeight(60)
            self.theme_bar.setFrameShape(QFrame.NoFrame)

            self.theme_bar_layout = QHBoxLayout(self.theme_bar)
            


            # Inicindo widgets que serao adicionados ao QFormLayout
            #--------------------------------------
            # Botao responsavel por mudar o tema da aplicacao
            self.btn_tema = QPushButton("Change Theme")
            self.btn_tema.setMaximumWidth(140)
            # ComboBox com as opcoes de temas
            self.cmb_tema = QComboBox()
            self.cmb_tema.insertItems(1, [
                'dark_amber.xml',
                'dark_cyan.xml',
                'dark_teal.xml',
                'light_amber.xml',
                'light_cyan.xml',
                'light_teal.xml'
            ])
            #--------------------------------------


            #--------------------------------------
            self.txt_site = QLineEdit()
            self.txt_user = QLineEdit()
            #--------------------------------------
            #--------------------------------------
            self.tam_senha = QSpinBox()
            self.tam_senha.setMaximum(30)
            self.tam_senha.setValue(8)
            self.cb_especial = QSpinBox()
            self.cb_especial.setMaximum(2)
            self.cb_especial.setValue(2)
            self.cb_num = QSpinBox()
            self.cb_num.setMaximum(2)
            self.cb_num.setValue(2)
            #--------------------------------------
            #--------------------------------------
            self.btn_pass_gen = QPushButton("Gerar Senha")
            #--------------------------------------
            #--------------------------------------
            self.lbl_site = QLabel()
            self.lbl_user = QLabel()
            self.lbl_senha = QLabel()
            #--------------------------------------
            #--------------------------------------
            self.btn_salvar = QPushButton("Salvar Senha")
            #--------------------------------------            


            #--------------------------------------
            # Layout esquerdo com todos os botoes e labels
            self.left_layout = QFormLayout()
            self.left_layout.setVerticalSpacing(28)
            self.left_layout.addRow("Site/App", self.txt_site)
            self.left_layout.addRow("User", self.txt_user)
            self.left_layout.addRow("Tamanho da Senha", self.tam_senha)
            self.left_layout.addRow("Caracteres", self.cb_especial)
            self.left_layout.addRow("Numeros", self.cb_num)
            self.left_layout.addRow(self.btn_pass_gen)
            self.left_layout.addRow("Site/App:", self.lbl_site)
            self.left_layout.addRow("User:", self.lbl_user)
            self.left_layout.addRow("Senha:", self.lbl_senha)
            self.left_layout.addRow(self.btn_salvar)
            #--------------------------------------


            self.theme_bar_layout.addWidget(self.cmb_tema)
            self.theme_bar_layout.addWidget(self.btn_tema)

            self.left_bar_layout.addWidget(self.theme_bar)
            self.left_bar_layout.addLayout(self.left_layout)
            # Fim da barra esquerda
            #///////////////////////////////////////////////////
            
            


            #///////////////////////////////////////////////////
            # Setando barra direita, layout e seus widgets
            self.right_bar = QFrame()
            self.right_bar.setContentsMargins(0,0,0,0)

            self.right_bar_layout = QVBoxLayout(self.right_bar)
            self.right_bar_layout.setContentsMargins(0,0,0,0)
            self.right_bar_layout.setSpacing(0)

            #--------------------------------------
            self.table_widget = QTableWidget()
            if (self.senhas != ''):
                with open("arquivos-leitura/senhas.csv") as arquivo:
                    leitura = csv.reader(arquivo)
                    for iterador in leitura:
                        self.senhas.append(iterador)
                    for row, text in enumerate(self.senhas):
                        for colum, data in enumerate(text):
                            self.table_widget.setHorizontalHeaderLabels(["Site/app","Usuario","Senha"])
                            self.table_widget.setColumnWidth(0,130)
                            self.table_widget.setColumnWidth(1,130)
                            self.table_widget.setColumnWidth(2,168)
                            self.table_widget.setRowCount(len(self.senhas))
                            self.table_widget.setColumnCount(len(self.senhas[0]))
                            self.table_widget.setItem(row, colum, QTableWidgetItem(str(data)))
            #--------------------------------------

            self.right_bar_layout.addWidget(self.table_widget)
            #///////////////////////////////////////////////////

            self.main_layout.addWidget(self.left_bar)
            self.main_layout.addWidget(self.right_bar)
            

            parent.setCentralWidget(self.main_frame)