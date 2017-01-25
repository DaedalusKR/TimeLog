
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
        self.timer_count_thread = None
        # end of init class vars

        #set up Timer UI and push to screen
        self.init_ui()
        self.show()

    def init_ui(self):
        #set vars for UI elements
        frame_x_len = 400
        frame_y_len = 200
        button_x_pos = 160
        button_y_pos = 150
        button_x_diff = 70
        button_y_diff = 0

        #create UI elements
        start_button = QPushButton("Start", self)
        stop_button = QPushButton("Stop", self)
        close_button = QPushButton("Close", self)
        self.timer_label.setFont(QFont('SansSerif', 40))

        #position UI elements
        start_button.move(button_x_pos, button_y_pos)
        start_button.pressed.connect(self.run_timer)
        stop_button.move(start_button.pos().x() + button_x_diff, start_button.pos().y() + button_y_diff)
        stop_button.pressed.connect(self.stop_timer)
        close_button.move(stop_button.pos().x() + button_x_diff, stop_button.pos().y() + button_y_diff)
        self.resize(frame_x_len, frame_y_len)
        self.timer_label.move(50, 50)
        self.timer_label.setFixedWidth(frame_x_len - 100)

    def run_timer(self):
        #GUI is running from the main thread so create a second thread to increate the timer every second 
        self.timer_count_thread = threading.Timer(1.0, self.inc_elapsed_time, [self.time_elapsed])
        self.timer_count_thread.start()

    def stop_timer(self):
        self.timer_count_thread.cancel()

    def inc_elapsed_time(self, time_elapsed):
        #Update the timer every second to inc by 1 and update the UI variable. 
        #Recurse back into the function until stop_timer() gets called from the UI
        self.time_elapsed = time_elapsed
        self.time_elapsed += 1
        self.timer_label_text = formatted_time(self.time_elapsed)
        self.timer_label.setText(str(self.timer_label_text))
        self.run_timer()








