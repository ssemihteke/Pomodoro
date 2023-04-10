import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont,QIcon
import time


class Pomodoro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pomodoro_time = 25 * 60
        self.break_time = 5 * 60
        self.long_break_time = 15 * 60
        self.timer_running = False
        self.pomodoros_completed = 0
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Pomodoro")
        self.setGeometry(100,100,400,200)


        self.time_display = QLabel(self)
        self.time_display.setFont(QFont('Helvetica', 48))
        self.time_display.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.time_display)

        start_button = QPushButton("Başlat", self)
        start_button.clicked.connect(self.start_timer)
        reset_button = QPushButton("Sıfırla", self)
        reset_button.clicked.connect(self.reset_timer)

        self.statusBar().addWidget(start_button)
        self.statusBar().addWidget(reset_button)

        self.pomodoros_completed_label = QLabel("Tamamlanan Pomodorolar: 0", self)
        self.statusBar().addPermanentWidget(self.pomodoros_completed_label)

        self.show()

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.run_timer(self.pomodoro_time)

    def run_timer(self, remaining_time):
        self.time_display.setText(time.strftime('%M:%S', time.gmtime(remaining_time)))
        if remaining_time <= 0:
            self.pomodoros_completed += 1
            self.pomodoros_completed_label.setText('Tamamlanan Pomodorolar: ' + str(self.pomodoros_completed))
            if self.pomodoros_completed % 4 == 0:
                self.run_timer(self.long_break_time)
            else:
                self.run_timer(self.break_time)
        else:
            QTimer.singleShot(1000, lambda: self.run_timer(remaining_time - 1))

    def reset_timer(self):
        self.timer_running = False
        self.time_display.setText('00:00')
        self.pomodoros_completed = 0
        self.pomodoros_completed_label.setText('Tamamlanan Pomodorolar: 0')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pomodoro()
    ex.show()
    sys.exit(app.exec_())