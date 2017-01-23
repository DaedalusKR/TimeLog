
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit)

class Interface(QWidget):
    def __init__(self):
        super().__init__()
        print("in class")
        self.init_ui()
    
    def init_ui(self):

        start_button = QPushButton("Start", self)
        stop_button = QPushButton("Stop", self)
        close_button = QPushButton("Close", self)
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(start_button)
        hbox.addWidget(stop_button)
        hbox.addWidget(close_button)
        
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        self.resize(400,200)

        self.show()

# app = QApplication(sys.argv)
#
# window = Interface()
# sys.exit(app.exec_())

