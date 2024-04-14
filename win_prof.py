import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QFrame, QPushButton, QTreeWidget, QTreeWidgetItem
from PyQt5 import QtGui

# Окно настроек
class Window2(QMainWindow):
    def __init__(self, window_title):
        super().__init__()
        self.setWindowTitle(window_title)
        self.setGeometry(200, 200, 800, 600)
        self.setStyleSheet("""
            background-color: #222;
            color: #fff;
            border: 2px solid #555;
            border-radius: 10px;
        """)