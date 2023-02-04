from qt_core import *
from mainwindow.ui_main_window import UI_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)







        self.show()

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

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_purple.xml')
    window = MainWindow()
    window.show()
    app.exec()


