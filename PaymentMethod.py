from PyQt5 import QtCore, QtGui, QtWidgets
import StartScreen


class Ui_PaymentMethod(object):
    def setupUi(self, PaymentMethod):
        PaymentMethod.setObjectName("PaymentMethod")
        PaymentMethod.resize(800, 480)
        PaymentMethod.setStyleSheet("background-color: rgb(136, 202, 94);")
        PaymentMethod.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(PaymentMethod)
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
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(110, 150, 251, 211))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.CashButton = QtWidgets.QLabel(self.frame_2)
        self.CashButton.setGeometry(QtCore.QRect(-70, -100, 391, 411))
        self.CashButton.setText("")
        self.CashButton.setPixmap(QtGui.QPixmap("Resources/images/method_pesos.png"))
        self.CashButton.setScaledContents(True)
        self.CashButton.setObjectName("CashButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 371, 41))
        self.label_2.setStyleSheet("font: 75 19pt \"MS Sans Serif\";\n"
        "color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.back_Button = QtWidgets.QPushButton(self.centralwidget)
        self.back_Button.setGeometry(QtCore.QRect(10, 20, 131, 31))
        self.back_Button.setStyleSheet("font: 75 12pt \"MS Sans Serif\";\n"
        "border-radius: 10px; \n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(136, 202, 94);")
        self.back_Button.setObjectName("back_Button")
        self.back_Button.clicked.connect(self.BackToCartSummary)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 70, 241, 41))
        self.label_3.setStyleSheet("font: 75 10pt \"MS Sans Serif\";\n"
        "color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(430, 150, 251, 211))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.EcashButton = QtWidgets.QLabel(self.frame_3)
        self.EcashButton.setGeometry(QtCore.QRect(-50, -70, 351, 351))
        self.EcashButton.setText("")
        self.EcashButton.setPixmap(QtGui.QPixmap("Resources/images/method_ecash.png"))
        self.EcashButton.setScaledContents(True)
        self.EcashButton.setObjectName("EcashButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 360, 261, 41))
        self.label_6.setStyleSheet("font: 75 10pt \"MS Sans Serif\";\n"
        "color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 370, 161, 41))
        self.label_7.setStyleSheet("font: 75 10pt \"MS Sans Serif\";\n"
        "color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(220, 110, 491, 41))
        self.label_8.setStyleSheet("font: 75 10pt \"MS Sans Serif\";\n"
        "color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.PayCashButton = QtWidgets.QPushButton(self.CashButton)
        self.PayCashButton.setGeometry(QtCore.QRect(70, 70, 321, 361))
        self.PayCashButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""border-width:0px;\n"
        "border-thickness: 0px;\n"
        "border-radius:20px;\n"
        "")
        self.PayCashButton.setObjectName("PayCashButton")
        self.PayCashButton.clicked.connect(self.PayCash)
        self.PayeCashButton = QtWidgets.QPushButton(self.centralwidget)
        self.PayeCashButton.setGeometry(QtCore.QRect(400, 60, 321, 361))
        self.PayeCashButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""border-width:0px;\n"
        "border-thickness: 0px;\n"
        "border-radius:20px;\n"
        "")
        self.PayeCashButton.setObjectName("PayeCashButton")
        self.PayeCashButton.clicked.connect(self.PayeCash)
        
        self.frame.raise_()
        self.frame_2.raise_()
        self.label_2.raise_()
        self.back_Button.raise_()
        self.label_3.raise_()
        self.frame_3.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.PayeCashButton.raise_()
        self.PayCashButton.raise_()
        
        PaymentMethod.setCentralWidget(self.centralwidget)

        self.retranslateUi(PaymentMethod)
        QtCore.QMetaObject.connectSlotsByName(PaymentMethod)

    def PayCash(self):
        from ChangeNotice import Ui_ChangeNotice
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ChangeNotice()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
        self.centralwidget.window().close()
        
    def PayeCash(self, cartContent):
        from Epayment import Ui_Epayment
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Epayment()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
        self.centralwidget.window().close()

    def BackToCartSummary(self):
        from CartSummary import Ui_CartSummary
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CartSummary()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
        self.centralwidget.window().close()
        
    def retranslateUi(self, PaymentMethod):
        _translate = QtCore.QCoreApplication.translate
        PaymentMethod.setWindowTitle(_translate("PaymentMethod", "MainWindow"))
        self.label.setText(_translate("PaymentMethod", "© 2024 LMMN, Inc. All rights reserved"))
        self.label_2.setText(_translate("PaymentMethod", "Choose a payment method"))
        self.back_Button.setText(_translate("PaymentMethod", "Back"))
        self.label_3.setText(_translate("PaymentMethod", "(Select one of the options below)"))
        self.label_6.setText(_translate("PaymentMethod", "Pay with cash (coins and bills)"))
        self.label_7.setText(_translate("PaymentMethod", "Pay with E-cash"))
        self.label_8.setText(_translate("PaymentMethod", "Click the respective icons  for each method to proceed"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaymentMethod = QtWidgets.QMainWindow()
    ui = Ui_PaymentMethod()
    ui.setupUi(PaymentMethod)
    PaymentMethod.showFullScreen()
    sys.exit(app.exec_())
