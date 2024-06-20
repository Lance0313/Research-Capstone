from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import StartScreen

class Ui_CartSummary(object):
    proceed_signal = QtCore.pyqtSignal(bool)

    def setupUi(self, CartSummary ):
        StartScreen.cartContent
        StartScreen.totalPrice
        print("Type of cartContent before setupUi:", type(StartScreen.cartContent))
        CartSummary.setObjectName("CartSummary")
        CartSummary.resize(800, 480)
        CartSummary.setStyleSheet("background-color: rgb(136, 202, 94);")
        CartSummary.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(CartSummary)
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
        self.CartSummaryBack = QtWidgets.QPushButton(self.centralwidget)
        self.CartSummaryBack.setGeometry(QtCore.QRect(10, 20, 131, 31))
        self.CartSummaryBack.setStyleSheet("\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"border-radius: 10px; \n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(136, 202, 94);")
        self.CartSummaryBack.setObjectName("CartSummaryBack")
        self.CartSummaryBack.clicked.connect(self.BackToPurchase)
        self.CartSummaryProceed = QtWidgets.QPushButton(self.centralwidget)
        self.CartSummaryProceed.setGeometry(QtCore.QRect(660, 390, 131, 31))
        self.CartSummaryProceed.setStyleSheet("\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"border-radius: 10px; \n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(136, 202, 94);")
        self.CartSummaryProceed.setObjectName("CartSummaryProceed")
        self.CartSummaryProceed.clicked.connect(self.ProceedToPayment)
        self.CartSummaryFrame = QtWidgets.QFrame(self.centralwidget)
        self.CartSummaryFrame.setGeometry(QtCore.QRect(40, 70, 721, 301))
        self.CartSummaryFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CartSummaryFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CartSummaryFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CartSummaryFrame.setObjectName("CartSummaryFrame")
        self.frame_3 = QtWidgets.QFrame(self.CartSummaryFrame)
        self.frame_3.setGeometry(QtCore.QRect(-10, 40, 741, 16))
        self.frame_3.setStyleSheet("background-color: rgb(136, 202, 94);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.CartSummaryFrame)
        self.label_2.setGeometry(QtCore.QRect(310, 10, 171, 21))
        self.label_2.setStyleSheet("color: rgb(136, 202, 94);\n"
"font: 75 15pt \"MS Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.CartSummaryTotal = QtWidgets.QLabel(self.CartSummaryFrame)
        self.CartSummaryTotal.setGeometry(QtCore.QRect(550, 270, 101, 20))
        self.CartSummaryTotal.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 12pt \"MS Sans Serif\";")
        self.CartSummaryTotal.setObjectName("CartSummaryTotal")
        self.CartSummaryTotal.setText("Php " + str(StartScreen.totalPrice))
        self.CartSummaryName = QtWidgets.QLabel(self.CartSummaryFrame)
        self.CartSummaryName.setGeometry(QtCore.QRect(30, 70, 191, 171))
        self.CartSummaryName.setObjectName("CartSummaryName")
        self.CartSummaryQuantity = QtWidgets.QLabel(self.CartSummaryFrame)
        self.CartSummaryQuantity.setGeometry(QtCore.QRect(280, 70, 191, 201))
        self.CartSummaryQuantity.setObjectName("CartSummaryQuantity")
        self.CartSummaryPrice = QtWidgets.QLabel(self.CartSummaryFrame)
        self.CartSummaryPrice.setGeometry(QtCore.QRect(510, 70, 191, 191))
        self.CartSummaryPrice.setObjectName("CartSummaryPrice")
        CartSummary.setCentralWidget(self.centralwidget)

        ##Display the cart content
        for index, (prod_name, prod_quantity, prod_price) in enumerate(StartScreen.cartContent):
            self.CartSummaryName.setText(self.CartSummaryName.text() + f"{prod_name}\n")
            self.CartSummaryName.setAlignment(Qt.AlignTop)
            self.CartSummaryQuantity.setText(self.CartSummaryQuantity.text() + f"{prod_quantity}\n")
            self.CartSummaryQuantity.setAlignment(Qt.AlignTop)
            self.CartSummaryPrice.setText(self.CartSummaryPrice.text() + f"Php {prod_price:.2f}\n")
            self.CartSummaryPrice.setAlignment(Qt.AlignTop)
        ##Display the cart content

        self.retranslateUi(CartSummary)
        QtCore.QMetaObject.connectSlotsByName(CartSummary)

    def ProceedToPayment(self):
        from PaymentMethod import Ui_PaymentMethod
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PaymentMethod()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
        self.centralwidget.window().close()

    def BackToPurchase(self):
        confirmation = QMessageBox()
        confirmation.setIcon(QMessageBox.Question)
        confirmation.setText("This will reset your cart. Continue?")
        confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirmation.setDefaultButton(QMessageBox.No)
        confirmation.setWindowTitle("Warning")

        # If user confirms, proceed to purchase screen
        if confirmation.exec() == QMessageBox.Yes:
            from Purchase import Ui_Purchase
            print("Type of cartContent inside BackToPurchase:", type(StartScreen.cartContent))
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Purchase()
            self.ui.setupUi(self.window)
            self.window.showFullScreen()
            self.centralwidget.window().close()

    def retranslateUi(self, CartSummary):
        _translate = QtCore.QCoreApplication.translate
        CartSummary.setWindowTitle(_translate("CartSummary", "MainWindow"))
        self.label.setText(_translate("CartSummary", "© 2024 LMMN, Inc. All rights reserved"))
        self.CartSummaryBack.setText(_translate("CartSummary", "Back"))
        self.CartSummaryProceed.setText(_translate("CartSummary", "Pay"))
        self.label_2.setText(_translate("CartSummary", "YOUR CART"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CartSummary = QtWidgets.QMainWindow()
    ui = Ui_CartSummary()
    ui.setupUi(CartSummary)
    CartSummary.showFullScreen()
    print("Before app.exec_()")  # Add this line
    sys.exit(app.exec_())
