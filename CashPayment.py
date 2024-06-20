from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QMessageBox, QWidget, QLabel
from PyQt5.QtGui import QMovie
import StartScreen
import serial 
import os
import time
# from gpiozero import LED

# relayA = LED(17)
# relayB = LED(27)

# def open_relay():
#     relayA.on()
#     relayB.on()

# def close_relay():
#     relayA.off()
#     relayB.off()

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 480)
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

class Ui_CashPayment(object):
    def setupUi(self, CashPayment):
        # open_relay()
        self.inserted1 = 0
        self.inserted2 = 0
        self.totalInserted = 0
        CashPayment.setObjectName("CashPayment")
        CashPayment.resize(800, 480)
        CashPayment.setStyleSheet("background-color: rgb(136, 202, 94);")
        CashPayment.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(CashPayment)
        self.centralwidget.setObjectName("centralwidget")
        self.proceed_Button = QtWidgets.QPushButton(self.centralwidget)
        self.proceed_Button.setGeometry(QtCore.QRect(650, 390, 131, 31))
        self.proceed_Button.setStyleSheet("\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"border-radius: 10px; \n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(136, 202, 94);")
        self.proceed_Button.setObjectName("proceed_Button")
        self.proceed_Button.clicked.connect(self.ProceedToThankYou)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 70, 511, 41))
        self.label_3.setStyleSheet("font: 75 10pt \"MS Sans Serif\";\n"
        "color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(240, 110, 311, 51))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 151, 16))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.TotalPrice = QtWidgets.QLabel(self.frame_3)
        self.TotalPrice.setGeometry(QtCore.QRect(240, 20, 31, 16))
        self.TotalPrice.setStyleSheet("color: rgb(255, 0, 0);")
        self.TotalPrice.setObjectName("TotalPrice")
        self.TotalPrice.setText(str(StartScreen.totalPrice))
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 430, 811, 51))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(280, 14, 301, 21))
        self.label.setStyleSheet("color: rgb(136, 202, 94);\n"
        "font: 75 6pt \"MS Sans Serif\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 40, 371, 41))
        self.label_2.setStyleSheet("font: 75 19pt \"MS Sans Serif\";\n"
        "color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.back_Button = QtWidgets.QPushButton(self.centralwidget)
        self.back_Button.setGeometry(QtCore.QRect(10, 20, 131, 31))
        self.back_Button.setStyleSheet("font: 75 15pt \"MS Sans Serif\";\n"
        "border-radius: 10px; \n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(136, 202, 94);")
        self.back_Button.setObjectName("back_Button")
        self.back_Button.clicked.connect(self.BackToCartSummary)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(240, 170, 311, 221))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(30, 190, 151, 16))
        self.label_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.amounInserted = QtWidgets.QLabel(self.frame_2)
        self.amounInserted.setGeometry(QtCore.QRect(240, 190, 31, 16))
        self.amounInserted.setStyleSheet("color: rgb(255, 0, 0);")
        self.amounInserted.setObjectName("amounInserted")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(0, -60, 311, 311))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Resources/images/cash_blue ins.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.label_8.raise_()
        self.amounInserted.raise_()
        CashPayment.setCentralWidget(self.centralwidget)

        self.retranslateUi(CashPayment)
        QtCore.QMetaObject.connectSlotsByName(CashPayment)
        self.timer = QTimer()
        self.timer.timeout.connect(self.updatePaymentInfo)
        self.timer.start(250)  # Update every 250 milliseconds

        #self.serial1 = serial.Serial('/dev/ttyUSB1', 9600)
        #self.serial1.flush()

        #self.serial2 = serial.Serial('/dev/ttyUSB2', 9600)  # Change 'COM8' to the port of Arduino 2
        #self.serial2.flush()
        
        try:
            self.serial1 = serial.Serial('/dev/ttyUSB1', 9600)
            self.serial1.flush()
        except serial.SerialException as e:
            print("Error opening serial port 1:", e)
            self.serial1 = None

        try:
            self.serial2 = serial.Serial('/dev/ttyUSB2', 9600)
            self.serial2.flush()
        except serial.SerialException as e:
            print("Error opening serial port 2:", e)
            self.serial2 = None

    #def updatePaymentInfo(self):
        #if self.serial1.in_waiting > 0:
            #amount = int(self.serial1.readline().strip())
            #self.inserted1 = amount
            #print("A: ", self.inserted1 )
            # Update UI or perform any other actions

        # For Arduino 2
        #if self.serial2.in_waiting > 0:
            #amount = int(self.serial2.readline().strip())
            #self.inserted2 = amount
            #print("B: ", self.inserted2)
        #self.totalInserted = self.inserted1 + self.inserted2
        #self.amounInserted.setText(str(self.totalInserted))
        #print(self.totalInserted)
    
    def close_serial_connection(self):
        if self.serial1 is not None:
            self.serial1.close()
            print("Serial connection 1 closed.")
        else:
            print("Serial connection 1 is already closed or not initialized.")

        if self.serial2 is not None:
            self.serial2.close()
            print("Serial connection 2 closed.")
        else:
            print("Serial connection 2 is already closed or not initialized.")


    def updatePaymentInfo(self):
        if self.serial1 is not None and self.serial1.isOpen() and self.serial1.in_waiting > 0:
            amount = int(self.serial1.readline().strip())
            self.inserted1 = amount
            print("A: ", self.inserted1)
            # Update UI or perform any other actions

        if self.serial2 is not None and self.serial2.isOpen() and self.serial2.in_waiting > 0:
            amount = int(self.serial2.readline().strip())
            self.inserted2 = amount
            print("B: ", self.inserted2)

        self.totalInserted = self.inserted1 + self.inserted2
        self.amounInserted.setText(str(self.totalInserted))
        print(self.totalInserted)


    def PaymentChecking(message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Pay more!")
        msg.setWindowTitle("Insufficient Amount")
        msg.exec_()

    def retranslateUi(self, CashPayment):
        _translate = QtCore.QCoreApplication.translate
        CashPayment.setWindowTitle(_translate("CashPayment", "MainWindow"))
        self.proceed_Button.setText(_translate("CashPayment", "Proceed"))
        self.label_3.setText(_translate("CashPayment", "Please insert the coin/s and bill/s on their respective slots"))
        self.label_5.setText(_translate("CashPayment", "Total Amount to be Paid"))
        self.label.setText(_translate("CashPayment", "© 2024 LMMN, Inc. All rights reserved"))
        self.label_2.setText(_translate("CashPayment", "Payment Method: Cash"))
        self.back_Button.setText(_translate("CashPayment", "Back"))
        self.label_8.setText(_translate("CashPayment", "Total Amount Inserted"))

    def stopTimer(self):
        self.timer.stop()

    def BackToCartSummary(self):
        from CartSummary import Ui_CartSummary
        self.stopTimer()
        self.close_serial_connection()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CartSummary()
        self.ui.setupUi(self.window)
        # close_relay()
        self.centralwidget.window().close()
        self.window.showFullScreen()
    
    def ProceedToThankYou(self):
        if StartScreen.totalPrice <= self.totalInserted:
            from ThankYou import Ui_ThankYou
            StartScreen.moneyChange = (self.totalInserted - StartScreen.totalPrice)
            print("Change is: " + str(StartScreen.moneyChange))
            self.close_serial_connection()
            self.loading = LoadingScreen()
            self.loading.showFullScreen()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ThankYou()
            self.ui.setupUi(self.window)
            # close_relay()
            self.window.showFullScreen()
            self.centralwidget.window().close()
        else:
            self.PaymentChecking()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CashPayment = QtWidgets.QMainWindow()
    ui = Ui_CashPayment()
    ui.setupUi(CashPayment)
    CashPayment.showFullScreen()
    sys.exit(app.exec_())
