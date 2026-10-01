from PyQt5 import QtCore, QtGui, QtWidgets import os import shutil

class Ui_MainWindow(object):

def main(self):
       extensions_text = self.comboBox.currentText()
       extensions = tuple(ext.strip().strip('"') for ext in extensions_text.split(","))
       
       source_folder = self.selected_folder_getter()  
       folder_name = self.lineEdit.text()
       new_folder_path = os.path.join(source_folder, folder_name)
       os.makedirs(new_folder_path, exist_ok=True)

       for file in os.listdir(source_folder):
           if file.endswith(extensions):
               source_path = os.path.join(source_folder, file)
               shutil.move(source_path, new_folder_path)

       for file in os.listdir(source_folder):
           if file.endswith((extensions)):
               source_path = os.path.join(source_folder, file)
               shutil.move(source_path, new_folder_path)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 470, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 470, 31, 21))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 470, 81, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(240, 470, 301, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.clicked.connect(self.main)
        self.Run.setGeometry(QtCore.QRect(550, 460, 101, 41))
        self.Run.setObjectName("Run")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 0, 351, 461))
        self.treeView.setObjectName("treeView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

 def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "name folder :"))
        self.comboBox.setItemText(
            0,
            _translate(
                "MainWindow", '".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"'
            ),
        )
        self.comboBox.setItemText(
            1,
            _translate("MainWindow", '".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"'),
        )
        self.comboBox.setItemText(
            2,
            _translate("MainWindow", '".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"'),
        )
        self.comboBox.setItemText(
            3,
            _translate(
                "MainWindow", '".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"'
            ),
        )
        self.comboBox.setItemText(
            4, _translate("MainWindow", '".zip", ".rar", ".7z", ".tar", ".gz"')
        )
        self.comboBox.setItemText(
            5,
            _translate("MainWindow", '".py", ".js", ".html", ".css", ".java", ".cpp"'),
        )
        self.Run.setToolTip(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:24pt;">Run</span></p></body></html>',
            )
        )
        self.Run.setText(_translate("MainWindow", "Run"))``
