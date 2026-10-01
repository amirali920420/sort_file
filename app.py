import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel
from untitled import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.selected_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        
        
        self.model = QFileSystemModel()
        self.model.setRootPath("C:/Users")
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index("C:/"))
        
        
        self.ui.treeView.clicked.connect(self.on_folder_selected)
        
        
        self.ui.selected_folder_getter = lambda: self.selected_folder

    def on_folder_selected(self, index):
        path = self.model.filePath(index)
        if os.path.isdir(path):
            self.selected_folder = path
            print(f"select folder: {path}")  

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())
