from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QTimer
import firebase_admin 
from firebase_admin import credentials, db
import sys
import os

## Database Insert
if not firebase_admin._apps:
    cred = credentials.Certificate("keywords-e2507-firebase-adminsdk-ruto8-cc3abd39a8.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://keywords-e2507-default-rtdb.firebaseio.com/'
    })
    print("Firebase initialized successfully.")


def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("keywords-e2507-firebase-adminsdk-ruto8-cc3abd39a8.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://keywords-e2507-default-rtdb.firebaseio.com/'
        })
        print("Firebase initialized successfully.")
## Database Insert

## Database Variables
vmdata_1 = db.reference("VendingMachine/01").get()
vmdata_2 = db.reference("VendingMachine/02").get()
vmdata_3 = db.reference("VendingMachine/03").get()
vmdata_4 = db.reference("VendingMachine/04").get()
vmdata_5 = db.reference("VendingMachine/05").get()
vmdata_6 = db.reference("VendingMachine/06").get()
vmdata_7 = db.reference("VendingMachine/07").get()
vmdata_8 = db.reference("VendingMachine/08").get()
vmdata_9 = db.reference("VendingMachine/09").get()
vmdata_0 = db.reference("VendingMachine/10").get()
fileUrl_1 = vmdata_1.get("fileUrl")
fileUrl_2 = vmdata_2.get("fileUrl")
fileUrl_3 = vmdata_3.get("fileUrl")
fileUrl_4 = vmdata_4.get("fileUrl")
fileUrl_5 = vmdata_5.get("fileUrl")
fileUrl_6 = vmdata_6.get("fileUrl")
fileUrl_7 = vmdata_7.get("fileUrl")
fileUrl_8 = vmdata_8.get("fileUrl")
fileUrl_9 = vmdata_9.get("fileUrl")
fileUrl_0 = vmdata_0.get("fileUrl")
itemNames_1 = vmdata_1.get("itemName")
itemNames_2 = vmdata_2.get("itemName")
itemNames_3 = vmdata_3.get("itemName")
itemNames_4 = vmdata_4.get("itemName")
itemNames_5 = vmdata_5.get("itemName")
itemNames_6 = vmdata_6.get("itemName")
itemNames_7 = vmdata_7.get("itemName")
itemNames_8 = vmdata_8.get("itemName")
itemNames_9 = vmdata_9.get("itemName")
itemNames_0 = vmdata_0.get("itemName")
itemPrices_1 = int(vmdata_1.get("itemPrice", 0))
itemPrices_2 = int(vmdata_2.get("itemPrice", 0))
itemPrices_3 = int(vmdata_3.get("itemPrice", 0))
itemPrices_4 = int(vmdata_4.get("itemPrice", 0))
itemPrices_5 = int(vmdata_5.get("itemPrice", 0))
itemPrices_6 = int(vmdata_6.get("itemPrice", 0))
itemPrices_7 = int(vmdata_7.get("itemPrice", 0))
itemPrices_8 = int(vmdata_8.get("itemPrice", 0))
itemPrices_9 = int(vmdata_9.get("itemPrice", 0))
itemPrices_0 = int(vmdata_0.get("itemPrice", 0))
itemStock_1 = int(vmdata_1.get("itemStock", 0))
itemStock_2 = int(vmdata_2.get("itemStock", 0))
itemStock_3 = int(vmdata_3.get("itemStock", 0))
itemStock_4 = int(vmdata_4.get("itemStock", 0))
itemStock_5 = int(vmdata_5.get("itemStock", 0))
itemStock_6 = int(vmdata_6.get("itemStock", 0))
itemStock_7 = int(vmdata_7.get("itemStock", 0))
itemStock_8 = int(vmdata_8.get("itemStock", 0))
itemStock_9 = int(vmdata_9.get("itemStock", 0))
itemStock_0 = int(vmdata_0.get("itemStock", 0))
cdata = db.reference("Sukli/01").get()
moneyChangeAvailable = cdata.get("available")
#print(moneyChangeAvailable)
## Database Variables

