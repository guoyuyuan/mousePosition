from PyQt5.QtCore import QTime,QTimer
from PyQt5.QtGui import QKeySequence
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import  QIcon
import pyautogui
from threading import Thread
import time





class Main:
    def __init__(self):
        # 加载ui文件
        self.ui = QUiLoader().load('mouse.ui')

        # 创建一个QTimer对象
        self.timer = QTimer()
        # QTimer开始计时
        self.ui.start_pushButton.clicked.connect(self.timer.start(1000))
        self.timer.timeout.connect(self.start_thread)




        # 执行主程序，即自动调用各种方法
        self.action()


    # 设计一个方法，用于自动调用各种方法
    def action(self):
        self.ui.start_pushButton.clicked.connect(self.start_thread)
        self.ui.end_pushButton.clicked.connect(self.end_thread)

    def start_thread(self):
        # 设置QTimer开始计时，且设定时间为1000ms
        self.timer.start(1000)
        self.timer.setInterval(1000) # 间隔时间为一秒
        s = Thread(target=self.start_button())
        s.start()



    def end_thread(self):
        # 停止定时器
        self.timer.stop()
        e = Thread(target=self.end_button())
        e.start()




    def start_button(self):


        x, y = pyautogui.position()
        print(f"鼠标位置：{x, y}")
        self.ui.x_textEdit.setText(str(x))
        self.ui.x_textEdit.setEnabled(False) # 设置文本不可编辑 shortcut

        self.ui.y_textEdit.setText(str(y))
        self.ui.y_textEdit.setEnabled(False)  # 设置文本不可编辑



    def end_button(self):
        print("点击了end按钮")
        self.reset_clicked = True



if __name__ == '__main__':
    # 加载ui文件
    app = QApplication([])
    m = Main()
    m.ui.show()
    app.exec_()