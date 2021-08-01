
import numpy as np
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QFormLayout, QPushButton
from cv2 import *

import math
import numpy as np

import requests
import json

from random import randint
import messages

class Window(QWidget):

    def getNewNum(self):
        image = getImage()
        self.imageCaptureLabel2.setText("successful")
        print(image.shape[0])

        response_API = requests.get('https://complimentr.com/api')
        data = response_API.text
        parse_json = json.loads(data)

        randCompliment = parse_json["compliment"]

        # randCompliment = messages.compliments[randint(0, len(messages.compliments))]

        self.imageCaptureLabel2.setText(randCompliment)

        print("done1")

        self.pixmap = QPixmap("images/filename.jpg")
        self.pictureLabel.setPixmap(self.pixmap)

        print("done2")

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selfie Booth")
        self.setGeometry(100, 100, 400, 100)
        self.move(400, 200)
        # Create a QFormLayout instance
        layout = QFormLayout()
        # Add widgets to the layout

        self.imageCaptureLabel1 = QLabel("Comment:")
        self.imageCaptureLabel2 = QLabel("none")
        self.imageCaptureLabel1.setFont(QFont('Arial', 10))
        self.imageCaptureLabel2.setFont(QFont('Arial', 10))
        layout.addRow(self.imageCaptureLabel1, self.imageCaptureLabel2)


        self.randNumLabel1 = QLabel("Take a selfie!")
        # self.randNumLabel2 = QLabel("?")
        # self.randNumLabel2.setFont(QFont('Arial', 10))
        self.randNumLabel1.setFont(QFont('Arial', 10))
        # self.nameLabel2.setWordWrap(True)
        # layout.addRow(self.randNumLabel1, self.randNumLabel2)
        layout.addRow(self.randNumLabel1)

        self.pictureLabel = QLabel()
        self.pixmap = QPixmap("images/placeholder.jpg")
        self.pictureLabel.setPixmap(self.pixmap)
        self.pictureLabel.setScaledContents(True)
        # self.pictureLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        layout.addRow(self.pictureLabel)


        button = QPushButton('Take selfie!')
        button.setToolTip('Click to take a selfie!')
        button.move(100, 70)
        button.clicked.connect(self.getNewNum)
        layout.addRow(button)

        # Set the layout on the application's window
        self.setLayout(layout)



def getImage():
    # initialize the camera
    cam = VideoCapture(0)  # 0 -> index of camera

    img = np.zeros((100, 100, 3), np.uint8)
    s, img = cam.read()
    if s:  # frame captured without any errors
        imwrite("images/filename.jpg", img)  # save image

    return img


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


