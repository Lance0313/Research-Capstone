from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import threading
import requests
import StartScreen
import sys
from Epayment import Ui_Epayment

# Define a function to fetch image asynchronously
def fetch_image(url, label):
    response = requests.get(url)
    if response.status_code == 200:
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
    else:
        label.setText("Image URL not found")

class Ui_Purchase(object):
    def setupUi(self, Purchase):
        self.products = {
            StartScreen.itemNames_1: {"quantity": StartScreen.quantity_1, "price": StartScreen.itemPrices_1},
            StartScreen.itemNames_2: {"quantity": StartScreen.quantity_2, "price": StartScreen.itemPrices_2},
            StartScreen.itemNames_3: {"quantity": StartScreen.quantity_3, "price": StartScreen.itemPrices_3},
            StartScreen.itemNames_4: {"quantity": StartScreen.quantity_4, "price": StartScreen.itemPrices_4},
            StartScreen.itemNames_5: {"quantity": StartScreen.quantity_5, "price": StartScreen.itemPrices_5},
            StartScreen.itemNames_6: {"quantity": StartScreen.quantity_6, "price": StartScreen.itemPrices_6},
            StartScreen.itemNames_7: {"quantity": StartScreen.quantity_7, "price": StartScreen.itemPrices_7},
            StartScreen.itemNames_8: {"quantity": StartScreen.quantity_8, "price": StartScreen.itemPrices_8},
            StartScreen.itemNames_9: {"quantity": StartScreen.quantity_9, "price": StartScreen.itemPrices_9},
            StartScreen.itemNames_0: {"quantity": StartScreen.quantity_0, "price": StartScreen.itemPrices_0},
        }

        self.cart = {}
        layout = QtWidgets.QVBoxLayout()
        for item_name in self.products:
            button = QtWidgets.QPushButton(item_name)
            button.clicked.connect(lambda _, name=item_name: self.addToCart(name))
            layout.addWidget(button)

        Purchase.setObjectName("Purchase")
        Purchase.resize(800, 480)
        Purchase.setStyleSheet("background-color: rgb(136, 202, 94);")
        Purchase.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(Purchase)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 450, 811, 41))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(290, 10, 231, 21))
        self.label_2.setStyleSheet("color: rgb(136, 202, 94);\n"
        "font: 75 6pt \"MS Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 811, 51))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.proceed_Button = QtWidgets.QPushButton(self.frame_2)
        self.proceed_Button.setGeometry(QtCore.QRect(660, 10, 131, 31))
        self.proceed_Button.setStyleSheet("\n"
        "font: 75 15pt \"MS Sans Serif\";\n"
        "border-radius: 10px; \n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(136, 202, 94);\n"
        "")
        self.proceed_Button.setObjectName("proceed_Button")
        self.proceed_Button.clicked.connect(self.ProceedToCartSummary)
        self.back_Button = QtWidgets.QPushButton(self.frame_2)
        self.back_Button.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.back_Button.setStyleSheet("\n"
        "font: 75 15pt \"MS Sans Serif\";\n"
        "border-radius: 10px; \n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(136, 202, 94);\n"
        "")
        self.back_Button.setObjectName("back_Button")
        self.back_Button.clicked.connect(self.BackToStart)
        self.CartButton = QtWidgets.QPushButton(self.frame_2)
        self.CartButton.setGeometry(QtCore.QRect(600, 0, 51, 51))
        self.CartButton.setStyleSheet("border: none;\n"
        "background-color: rgb(255, 255, 255);")
        self.CartButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/images/Cart.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CartButton.setIcon(icon)
        self.CartButton.setIconSize(QtCore.QSize(45, 45))
        self.CartButton.setObjectName("CartButton")
        self.CartButton.clicked.connect(self.HideCart)
        self.itemName_1 = QtWidgets.QLabel(self.centralwidget)
        self.itemName_1.setGeometry(QtCore.QRect(5, 60, 150, 13))
        self.itemName_1.setObjectName("itemName_1")
        self.itemName_1.setText(StartScreen.itemNames_1)
        self.itemName_1.setAlignment(Qt.AlignCenter)
        self.itemName_1.setStyleSheet("font:75 13px")
        self.itemPrice_1 = QtWidgets.QLabel(self.centralwidget)
        self.itemPrice_1.setGeometry(QtCore.QRect(60, 80, 47, 16))
        self.itemPrice_1.setObjectName("itemPrice_1")
        self.itemPrice_1.setAlignment(Qt.AlignCenter)
        self.itemPrice_1.setStyleSheet("font:75 13px")
        self.itemPrice_1.setText("Php "+ str(StartScreen.itemPrices_1))
        self.itemImage_1 = QtWidgets.QLabel(self.centralwidget)
        self.itemImage_1.setGeometry(QtCore.QRect(30, 100, 111, 111))
        self.itemImage_1.setText("")
        self.itemImage_1.setScaledContents(True)
        self.itemImage_1.setObjectName("itemImage_1")



        self.itemQuantity_1 = QtWidgets.QLabel(self.centralwidget)
        self.itemQuantity_1.setGeometry(QtCore.QRect(60, 220, 47, 13))
        self.itemQuantity_1.setObjectName("itemQuantity_1")
        self.itemQuantity_1.setAlignment(Qt.AlignCenter)
        self.itemName_2 = QtWidgets.QLabel(self.centralwidget)
        self.itemName_2.setGeometry(QtCore.QRect(155, 60, 150, 13))
        self.itemName_2.setObjectName("itemName_2")
        self.itemName_2.setText(StartScreen.itemNames_2)
        self.itemName_2.setAlignment(Qt.AlignCenter)
        self.itemName_2.setStyleSheet("font:75 13px")
        self.itemPrice_2 = QtWidgets.QLabel(self.centralwidget)
        self.itemPrice_2.setGeometry(QtCore.QRect(210, 80, 47, 13))
        self.itemPrice_2.setObjectName("itemPrice_2")
        self.itemPrice_2.setText("Php "+ str(StartScreen.itemPrices_2))
        self.itemImage_2 = QtWidgets.QLabel(self.centralwidget)
        self.itemImage_2.setGeometry(QtCore.QRect(180, 100, 111, 111))
        self.itemImage_2.setText("")
        
        self.itemImage_2.setScaledContents(True)
        self.itemImage_2.setObjectName("itemImage_2")


        self.itemQuantity_2 = QtWidgets.QLabel(self.centralwidget)
        self.itemQuantity_2.setGeometry(QtCore.QRect(210, 220, 47, 13))
        self.itemQuantity_2.setObjectName("itemQuantity_2")
        self.itemQuantity_2.setAlignment(Qt.AlignCenter)
        self.itemQuantity_3 = QtWidgets.QLabel(self.centralwidget)
        self.itemQuantity_3.setGeometry(QtCore.QRect(360, 220, 47, 13))
        self.itemQuantity_3.setObjectName("itemQuantity_3")
        self.itemQuantity_3.setAlignment(Qt.AlignCenter)
        self.itemName_3 = QtWidgets.QLabel(self.centralwidget)
        self.itemName_3.setGeometry(QtCore.QRect(320, 60, 150, 13))
        self.itemName_3.setObjectName("itemName_3")
        self.itemName_3.setText("Php "+ str(StartScreen.itemPrices_3))
        self.itemName_3.setAlignment(Qt.AlignCenter)
        self.itemName_3.setStyleSheet("font:75 13px")
        self.itemImage_3 = QtWidgets.QLabel(self.centralwidget)
        self.itemImage_3.setGeometry(QtCore.QRect(340, 100, 111, 111))
        self.itemImage_3.setText("")
        
        self.itemImage_3.setScaledContents(True)
        self.itemImage_3.setObjectName("itemImage_3")



        self.itemPrice_3 = QtWidgets.QLabel(self.centralwidget)
        self.itemPrice_3.setGeometry(QtCore.QRect(370, 80, 47, 13))
        self.itemPrice_3.setObjectName("itemPrice_3")
        self.itemPrice_3.setText("Php "+ str(StartScreen.itemPrices_3))
        self.itemQuantity_4 = QtWidgets.QLabel(self.centralwidget)
        self.itemQuantity_4.setGeometry(QtCore.QRect(520, 220, 47, 13))
        self.itemQuantity_4.setObjectName("itemQuantity_4")
        self.itemQuantity_4.setAlignment(Qt.AlignCenter)
        self.itemName_4 = QtWidgets.QLabel(self.centralwidget)
        self.itemName_4.setGeometry(QtCore.QRect(480, 60, 150, 13))
        self.itemName_4.setObjectName("itemName_4")
        self.itemName_4.setText("Php "+ str(StartScreen.itemPrices_4))
        self.itemName_4.setAlignment(Qt.AlignCenter)
        self.itemName_4.setStyleSheet("font:75 13px")
        self.itemImage_4 = QtWidgets.QLabel(self.centralwidget)
        self.itemImage_4.setGeometry(QtCore.QRect(490, 90, 111, 111))
        self.itemImage_4.setText("")
        
        self.itemImage_4.setScaledContents(True)
        self.itemImage_4.setObjectName("itemImage_4")



        self.itemPrice_4 = QtWidgets.QLabel(self.centralwidget)
        self.itemPrice_4.setGeometry(QtCore.QRect(520, 80, 150, 13))
        self.itemPrice_4.setObjectName("itemPrice_4")
        self.itemPrice_4.setText("Php "+ str(StartScreen.itemPrices_4))
        self.itemQuantity_5 = QtWidgets.QLabel(self.centralwidget)
        self.itemQuantity_5.setGeometry(QtCore.QRect(670, 220, 47, 13))
        self.itemQuantity_5.setObjectName("itemQuantity_5")
        self.itemQuantity_5.setAlignment(Qt.AlignCenter)
        self.itemName_5 = QtWidgets.QLabel(self.centralwidget)
        self.itemName_5.setGeometry(QtCore.QRect(625, 60, 150, 20))
        self.itemName_5.setObjectName("itemName_5")
        self.itemName_5.setText("Php "+ str(StartScreen.itemPrices_5))
        self.itemName_5.setAlignment(Qt.AlignCenter)
        self.itemName_5.setStyleSheet("font:75 13px")
        self.itemImage_5 = QtWidgets.QLabel(self.centralwidget)
        self.itemImage_5.setGeometry(QtCore.QRect(640, 100, 111, 111))
        self.itemImage_5.setText("")
        
        self.itemImage_5.setScaledContents(True)
        self.itemImage_5.setObjectName("itemImage_5")



        self.itemPrice_5 = QtWidgets.QLabel(self.centralwidget)
        self.itemPrice_5.setGeometry(QtCore.QRect(670, 80, 47, 13))
        self.itemPrice_5.setObjectName("itemPrice_5")
        self.itemPrice_5.setText("Php "+ str(StartScreen.itemPrices_5))
        self.itemQuantity_6 = QtWidgets.QLabel(self.centralwidget)
        self.itemQuantity_6.setGeometry(QtCore.QRect(60, 420, 47, 13))
        self.itemQuantity_6.setObjectName("itemQuantity_6")
        self.itemQuantity_6.setAlignment(Qt.AlignCenter)
        self.itemName_6 = QtWidgets.QLabel(self.centralwidget)
        self.itemName_6.setGeometry(QtCore.QRect(10, 260, 150, 13))
        self.itemName_6.setObjectName("itemName_6")
        self.itemName_6.setText("Php "+ str(StartScreen.itemPrices_6))
        self.itemName_6.setAlignment(Qt.AlignCenter)
        self.itemName_6.setStyleSheet("font:75 13px")
        self.itemImage_6 = QtWidgets.QLabel(self.centralwidget)
        self.itemImage_6.setGeometry(QtCore.QRect(30, 300, 111, 111))
        self.itemImage_6.setText("")
        
        self.itemImage_6.setScaledContents(True)
        self.itemImage_6.setObjectName("itemImage_6")



        self.itemPrice_6 = QtWidgets.QLabel(self.centralwidget)
        self.itemPrice_6.setGeometry(QtCore.QRect(60, 280, 47, 13))
        self.itemPrice_6.setObjectName("itemPrice_6")
        self.itemPrice_6.setText("Php "+ str(StartScreen.itemPrices_6))
        self.itemPrice_6.setAlignment(Qt.AlignCenter)
        self.itemQuantity_7 = QtWidgets.QLabel(self.centralwidget)
        self.itemQuantity_7.setGeometry(QtCore.QRect(210, 420, 47, 13))
        self.itemQuantity_7.setObjectName("itemQuantity_7")
        self.itemQuantity_7.setAlignment(Qt.AlignCenter)
        self.itemName_7 = QtWidgets.QLabel(self.centralwidget)
        self.itemName_7.setGeometry(QtCore.QRect(155, 260, 150, 13))
        self.itemName_7.setObjectName("itemName_7")
        self.itemName_7.setText("Php "+ str(StartScreen.itemPrices_7))
        self.itemName_7.setAlignment(Qt.AlignCenter)
        self.itemName_7.setStyleSheet("font:75 13px")
        self.itemImage_7 = QtWidgets.QLabel(self.centralwidget)
        self.itemImage_7.setGeometry(QtCore.QRect(180, 300, 111, 111))
        self.itemImage_7.setText("")
        
        self.itemImage_7.setScaledContents(True)
        self.itemImage_7.setObjectName("itemImage_7")


        self.itemPrice_7 = QtWidgets.QLabel(self.centralwidget)
        self.itemPrice_7.setGeometry(QtCore.QRect(210, 280, 47, 13))
        self.itemPrice_7.setObjectName("itemPrice_7")
        self.itemPrice_7.setText("Php "+ str(StartScreen.itemPrices_7))
        self.itemPrice_7.setAlignment(Qt.AlignCenter)
        self.itemQuantity_8 = QtWidgets.QLabel(self.centralwidget)
        self.itemQuantity_8.setGeometry(QtCore.QRect(370, 420, 47, 13))
        self.itemQuantity_8.setObjectName("itemQuantity_8")
        self.itemQuantity_8.setAlignment(Qt.AlignCenter)
        self.itemName_8 = QtWidgets.QLabel(self.centralwidget)
        self.itemName_8.setGeometry(QtCore.QRect(320, 260, 150, 13))
        self.itemName_8.setObjectName("itemName_8")
        self.itemName_8.setText("Php "+ str(StartScreen.itemPrices_8))
        self.itemName_8.setAlignment(Qt.AlignCenter)
        self.itemName_8.setStyleSheet("font:75 13px")
        self.itemImage_8 = QtWidgets.QLabel(self.centralwidget)
        self.itemImage_8.setGeometry(QtCore.QRect(340, 300, 111, 111))
        self.itemImage_8.setText("")
        
        self.itemImage_8.setScaledContents(True)
        self.itemImage_8.setObjectName("itemImage_8")



        self.itemPrice_8 = QtWidgets.QLabel(self.centralwidget)
        self.itemPrice_8.setGeometry(QtCore.QRect(370, 280, 47, 13))
        self.itemPrice_8.setObjectName("itemPrice_8")
        self.itemPrice_8.setText("Php "+ str(StartScreen.itemPrices_8))
        self.itemPrice_8.setAlignment(Qt.AlignCenter)
        self.itemQuantity_9 = QtWidgets.QLabel(self.centralwidget)
        self.itemQuantity_9.setGeometry(QtCore.QRect(530, 420, 47, 13))
        self.itemQuantity_9.setObjectName("itemQuantity_9")
        self.itemQuantity_9.setAlignment(Qt.AlignCenter)
        self.itemName_9 = QtWidgets.QLabel(self.centralwidget)
        self.itemName_9.setGeometry(QtCore.QRect(480, 260, 150, 13))
        self.itemName_9.setObjectName("itemName_9")
        self.itemName_9.setText("Php "+ str(StartScreen.itemPrices_9))
        self.itemName_9.setAlignment(Qt.AlignCenter)
        self.itemName_9.setStyleSheet("font:75 13px")
        self.itemImage_9 = QtWidgets.QLabel(self.centralwidget)
        self.itemImage_9.setGeometry(QtCore.QRect(500, 300, 111, 111))
        self.itemImage_9.setText("")
        
        self.itemImage_9.setScaledContents(True)
        self.itemImage_9.setObjectName("itemImage_9")



        self.itemPrice_9 = QtWidgets.QLabel(self.centralwidget)
        self.itemPrice_9.setGeometry(QtCore.QRect(530, 280, 47, 13))
        self.itemPrice_9.setObjectName("itemPrice_9")
        self.itemPrice_9.setText("Php "+ str(StartScreen.itemPrices_9))
        self.itemPrice_9.setAlignment(Qt.AlignCenter)
        self.itemQuantity_0 = QtWidgets.QLabel(self.centralwidget)
        self.itemQuantity_0.setGeometry(QtCore.QRect(670, 420, 47, 13))
        self.itemQuantity_0.setObjectName("itemQuantity_0")
        self.itemQuantity_0.setAlignment(Qt.AlignCenter)
        self.itemName_0 = QtWidgets.QLabel(self.centralwidget)
        self.itemName_0.setGeometry(QtCore.QRect(625, 260, 150, 13))
        self.itemName_0.setObjectName("itemName_0")
        self.itemName_0.setText("Php "+ str(StartScreen.itemPrices_0))
        self.itemName_0.setAlignment(Qt.AlignCenter)
        self.itemName_0.setStyleSheet("font:75 13px")
        self.itemImage_0 = QtWidgets.QLabel(self.centralwidget)
        self.itemImage_0.setGeometry(QtCore.QRect(640, 300, 111, 111))
        self.itemImage_0.setText("")
        
        self.itemImage_0.setScaledContents(True)
        self.itemImage_0.setObjectName("itemImage_0")

        for i in range(10):
            item_url = getattr(StartScreen, f"fileUrl_{i}", None)
            if item_url:
                label = getattr(self, f"itemImage_{i}")
                thread = threading.Thread(target=fetch_image, args=(item_url, label))
                thread.start()

        self.itemPrice_0 = QtWidgets.QLabel(self.centralwidget)
        self.itemPrice_0.setGeometry(QtCore.QRect(670, 280, 47, 13))
        self.itemPrice_0.setObjectName("itemPrice_0")
        self.itemPrice_0.setText("Php "+ str(StartScreen.itemPrices_0))
        self.itemPrice_0.setAlignment(Qt.AlignCenter)
        self.itemAdd_1 = QtWidgets.QPushButton(self.centralwidget)
        self.itemAdd_1.setGeometry(QtCore.QRect(120, 220, 21, 23))
        self.itemAdd_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/images/Plus.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.itemAdd_1.setIcon(icon1)
        self.itemAdd_1.setObjectName("itemAdd_1")
        self.itemAdd_1.clicked.connect(lambda _, num=1: self.addToCart(num))
        self.itemAdd_2 = QtWidgets.QPushButton(self.centralwidget)
        self.itemAdd_2.setGeometry(QtCore.QRect(270, 220, 21, 23))
        self.itemAdd_2.setText("")
        self.itemAdd_2.setIcon(icon1)
        self.itemAdd_2.setObjectName("itemAdd_2")
        self.itemAdd_2.clicked.connect(lambda _, num=2: self.addToCart(num))
        self.itemAdd_3 = QtWidgets.QPushButton(self.centralwidget)
        self.itemAdd_3.setGeometry(QtCore.QRect(430, 220, 21, 23))
        self.itemAdd_3.setText("")
        self.itemAdd_3.setIcon(icon1)
        self.itemAdd_3.setObjectName("itemAdd_3")
        self.itemAdd_3.clicked.connect(lambda _, num=3: self.addToCart(num))
        self.itemAdd_4 = QtWidgets.QPushButton(self.centralwidget)
        self.itemAdd_4.setGeometry(QtCore.QRect(580, 220, 21, 23))
        self.itemAdd_4.setText("")
        self.itemAdd_4.setIcon(icon1)
        self.itemAdd_4.setObjectName("itemAdd_4")
        self.itemAdd_4.clicked.connect(lambda _, num=4: self.addToCart(num))
        self.itemAdd_5 = QtWidgets.QPushButton(self.centralwidget)
        self.itemAdd_5.setGeometry(QtCore.QRect(730, 220, 21, 23))
        self.itemAdd_5.setText("")
        self.itemAdd_5.setIcon(icon1)
        self.itemAdd_5.setObjectName("itemAdd_5")
        self.itemAdd_5.clicked.connect(lambda _, num=5: self.addToCart(num))
        self.itemAdd_6 = QtWidgets.QPushButton(self.centralwidget)
        self.itemAdd_6.setGeometry(QtCore.QRect(120, 420, 21, 23))
        self.itemAdd_6.setText("")
        self.itemAdd_6.setIcon(icon1)
        self.itemAdd_6.setObjectName("itemAdd_6")
        self.itemAdd_6.clicked.connect(lambda _, num=6: self.addToCart(num))
        self.itemAdd_7 = QtWidgets.QPushButton(self.centralwidget)
        self.itemAdd_7.setGeometry(QtCore.QRect(270, 420, 21, 23))
        self.itemAdd_7.setText("")
        self.itemAdd_7.setIcon(icon1)
        self.itemAdd_7.setObjectName("itemAdd_7")
        self.itemAdd_7.clicked.connect(lambda _, num=7: self.addToCart(num))
        self.itemAdd_8 = QtWidgets.QPushButton(self.centralwidget)
        self.itemAdd_8.setGeometry(QtCore.QRect(430, 420, 21, 23))
        self.itemAdd_8.setText("")
        self.itemAdd_8.setIcon(icon1)
        self.itemAdd_8.setObjectName("itemAdd_8")
        self.itemAdd_8.clicked.connect(lambda _, num=8: self.addToCart(num))
        self.itemAdd_9 = QtWidgets.QPushButton(self.centralwidget)
        self.itemAdd_9.setGeometry(QtCore.QRect(590, 420, 21, 23))
        self.itemAdd_9.setText("")
        self.itemAdd_9.setIcon(icon1)
        self.itemAdd_9.setObjectName("itemAdd_9")
        self.itemAdd_9.clicked.connect(lambda _, num=9: self.addToCart(num))
        self.itemAdd_0 = QtWidgets.QPushButton(self.centralwidget)
        self.itemAdd_0.setGeometry(QtCore.QRect(730, 420, 21, 23))
        self.itemAdd_0.setText("")
        self.itemAdd_0.setIcon(icon1)
        self.itemAdd_0.setObjectName("itemAdd_0")
        self.itemAdd_0.clicked.connect(lambda _, num=0: self.addToCart(num))
        self.itemMinus_1 = QtWidgets.QPushButton(self.centralwidget)
        self.itemMinus_1.setGeometry(QtCore.QRect(30, 220, 21, 23))
        self.itemMinus_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/images/Minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.itemMinus_1.setIcon(icon2)
        self.itemMinus_1.setObjectName("itemMinus_1")
        self.itemMinus_1.clicked.connect(lambda _, num=1: self.subToCart(num))
        self.itemMinus_1.setEnabled(False)
        self.itemMinus_2 = QtWidgets.QPushButton(self.centralwidget)
        self.itemMinus_2.setGeometry(QtCore.QRect(180, 220, 21, 23))
        self.itemMinus_2.setText("")
        self.itemMinus_2.setIcon(icon2)
        self.itemMinus_2.setObjectName("itemMinus_2")
        self.itemMinus_2.clicked.connect(lambda _, num=2: self.subToCart(num))
        self.itemMinus_2.setEnabled(False)
        self.itemMinus_3 = QtWidgets.QPushButton(self.centralwidget)
        self.itemMinus_3.setGeometry(QtCore.QRect(340, 220, 21, 23))
        self.itemMinus_3.setText("")
        self.itemMinus_3.setIcon(icon2)
        self.itemMinus_3.setObjectName("itemMinus_3")
        self.itemMinus_3.clicked.connect(lambda _, num=3 : self.subToCart(num))
        self.itemMinus_3.setEnabled(False)
        self.itemMinus_4 = QtWidgets.QPushButton(self.centralwidget)
        self.itemMinus_4.setGeometry(QtCore.QRect(490, 220, 21, 23))
        self.itemMinus_4.setText("")
        self.itemMinus_4.setIcon(icon2)
        self.itemMinus_4.setObjectName("itemMinus_4")
        self.itemMinus_4.clicked.connect(lambda _, num=4 : self.subToCart(num))
        self.itemMinus_4.setEnabled(False)
        self.itemMinus_5 = QtWidgets.QPushButton(self.centralwidget)
        self.itemMinus_5.setGeometry(QtCore.QRect(640, 220, 21, 23))
        self.itemMinus_5.setText("")
        self.itemMinus_5.setIcon(icon2)
        self.itemMinus_5.setObjectName("itemMinus_5")
        self.itemMinus_5.clicked.connect(lambda _, num=5 : self.subToCart(num))
        self.itemMinus_5.setEnabled(False)
        self.itemMinus_6 = QtWidgets.QPushButton(self.centralwidget)
        self.itemMinus_6.setGeometry(QtCore.QRect(30, 420, 21, 23))
        self.itemMinus_6.setText("")
        self.itemMinus_6.setIcon(icon2)
        self.itemMinus_6.setObjectName("itemMinus_6")
        self.itemMinus_6.clicked.connect(lambda _, num=6 : self.subToCart(num))
        self.itemMinus_6.setEnabled(False)
        self.itemMinus_7 = QtWidgets.QPushButton(self.centralwidget)
        self.itemMinus_7.setGeometry(QtCore.QRect(180, 420, 21, 23))
        self.itemMinus_7.setText("")
        self.itemMinus_7.setIcon(icon2)
        self.itemMinus_7.setObjectName("itemMinus_7")
        self.itemMinus_7.clicked.connect(lambda _, num=7 : self.subToCart(num))
        self.itemMinus_7.setEnabled(False)
        self.itemMinus_8 = QtWidgets.QPushButton(self.centralwidget)
        self.itemMinus_8.setGeometry(QtCore.QRect(340, 420, 21, 23))
        self.itemMinus_8.setText("")
        self.itemMinus_8.setIcon(icon2)
        self.itemMinus_8.setObjectName("itemMinus_8")
        self.itemMinus_8.clicked.connect(lambda _, num=8 : self.subToCart(num))
        self.itemMinus_8.setEnabled(False)
        self.itemMinus_9 = QtWidgets.QPushButton(self.centralwidget)
        self.itemMinus_9.setGeometry(QtCore.QRect(500, 420, 21, 23))
        self.itemMinus_9.setText("")
        self.itemMinus_9.setIcon(icon2)
        self.itemMinus_9.setObjectName("itemMinus_9")
        self.itemMinus_9.clicked.connect(lambda _, num=9 : self.subToCart(num))
        self.itemMinus_9.setEnabled(False)
        self.itemMinus_0 = QtWidgets.QPushButton(self.centralwidget)
        self.itemMinus_0.setGeometry(QtCore.QRect(640, 420, 21, 23))
        self.itemMinus_0.setText("")
        self.itemMinus_0.setIcon(icon2)
        self.itemMinus_0.setObjectName("itemMinus_0")
        self.itemMinus_0.clicked.connect(lambda _, num=0 : self.subToCart(num))
        self.itemMinus_0.setEnabled(False)
        self.PurchaseCartframe = QtWidgets.QFrame(self.centralwidget)
        self.PurchaseCartframe.setGeometry(QtCore.QRect(0, 51, 281, 441))
        self.PurchaseCartframe.setStyleSheet("background-color: rgb(136, 202, 94);")
        self.PurchaseCartframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PurchaseCartframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PurchaseCartframe.setObjectName("PurchaseCartframe")
        self.PurchaseCartframe.setVisible(False)
        self.frame_3 = QtWidgets.QFrame(self.PurchaseCartframe)
        self.frame_3.setGeometry(QtCore.QRect(20, 60, 240, 351))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.PurchaseCartList = QtWidgets.QLabel(self.frame_3)
        self.PurchaseCartList.setGeometry(QtCore.QRect(10, 10, 221, 321))
        self.PurchaseCartList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PurchaseCartList.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PurchaseCartList.setStyleSheet("font: 75 12pt \"MS Sans Serif\";")
        self.PurchaseCartList.setObjectName("PurchaseCartList")
        self.ResetCartButton = QtWidgets.QPushButton(self.PurchaseCartList)
        self.ResetCartButton.setGeometry(QtCore.QRect(145, 285, 60, 20))
        self.ResetCartButton.setStyleSheet("font: 75 8pt \"MS Sans Serif\";\n"
        "border-radius: 5px; \n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(136, 202, 94);\n"
        "")
        self.ResetCartButton.setText("Reset")
        self.ResetCartButton.clicked.connect(self.ResetCart)
        self.TotalPrice = QtWidgets.QLabel(self.PurchaseCartList)
        self.TotalPrice.setGeometry(QtCore.QRect(5, 285, 100, 20))
        self.TotalPrice.setStyleSheet("font: 150 12pt \"MS Sans Serif\";")
        self.TotalPrice.setObjectName("PurchaseCartList")
        self.label_3 = QtWidgets.QLabel(self.PurchaseCartframe)
        self.label_3.setGeometry(QtCore.QRect(110, 20, 81, 21))
        self.label_3.setStyleSheet("font: 75 15pt \"MS Sans Serif\";\n"
        "color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        Purchase.setCentralWidget(self.centralwidget)
        self.ResetCart()

        # formatted_text = ""
        # for item in StartScreen.cartContent:
        #     name, quantity, price = item
        #     formatted_text += f"{name} = {quantity} = {'Php ' + str(price)}\n"

        #self.PurchaseCartList.setText(formatted_text)
        #self.PurchaseCartList.setAlignment(Qt.AlignTop)
        #self.TotalPrice.setText("Php ")
        # for i in range(10):
        #     getattr(self, f"itemQuantity_{i}").setText(str(getattr(StartScreen, f"quantity_{i}", 0)))
        
        # for i in range(10):
        #     print(getattr(StartScreen, f"quantity_{i}", 0))

        # for i in range(10):
        #     label = getattr(self, f"itemName_{i}")
        #     label.setText(str(getattr(StartScreen, f"itemNames_{i}", 0)))
        #     label.setAlignment(QtCore.Qt.AlignCenter)  # Set alignment to center
        #     label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)  # Allow label to expand horizontally


        self.retranslateUi(Purchase)
        QtCore.QMetaObject.connectSlotsByName(Purchase)

    def BuyingLimitError(self):
        StartScreen.ErrorDialogue = "Only 3 purchases per product is allowed in an instance"
        from ErrorDialogue import Ui_ErrorMessage
        self.error = QtWidgets.QMainWindow()
        self.ui = Ui_ErrorMessage()
        self.ui.setupUi(self.error)
        self.error.show()

        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Critical)
        # msg.setText("Only 3 purchases per product is allowed in an instance")
        # msg.setWindowTitle("Buying Policy")
        # msg.exec_()

    def StockError(self):
        StartScreen.ErrorDialogue = "No more stock is available"
        from ErrorDialogue import Ui_ErrorMessage
        self.error = QtWidgets.QMainWindow()
        self.ui = Ui_ErrorMessage()
        self.ui.setupUi(self.error)
        self.error.show()

        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Critical)
        # msg.setText("There is no more stock")
        # msg.setWindowTitle("Stock Limit Reached")
        # msg.exec_()

    ## Add Items to cart
    def addToCart(self, item_number):
        item_name = getattr(StartScreen, f"itemNames_{item_number}", None)
        if item_name is not None:
            if getattr(StartScreen, f"itemStock_{item_number}") == 0:
                    self.StockError()
                    getattr(self, f"itemAdd_{item_number}").setEnabled(False)
            else:
                if item_name in self.cart:
                        if getattr(StartScreen, f"itemStock_{item_number}") > self.cart[item_name]["quantity"]:
                            if self.cart[item_name]["quantity"] >= 3:
                                
                                self.BuyingLimitError()
                                getattr(self, f"itemAdd_{item_number}").setEnabled(False)
                            else:    
                                    self.cart[item_name]["quantity"] += 1
                        else:
                            self.StockError()
                            getattr(self, f"itemAdd_{item_number}").setEnabled(False)
                
                else:
                        self.cart[item_name] = {"quantity": 1, "price": self.products[item_name]["price"]}

                setattr(StartScreen, f"quantity_{item_number}",  self.cart[item_name]["quantity"])
                self.updateCartLabel()
                print(f"Adding {item_name} to cart", getattr(StartScreen, f"quantity_{item_number}"))
                getattr(self, f"itemMinus_{item_number}").setEnabled(True)
        else:
            print(f"Item with number {item_number} not found")
    ## Add Items to cart

    ##Subtract Items to cart
    def subToCart(self, item_number):
        item_name = getattr(StartScreen, f"itemNames_{item_number}", None)
        if item_name is not None:
            if item_name in self.cart:
                self.cart[item_name]["quantity"] -= 1
                getattr(self, f"itemAdd_{item_number}").setEnabled(True)
                if self.cart[item_name]["quantity"] == 0:
                    del self.cart[item_name]  # Remove item if its quantity becomes 0
                    getattr(self, f"itemMinus_{item_number}").setEnabled(False)
                else:
                    getattr(self, f"itemMinus_{item_number}").setEnabled(True)
            else:
                # If item not in cart, add it
                self.cart[item_name] = {"quantity": 1, "price": self.products[item_name]["price"]}
                getattr(self, f"itemMinus_{item_number}").setEnabled(True)

            # Update quantity display and cart label

            try:
                setattr(StartScreen, f"quantity_{item_number}", self.cart[item_name]["quantity"])

            except:
                setattr(StartScreen, f"quantity_{item_number}", 0)

            print(f"Quantity {item_name}: {getattr(StartScreen, f'quantity_{item_number}')}")
            self.updateCartLabel()  # Update the cart label after modifying the cart
        else:
            print(f"Item with number {item_number} not found")

    ##Update the Cart List
    def updateCartLabel(self):
        cart_text = ""
        accumulated_price = 0
        for item_name, item_info in self.cart.items():
            cart_text += f"{item_name} = {item_info['quantity']} = Php {item_info['quantity']*item_info['price']}\n"
            accumulated_price += item_info['quantity'] * item_info['price']

        if cart_text == "":
            # If cart is empty, reset the label
            self.PurchaseCartList.setText("")
        else:
            # If cart is not empty, update the label
            self.PurchaseCartList.setText(cart_text)

        self.PurchaseCartList.setAlignment(Qt.AlignTop)
        total_price = sum(getattr(StartScreen, f"quantity_{i}") * getattr(StartScreen, f"itemPrices_{i}") for i in range(len(self.products)))
        self.TotalPrice.setText("Php " + str(total_price))
        for i in range(10):
            getattr(self, f"itemQuantity_{i}").setText(str(getattr(StartScreen, f"quantity_{i}", 0)))
    ##Update the Cart List

    def getTotalPrice(self):
        sum = 0
        for i in range(10):
           sum += getattr(StartScreen, f"quantity_{i}") * getattr(StartScreen, f"itemPrices_{i}")
        print(StartScreen.itemPrices_1)
        return sum
    
    ##Get data from cart
    def getCartContents(self):
        cart_contents = []
        total_price = 0
        cart_text = self.PurchaseCartList.text()
        lines = cart_text.split('\n')
        for line in lines:
            parts = line.split('=')
            if len(parts) == 3:
                prod_name = parts[0].strip()
                prod_quantity = int(parts[1].strip())
                prod_price = float(parts[2].strip().replace('Php', ''))
                cart_contents.append((prod_name, prod_quantity, prod_price))
                total_price = self.getTotalPrice()
        return cart_contents, total_price
    ##Get data from cart

    ##Navigation functions
    def ProceedToCartSummary(self):
        from CartSummary import Ui_CartSummary
        cart_contents, total_price = self.getCartContents()
        if not cart_contents:
            self.show_error_message()
            return
        StartScreen.cartContent = cart_contents
        StartScreen.totalPrice = total_price
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CartSummary()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
        self.centralwidget.window().close()
    
    def show_error_message(self):
        StartScreen.ErrorDialogue = "Cart is empty! \nPlease add an item/items to proceed."
        from ErrorDialogue import Ui_ErrorMessage
        self.error = QtWidgets.QMainWindow()
        self.ui = Ui_ErrorMessage()
        self.ui.setupUi(self.error)
        self.error.show()
        # error_box = QtWidgets.QMessageBox()
        # error_box.setIcon(QtWidgets.QMessageBox.Critical)
        # error_box.setText("Please add an item/items to proceed.")
        # error_box.setWindowTitle("Cart is empty!")
        # error_box.exec_()
        
    def BackToStart(self):
        from StartScreen import Ui_StartScreen
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_StartScreen()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
        self.centralwidget.window().close()
    ##Navigation functions

    ##Reset Cart
    def ResetCart(self):
        self.cart = {}
        self.PurchaseCartList.setText("")
        self.TotalPrice.setText("")
        for i in range(10):  # Range from 0 to 9
            getattr(self, f"itemMinus_{i}").setEnabled(False)
        for i in range(10):  # Range from 0 to 9
            getattr(self, f"itemAdd_{i}").setEnabled(True)
        for i in range(10):
            setattr(StartScreen, f"quantity_{i}", 0)
        for i in range(10):
            getattr(self, f"itemQuantity_{i}").setText(str(getattr(StartScreen, f"quantity_{i}")))
    ##Reset Cart

    def retranslateUi(self, Purchase):
        _translate = QtCore.QCoreApplication.translate
        Purchase.setWindowTitle(_translate("Purchase", "MainWindow"))
        self.label_2.setText(_translate("Purchase", "© 2024 LMMN, Inc. All rights reserved"))
        self.proceed_Button.setText(_translate("Purchase", "Proceed"))
        self.back_Button.setText(_translate("Purchase", "Back"))
        self.label_3.setText(_translate("Purchase", "CART"))

    def HideCart(self):
        self.PurchaseCartframe.setVisible(not self.PurchaseCartframe.isVisible())
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Purchase = QtWidgets.QMainWindow()
    ui = Ui_Purchase()
    ui.setupUi(Purchase)
    Purchase.showFullScreen()
    sys.exit(app.exec_())
