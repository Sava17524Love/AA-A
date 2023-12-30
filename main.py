from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

app = QApplication([])
win = QWidget()

win.setStyleSheet('background-color:#ABDCFF; font-size:24px; padding: 5px')
win.resize(1200, 700)
win.setWindowTitle('Easy Editor')

btn_dir = QPushButton('папка')
btn_dir.setCursor(Qt.PointingHandCursor)
btn_dir.setStyleSheet('border: 2px solid #708899; border-radius: 20px; backgroud-color:white')

lw_files = QListWidget()
btn_left = QPushButton('вліво')
btn_left.setCursor(Qt.PointingHandCursor)

btn_right = QPushButton('вправо')
btn_right.setCursor(Qt.PointingHandCursor)

btn_flip = QPushButton('Відзеркалить')
btn_flip.setCursor(Qt.PointingHandCursor)

btn_sharp = QPushButton('Різкість')
btn_sharp.setCursor(Qt.PointingHandCursor)

btn_bw = QPushButton('Ч/Б')
btn_bw.setCursor(Qt.PointingHandCursor)

lb_image = QLabel('Картинка')
row = QHBoxLayout()

col1 = QHBoxLayout()
col2 = QHBoxLayout()
col3 = QHBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)

col2.addWidget(lb_image)

col3.addWidget(btn_left)
col3.addWidget(btn_right)
col3.addWidget(btn_sharp)

row.addLayout(col1, 20)
row.addLayout(col2, 60)

win.setLayout(row)
win.show()
app.exec()
