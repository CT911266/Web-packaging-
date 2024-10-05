# 网页打包客户端软件
使用Python和PyQt5开发的桌面应用程序，用于加载和显示指定的网页。<br>
我看网页上好多都是教程，没有一键打包的东西就很麻烦
所以说就做了这个

![image](https://github.com/user-attachments/assets/f923f32a-3a6b-4209-9f05-d14eb398b7da)
## 环境配置
* PyQt5==5.15.9
* PyQtWebEngine==5.15.6
* pyinstaller==5.13.0
## 修改位置
* **客户端名称位置 `app.py` 11行**<br>
* **网址更改位置在 `app.py` 18行**<br>
## 运行方法
**在线运行进入根目录**<br> `python app.py`
<br><br>
**打包方法**<br>
`pyinstaller --onefile --windowed --icon=resources/icon.ico app.py`
