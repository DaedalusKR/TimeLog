from UI import *
import sys
import threading
from timeformat import  *



def main():
    app = QApplication(sys.argv)

    #create ui window
    timer_ui = Interface()

    #ensure system exits cleanly when main terminates
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = main()
    app.run()
