import sys
import os
import shutil
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox

class SiOApp(QWidget):
    def __init__(self):
        super().__init__()
        self.path = ""
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('SiO')
        self.setFixedSize(400, 150)
        
        layout = QVBoxLayout()

        self.label = QLabel('No folder selected')
        layout.addWidget(self.label)

        self.btn_select = QPushButton('Select Folder')
        self.btn_select.clicked.connect(self.select)
        layout.addWidget(self.btn_select)

        self.btn_delete = QPushButton('Delete Completely')
        self.btn_delete.setEnabled(False)
        self.btn_delete.clicked.connect(self.delete)
        layout.addWidget(self.btn_delete)

        self.setLayout(layout)

    def select(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.path = folder
            self.label.setText(folder)
            self.btn_delete.setEnabled(True)

    def delete(self):
        if not os.path.exists(self.path):
            return
            
        reply = QMessageBox.question(self, 'Confirm', 'Delete this folder permanently?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                shutil.rmtree(self.path)
                QMessageBox.information(self, 'Success', 'Deleted successfully')
                self.path = ""
                self.label.setText('No folder selected')
                self.btn_delete.setEnabled(False)
            except Exception as e:
                QMessageBox.critical(self, 'Error', str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SiOApp()
    ex.show()
    sys.exit(app.exec())
