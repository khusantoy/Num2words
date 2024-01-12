from num2words import num2words

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QTextEdit
)
from PyQt5 import QtCore


class Window(QWidget):

    def __init__(self) -> None:
        super().__init__()
        #window styles
        self.setWindowTitle("Numbers to words")
        self.setFixedSize(500, 400)
        self.setStyleSheet("""
            background-color:#2D3250;
            font-family:Arial;
        """)

        #layout
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.v_box = QVBoxLayout()

        #input
        self.input = QLineEdit(self)
        self.input.setFixedSize(300, 50)
        self.input.setPlaceholderText("Enter a number")
        self.input.setStyleSheet("""
            font-size: 30px;
            color: #597E52;
            background-color: #F1E4C3;
            border: 2px solid #fff;
            border-radius: 25px;
        """)
        self.input.setAlignment(QtCore.Qt.AlignCenter)

        #button
        self.button = QPushButton(self)
        self.button.setText("Convert")
        self.button.setFixedHeight(50)
        self.button.setStyleSheet("""
            QPushButton {
                color: #fff;
                background-color: #C6A969;
                font-size: 24px;
                border: 2px solid #fff;
                border-radius: 25px;
            }
            
            QPushButton:hover {
                background-color: #D9B87C;
            }
            QPushButton:pressed {
                background-color: #A68850;
            }
        """)

        #textarea
        self.textarea = QTextEdit(self)
        self.textarea.setFixedHeight(300)
        self.textarea.setStyleSheet("""
            font-size: 35px;
            color: #597E52;
            background-color: #F1E4C3;
            border: 2px solid #fff;
            border-radius: 25px;
        """)
        self.textarea.setAlignment(QtCore.Qt.AlignCenter)
        self.textarea.setLineWrapMode(QTextEdit.WidgetWidth)
        self.textarea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
        #creating layout
        self.h_box1.addWidget(self.input)
        self.h_box1.addWidget(self.button)
        self.h_box2.addWidget(self.textarea)

        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)

        self.setLayout(self.v_box)

        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        text = self.input.text()
        if text.isdigit():
            self.input.clear()
            text = num2words(text)
            self.textarea.setText(text)

app = QApplication([])
win = Window()
app.exec_()