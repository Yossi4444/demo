#self.pushButton.setShortcut(_translate("MainWindow", "enter")) #设置快捷键
import sys,login
import Logic_main

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox

import service
from login import Ui_login_MainWindow

class LoginWindowActions(login.Ui_login_MainWindow, QMainWindow):
    def __init__(self):
        super(login.Ui_login_MainWindow, self).__init__()

        self.setupUi(self)  # 创建窗体对象
        # 绑定槽函数`

        #登录键绑定
        self.pushButton.clicked.connect(self.open_btn_clicked)
#        self.loginbutton.clicked.connect(self.close)

    # 核心代码
    # 定义一个按钮的槽函数
    def open_btn_clicked(self):
        """点击相应按钮，跳转到第二个界面"""
        self.Name = self.lineEdit.text()  # 全局变量，记录用户名
        self.Pwd = self.lineEdit_2.text()  # 记录用户密码
        if self.Name != "" and self.Pwd != "":  # 判断用户名和密码不为空
            # 根据用户名和密码查询数据
            result = service.query("select * from user where username = %s and password = %s", self.Name, self.Pwd)
            if len(result)>0: # 如果查询结果大于0，说明存在该用户，可以登录
                self.another_window = Logic_main.mainWindowActions() # 创建主窗体对象
                self.another_window.showFullScreen()  # 显示主窗体
            else:
                self.lineEdit.setText("") # 清空用户名文本
                self.lineEdit_2.setText("") # 清空密码文本框
                QMessageBox.warning(None, '警告', '请输入正确的用户名和密码！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请输入用户名和密码！', QMessageBox.Ok)


#主程序
if __name__=='__main__':
    # 这里是界面的入口，在这里需要定义QApplication对象，之后界面跳转时不用再重新定义，只需要调用show()函数即可
    app=QApplication(sys.argv)
    #实列化
    MainWindow=LoginWindowActions()

    #显示
    MainWindow.show()

    sys.exit(app.exec_())
