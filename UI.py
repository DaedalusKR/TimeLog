from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import threading
from timeformat import *
import json
import os
import sys
import os.path


class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.set_vars()
        self.init_ui()
        self.file_check_set()
        self.show()

    def set_vars(self):
        # init class vars #
        # self.time_elapsed = 0
        self.timer_label_text = "00:00:00"
        self.timer_label = QLabel(self.timer_label_text, self)
        self.timer_count_thread = None
        self.list_options = QListWidget(self)
        self.save_object = []

    def init_ui(self):
        # set vars for UI elements
        frame_x_len = 400
        frame_y_len = 200
        button_x_pos = 160
        button_y_pos = 150
        button_x_diff = 70
        button_y_diff = 0

        # create UI elements
        start_button = QPushButton("Start", self)
        stop_button = QPushButton("Stop", self)
        close_button = QPushButton("Close", self)
        add_button = QPushButton("Add", self)
        remove_button = QPushButton(str("Delete"),self)
        self.timer_label.setFont(QFont('SansSerif', 40))

        # position UI elements
        start_button.move(button_x_pos, button_y_pos)
        start_button.clicked.connect(self.run_timer)
        stop_button.move(start_button.pos().x() + button_x_diff, start_button.pos().y() + button_y_diff)
        stop_button.clicked.connect(self.stop_timer)
        close_button.move(stop_button.pos().x() + button_x_diff, stop_button.pos().y() + button_y_diff)
        close_button.clicked.connect(lambda: sys.exit())
        add_button.move(2, 130)
        add_button.clicked.connect(self.add_timer)
        remove_button.move(60, 130)
        remove_button.clicked.connect(self.remove_timer)
        self.resize(frame_x_len, frame_y_len)
        self.timer_label.move(180, 50)
        self.timer_label.setFixedWidth(frame_x_len - 100)
        self.list_options.setGeometry(10, 10, 135, 120)
        self.update_timers()
        self.list_options.setCurrentRow(0)
        self.list_options.itemSelectionChanged.connect(lambda: self.update_timer_label())

    def file_check_set(self):
        if os.path.isfile('./SaveData.txt'):
            self.timers = self.load_timer_file()
            self.update_timer_label()
        else:
            self.timers = []
            self.save_timer_file(self.timers)
            self.time_elapsed = 0

    def update_timer_label(self):
            selected_timer = self.list_options.currentItem().text()
            print(selected_timer)
            for item in self.timers:
                if item['tTitle'] == selected_timer:
                    self.timer_label.setText(str(formatted_time(item['tSeconds'])))
                    self.time_elapsed = item['tSeconds']
                    print(self.timer_label.text())

    def update_timers(self):
        self.timers = None
        self.timers = self.load_timer_file()
        temp_timers = self.timers

        for item in temp_timers:
            self.list_options.addItem(item['tTitle'])
            print('added')

    def save_timer_file(self, save_object):
        with open("SaveData.txt", "w") as outfile:
            json.dump(save_object, outfile)
        outfile.close()
        print("File Data Saved")

    def load_timer_file(self):
        with open("SaveData.txt", "r") as infile:
            loaded_data = json.load(infile)
            infile.close()

        return loaded_data

    def add_timer(self):
        new_timer = QInputDialog.getText(self, "New Timer", "What are you timing?")
        timer_title = new_timer[0]
        new_timer = {"tTitle": timer_title, "tSeconds": int(0)}
        self.timers.append(new_timer)
        self.save_timer_file(self.timers)
        self.list_options.addItem(str(timer_title))

    def remove_timer(self):
        remove_confirm_box = QMessageBox()
        remove_confirm_box.setIcon(QMessageBox.Question)
        remove_confirm_box.setWindowTitle("Remove Timer")
        remove_confirm_box.setText("Are you sure you want to delete this timer? This can\'t be undone")
        remove_confirm_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        remove_action_selected = remove_confirm_box.exec()

        # look at the returned qmessagebox button pressed and remove or ignore
        if remove_action_selected == QMessageBox.Ok:
            iterator = 0
            for items in self.timers:
                if items['tTitle'] == self.list_options.currentItem().text():
                    print(iterator)
                    del self.timers[iterator]
                    self.save_timer_file(self.timers)
                iterator += 1

            item = self.list_options.takeItem(self.list_options.currentRow())
            item = None
        else:
            pass

    def run_timer(self):
        # GUI is running from the main thread so create a second thread to increate the timer every second
        self.timer_count_thread = threading.Timer(1.0, self.inc_elapsed_time, [self.time_elapsed])
        self.timer_count_thread.start()

    def stop_timer(self):
        self.timer_count_thread.cancel()

    def inc_elapsed_time(self, time_elapsed):
        # Update the timer every second to inc by 1 and update the UI variable.
        # Recurse back into the function until stop_timer() gets called from the UI
        self.time_elapsed = time_elapsed
        self.time_elapsed += 1

        # find timer in the timers dict and update the file each tick
        if self.list_options.count() > 0:
            for item in self.timers:
                if self.list_options.currentItem().text() == item['tTitle']:
                    item['tSeconds'] = self.time_elapsed
                    self.save_timer_file(self.timers)
                    self.list_options.update()

        self.timer_label_text = formatted_time(self.time_elapsed)
        self.timer_label.setText(str(self.timer_label_text))
        self.run_timer()








