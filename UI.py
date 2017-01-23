
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import threading



class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.time_elapsed = 0

        self.init_ui()
        self.show()
        self.run_timer()
    
    def init_ui(self):

        self.resize(400, 200)
        button_x_pos = 160
        button_y_pos = 150
        button_x_diff = 70
        button_y_diff = 0
        self.timer_label_text = "Default"

        start_button = QPushButton("Start", self)
        stop_button = QPushButton("Stop", self)
        close_button = QPushButton("Close", self)
        timer_label = QLabel(self.timer_label_text, self)
        timer_label.setFont(QFont('SansSerif', 40))

        start_button.move(button_x_pos, button_y_pos)
        stop_button.move(start_button.pos().x() + button_x_diff, start_button.pos().y() + button_y_diff)
        close_button.move(stop_button.pos().x() + button_x_diff, stop_button.pos().y() + button_y_diff)
        timer_label.move(50, 50)

    def run_timer(self):
        t = threading.Timer(1.0, self.inc_elapsed_time, [self.time_elapsed])
        t.start()

    def inc_elapsed_time(self, time_elapsed):
        self.time_elapsed = time_elapsed
        self.time_elapsed += 1
        self.timer_label_text = self.time_elapsed
        self.init_ui()
        self.run_timer()








