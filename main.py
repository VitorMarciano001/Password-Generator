from qt_core import *
from mainwindow.ui_main_window import UI_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        self.setWindowTitle("Password Generator")


        self.ui.btn_tema.clicked.connect(self.troca_tema)
        self.ui.btn_pass_gen.clicked.connect(self.password_ganerator)
        self.ui.btn_salvar.clicked.connect(self.update_status)


        self.show()

    def password_ganerator(self):
        self.message_box = QMessageBox()
        
        self.nova_senha = ''      
        alfa_maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alfa_minuscula = "abcdefghijklmnopqrstuvwxyz"
        numerico = "1234567890"
        caractere = "!@#$%^&*"
        controle = int(self.ui.cb_especial.text()) + int(self.ui.cb_num.text())
        tamanho_senha = int(self.ui.tam_senha.text())
        resto = tamanho_senha - controle
        texto = self.ui.txt_site.text() + self.ui.txt_user.text()


        
        if (controle <= tamanho_senha and texto != ''):
            self.message_box.setWindowTitle("Senha Gerada")
            self.message_box.setText("Senha Gerada com Sucesso.")
            #self.message_box.setWindowFlag()
            self.message_box.show()

            for indice in range (1, int(self.ui.cb_especial.text())+1):
                self.nova_senha = self.nova_senha + choice(caractere)
            for i in range (1, int(self.ui.cb_num.text())+1):
                self.nova_senha = self.nova_senha + choice(numerico)
            for i in range( 1, resto+1):
                if i % 2 == 0:
                    self.nova_senha = self.nova_senha + choice(alfa_maiuscula)
                else:
                    self.nova_senha = self.nova_senha + choice(alfa_minuscula)
            self.nova_senha = list(self.nova_senha)
            for i in range (0,10):
                shuffle(self.nova_senha)

            self.nova_senha = ''.join(self.nova_senha)

            self.ui.lbl_senha.setText(self.nova_senha)
            self.ui.lbl_site.setText(self.ui.txt_site.text())
            self.ui.lbl_user.setText(self.ui.txt_user.text())
        else:
            self.message_box.setWindowTitle("Senha nao Gerada")
            self.message_box.setText("Preencha todos os campos, por favor.")
                                     
            self.message_box.show()
    
    def update_status(self):
        #---------------------------------------------------------
        # Inicio de variaveis
        self.lista_senhas = []
        self.minha_senha = self.ui.txt_site.text() + "," + self.ui.txt_user.text() + "," + self.nova_senha + "\n"
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Adicionando endereco, usuario e self.nova_senha ao CSV
        with open("arquivos-leitura/senhas.csv", "a") as self.nova_senha:
            self.nova_senha.write(self.minha_senha)
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Lendo CSV e preenchendo a tabela
        with open("arquivos-leitura/senhas.csv") as arquivo:
            leitura = csv.reader(arquivo)
            for iterador in leitura:
                self.lista_senhas.append(iterador)
        for row, text in enumerate(self.lista_senhas):
            for colum, data in enumerate(text):
                self.ui.table_widget.setHorizontalHeaderLabels(["Site/app","Usuario","Senha"])
                self.ui.table_widget.setColumnWidth(0,130)
                self.ui.table_widget.setColumnWidth(1,130)
                self.ui.table_widget.setColumnWidth(2,168)
                self.ui.table_widget.setRowCount(len(self.lista_senhas))
                self.ui.table_widget.setColumnCount(len(self.lista_senhas[0]))
                self.ui.table_widget.setItem(row, colum, QTableWidgetItem(str(data)))

    def troca_tema(self):
        tema = self.ui.cmb_tema.currentText()
        
        match tema:
            case 'dark_amber.xml':
                apply_stylesheet(app, theme='dark_amber.xml')
            case 'dark_cyan.xml':
                apply_stylesheet(app, theme='dark_cyan.xml')
            case 'dark_teal.xml':
                apply_stylesheet(app, theme='dark_teal.xml')
            case 'light_amber.xml':
                apply_stylesheet(app, theme='light_amber.xml')
            case 'light_cyan.xml':
                apply_stylesheet(app, theme='light_cyan.xml')
            case 'light_teal.xml':
                apply_stylesheet(app, theme='light_teal.xml')

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_amber.xml')
    window = MainWindow()
    window.show()
    app.exec()


