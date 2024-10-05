import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("客户端")
        icon_path = os.path.join(os.path.dirname(__file__), 'resources', 'icon.png')
        self.setWindowIcon(QIcon(icon_path))
        self.setGeometry(100, 100, 1200, 800)  # 设置窗口大小

        # 创建网页视图
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://4399.com"))  # 替换为你想加载的网页
        self.setCentralWidget(self.browser)

        # 创建工具栏
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # 添加刷新按钮
        refresh_icon_path = os.path.join(os.path.dirname(__file__), 'resources', 'refresh.png')
        refresh_action = QAction(QIcon(refresh_icon_path), "刷新", self)
        refresh_action.triggered.connect(self.browser.reload)
        toolbar.addAction(refresh_action)

        # 你可以在这里添加更多按钮或控件

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