## Global Variables
global cartContent
global totalPrice
global moneyChange
global quantity_1
global quantity_2
global quantity_3
global quantity_4
global quantity_5
global quantity_6
global quantity_7
global quantity_8
global quantity_9
global quantity_0
cartContent = []
totalPrice = 0
moneyChange = 0
quantity_1 = 0
quantity_2 = 0
quantity_3 = 0
quantity_4 = 0
quantity_5 = 0
quantity_6 = 0
quantity_7 = 0
quantity_8 = 0
quantity_9 = 0
quantity_0 = 0
ErrorDialogue = ""
## Global Variables

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 480)
        if sys.platform == 'linux':
            self.setWindowFlags(Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.label_animation = QLabel(self)
        self.label_animation.setGeometry(0, 0, 800, 480)
        self.label_animation.setScaledContents(True)
        current_directory = os.getcwd()
        image_path = os.path.join(current_directory, "Resources", "images", "Loading.gif")
        self.movie = QMovie(image_path)
        self.label_animation.setMovie(self.movie)

        timer = QTimer(self)
        self.startAnimation()
        timer.singleShot(6000, self.stopAnimation)

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()

class Ui_StartScreen(object):
    def setupUi(self, StartScreen):
        self.clear_cart()
        self.clearQuantities()
        StartScreen.setObjectName("StartScreen")
        StartScreen.resize(800, 480)
        StartScreen.setStyleSheet("background-color: rgb(136, 202, 94);")
        StartScreen.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(StartScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 430, 811, 51))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(280, 14, 301, 21))
        self.label.setStyleSheet("color: rgb(136, 202, 94);\n"
        "font: 75 10pt \"MS Sans Serif\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 80, 461, 111))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 75 130pt \"MS Sans Serif\";\n"
        "")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Resources/images/SMART.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.PurchaseButton = QtWidgets.QPushButton(self.centralwidget)
        self.PurchaseButton.setGeometry(QtCore.QRect(50, 320, 171, 41))
        self.PurchaseButton.setStyleSheet("color: rgb(136, 202, 94);\n"
        "font: 15pt \"MS Sans Serif\";\n"
        "border-radius: 10px;\n"
        "\n"
        "background-color: rgb(255, 255, 255);")
        self.PurchaseButton.setObjectName("PurchaseButton")
        self.SuggestionButton = QtWidgets.QPushButton(self.centralwidget)
        self.SuggestionButton.setGeometry(QtCore.QRect(280, 320, 171, 41))
        self.SuggestionButton.setStyleSheet("color: rgb(136, 202, 94);\n"
        "font: 75 15pt \"MS Sans Serif\";\n"
        "border-radius: 10px; \n"
        "background-color: rgb(255, 255, 255);")
        self.SuggestionButton.setObjectName("SuggestionButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 190, 461, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Resources/images/Pharmakeutical Kiosk.png"))
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 260, 451, 41))
        self.label_5.setStyleSheet("font: 75 12pt \"MS Sans Serif\";\n"
        "color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, -30, 481, 511))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Resources/images/MedicineStart.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.frame.raise_()
        self.PurchaseButton.raise_()
        self.SuggestionButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        StartScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartScreen)
        QtCore.QMetaObject.connectSlotsByName(StartScreen)

    def retranslateUi(self, StartScreen):
        _translate = QtCore.QCoreApplication.translate
        StartScreen.setWindowTitle(_translate("StartScreen", "MainWindow"))
        self.label.setText(_translate("StartScreen", "© 2024 LMMN, Inc. All rights reserved"))
        self.PurchaseButton.setText(_translate("StartScreen", "Purchase"))
        self.PurchaseButton.clicked.connect(self.ProceedToPurchase)
        self.SuggestionButton.setText(_translate("StartScreen", "Suggestion"))
        self.SuggestionButton.clicked.connect(self.ProceedToSuggestion)
        self.label_5.setText(_translate("StartScreen", "Streamlined Over-the-Counter Medicine Dispensing Innovation\n"""))
    
    ## Clear cartlist
    def clear_cart(self):
        self.cartContent = []
        print(cartContent)

    def clearQuantities(self):
        for i in range(10):
            setattr(self, f"quantity_{i}", 0)
    ## Clear cartlist

    ## Navigation Functions
    def ProceedToPurchase(self):
        initialize_firebase()
        from Purchase import Ui_Purchase
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Purchase()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
        self.loading = LoadingScreen()
        self.loading.showFullScreen()
        self.centralwidget.window().close()
    
    def ProceedToSuggestion(self):
        initialize_firebase()
        from SuggestionQuery import Ui_SuggestionQuery
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SuggestionQuery()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
        self.centralwidget.window().close()
    ## Navigation Functions

if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartScreen = QtWidgets.QMainWindow()
    ui = Ui_StartScreen()
    ui.setupUi(StartScreen)
    StartScreen.showFullScreen() 
    sys.exit(app.exec_())
