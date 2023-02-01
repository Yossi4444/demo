from PyQt5.QtWidgets import QMainWindow, QApplication

import main
import sys

class mainWindowActions(main.Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(main.Ui_MainWindow,self).__init__()

        self.setupUi(self)
        # # 打开用户登录操作
        # self.LogoutButton.clicked.connect(self.logout)
        # # 接受参数
        # self.currentUser_label.setText('admin')
        # self.currentRole_label.setText('工程师')

    def logout(self): # 用户退出登录框
        return

if __name__=='__main__':
    # 这里是界面的入口，在这里需要定义QApplication对象，之后界面跳转时不用再重新定义，只需要调用show()函数即可
    app = QApplication(sys.argv)

    # 实例化
    demo_window = mainWindowActions()
    # 显示
    demo_window.show()

    sys.exit(app.exec_())