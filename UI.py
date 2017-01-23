import sys
from QWidgit import *

class Interface(self):
    def __init__.(self)
        super.__init__()
        self.init_ui()
    
    def init_ui(self):
        
        start_button = QPushButton("Start", self)
        stop_button = QPushButton("Stop", self)
        close_button = QPushButton("Close", self)
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(start_button)
        hbox.addLayout(end_button)
        hbox.addLayout(close_button)
        
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.addLayout(vbox)
