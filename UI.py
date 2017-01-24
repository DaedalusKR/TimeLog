
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import threading
from timeformat import *

class Interface(QWidget):
    def __init__(self):
        super().__init__()

        # init class vars
        self.time_elapsed = 0
        self.timer_label_text = "00:00:00"
        self.timer_label = QLabel(self.timer_label_text, self)
        self.t = None

        self.init_ui()
        self.show()

    def init_ui(self):

        frame_x_len = 400
        frame_y_len = 200
        button_x_pos = 160
        button_y_pos = 150
        button_x_diff = 70
        button_y_diff = 0

        start_button = QPushButton("Start", self)
        stop_button = QPushButton("Stop", self)
        close_button = QPushButton("Close", self)

        self.timer_label.setFont(QFont('SansSerif', 40))

        start_button.move(button_x_pos, button_y_pos)
        start_button.pressed.connect(self.run_timer)
        stop_button.move(start_button.pos().x() + button_x_diff, start_button.pos().y() + button_y_diff)
        stop_button.pressed.connect(self.stop_timer)
        close_button.move(stop_button.pos().x() + button_x_diff, stop_button.pos().y() + button_y_diff)

        self.resize(frame_x_len, frame_y_len)
        self.timer_label.move(50, 50)
        self.timer_label.setFixedWidth(frame_x_len - 100)

    def run_timer(self):
        self.t = threading.Timer(1.0, self.inc_elapsed_time, [self.time_elapsed])
        self.t.start()

    def stop_timer(self):
        self.t.cancel()

    def inc_elapsed_time(self, time_elapsed):
        self.time_elapsed = time_elapsed
        self.time_elapsed += 1
        self.timer_label_text = formatted_time(self.time_elapsed)
        self.timer_label.setText(str(self.timer_label_text))
        self.run_timer()








