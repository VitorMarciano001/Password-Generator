from qt_core import *


class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

            # Resetando o tamanho da janela
            parent.resize(880, 620)
            parent.setMinimumSize(320, 280)
            #------------------------------



            