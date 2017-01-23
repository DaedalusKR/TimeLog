from UI import *
import sys


def main():
    app = QApplication(sys.argv)

    timer_ui = Interface()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = main()
    app.run()
