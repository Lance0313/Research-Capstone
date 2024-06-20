from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import StartScreen

class Ui_ChangeNotice(object):
    def setupUi(self, ChangeNotice):
        ChangeNotice.setObjectName("ChangeNotice")
        ChangeNotice.resize(800, 480)
        ChangeNotice.setStyleSheet("background-color: rgb(136, 202, 94);")
        ChangeNotice.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(ChangeNotice)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 651, 61))
        self.label.setStyleSheet("font: 27pt \"MS Sans Serif\";\n"
        "background-color: rgb(255, 255, 255);\n"
        "text-align: center;\n"
        "border-radius:5px;\n""\n""")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.amountExpected = QtWidgets.QLabel(self.centralwidget)
        self.amountExpected.setGeometry(QtCore.QRect(150, 110, 501, 71))
        self.amountExpected.setStyleSheet("font: 22pt \"MS Sans Serif\";\n"
        "background-color: rgb(255, 255, 255);\n"
        "border-radius:5px;")
        self.amountExpected.setAlignment(QtCore.Qt.AlignCenter)
        self.amountExpected.setObjectName("amountExpected")
        self.numpadFrame = QtWidgets.QFrame(self.centralwidget)
        self.numpadFrame.setGeometry(QtCore.QRect(290, 200, 221, 221))
        self.numpadFrame.setStyleSheet("background-color: rgb(255, 0, 127);\n"
        "background-color: rgb(255, 255, 255);\n"
        "")
        self.numpadFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.numpadFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.numpadFrame.setObjectName("numpadFrame")
        self.one_key = QtWidgets.QPushButton(self.numpadFrame)
        self.one_key.setGeometry(QtCore.QRect(20, 120, 41, 41))
        self.one_key.setStyleSheet("background-color: rgb(217, 217, 217);\n"
        "font: 15pt \"MS Sans Serif\";\n"
        "alternate-background-color: rgb(132, 132, 132);\n"
        "")
        self.one_key.setObjectName("one_key")
        self.one_key.clicked.connect(self.one_key_add)
        self.two_key = QtWidgets.QPushButton(self.numpadFrame)
        self.two_key.setGeometry(QtCore.QRect(90, 120, 41, 41))
        self.two_key.setStyleSheet("background-color: rgb(217, 217, 217);\n"
        "font: 15pt \"MS Sans Serif\";\n"
        "alternate-background-color: rgb(132, 132, 132);\n"
        "")
        self.two_key.setObjectName("two_key")
        self.two_key.clicked.connect(self.two_key_add)
        self.three_key = QtWidgets.QPushButton(self.numpadFrame)
        self.three_key.setGeometry(QtCore.QRect(160, 120, 41, 41))
        self.three_key.setStyleSheet("background-color: rgb(217, 217, 217);\n"
        "font: 15pt \"MS Sans Serif\";\n"
        "alternate-background-color: rgb(132, 132, 132);\n"
        "")
        self.three_key.setObjectName("three_key")
        self.three_key.clicked.connect(self.three_key_add)
        self.four_key = QtWidgets.QPushButton(self.numpadFrame)
        self.four_key.setGeometry(QtCore.QRect(20, 70, 41, 41))
        self.four_key.setStyleSheet("background-color: rgb(217, 217, 217);\n"
        "font: 15pt \"MS Sans Serif\";\n"
        "alternate-background-color: rgb(132, 132, 132);\n"
        "")
        self.four_key.setObjectName("four_key")
        self.four_key.clicked.connect(self.four_key_add)
        self.five_key = QtWidgets.QPushButton(self.numpadFrame)
        self.five_key.setGeometry(QtCore.QRect(90, 70, 41, 41))
        self.five_key.setStyleSheet("background-color: rgb(217, 217, 217);\n"
        "font: 15pt \"MS Sans Serif\";\n"
        "alternate-background-color: rgb(132, 132, 132);\n"
        "")
        self.five_key.setObjectName("five_key")
        self.five_key.clicked.connect(self.five_key_add)
        self.six_key = QtWidgets.QPushButton(self.numpadFrame)
        self.six_key.setGeometry(QtCore.QRect(160, 70, 41, 41))
        self.six_key.setStyleSheet("background-color: rgb(217, 217, 217);\n"
        "font: 15pt \"MS Sans Serif\";\n"
        "alternate-background-color: rgb(132, 132, 132);\n"
        "")
        self.six_key.setObjectName("six_key")
        self.six_key.clicked.connect(self.six_key_add)
        self.seven_key = QtWidgets.QPushButton(self.numpadFrame)
        self.seven_key.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.seven_key.setStyleSheet("background-color: rgb(217, 217, 217);\n"
        "font: 15pt \"MS Sans Serif\";\n"
        "alternate-background-color: rgb(132, 132, 132);\n"
        "")
        self.seven_key.setObjectName("seven_key")
        self.seven_key.clicked.connect(self.seven_key_add)
        self.eight_key = QtWidgets.QPushButton(self.numpadFrame)
        self.eight_key.setGeometry(QtCore.QRect(90, 20, 41, 41))
        self.eight_key.setStyleSheet("background-color: rgb(217, 217, 217);\n"
        "font: 15pt \"MS Sans Serif\";\n"
        "alternate-background-color: rgb(132, 132, 132);\n"
        "")
        self.eight_key.setObjectName("eight_key")
        self.eight_key.clicked.connect(self.eight_key_add)
        self.nine_key = QtWidgets.QPushButton(self.numpadFrame)
        self.nine_key.setGeometry(QtCore.QRect(160, 20, 41, 41))
        self.nine_key.setStyleSheet("background-color: rgb(217, 217, 217);\n"
        "font: 15pt \"MS Sans Serif\";\n"
        "alternate-background-color: rgb(132, 132, 132);")
        self.nine_key.setObjectName("nine_key")
        self.nine_key.clicked.connect(self.nine_key_add)
        self.zero_key = QtWidgets.QPushButton(self.numpadFrame)
        self.zero_key.setGeometry(QtCore.QRect(90, 170, 41, 41))
        self.zero_key.setStyleSheet("background-color: rgb(217, 217, 217);\n"
        "font: 15pt \"MS Sans Serif\";\n"
        "alternate-background-color: rgb(132, 132, 132);")
        self.zero_key.setObjectName("zero_key")
        self.zero_key.clicked.connect(self.zero_key_add)
        self.backspace_key = QtWidgets.QPushButton(self.numpadFrame)
        self.backspace_key.setGeometry(QtCore.QRect(160, 170, 41, 41))
        self.backspace_key.setStyleSheet("background-color: rgb(217, 217, 217);\n"
        "font: 15pt \"MS Sans Serif\";\n"
        "alternate-background-color: rgb(132, 132, 132);")
        self.backspace_key.setObjectName("backspace_key")
        self.backspace_key.clicked.connect(self.backspace_key_add)
        self.proceed_Button = QtWidgets.QPushButton(self.centralwidget)
        self.proceed_Button.setGeometry(QtCore.QRect(660, 400, 131, 31))
        self.proceed_Button.setStyleSheet("\n"
        "font: 75 15pt \"MS Sans Serif\";\n"
        "border-radius: 10px; \n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(136, 202, 94);")
        self.proceed_Button.setObjectName("proceed_Button")
        self.proceed_Button.clicked.connect(self.ProceedToCashPayment)
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(10, 400, 131, 31))
        self.back_button.setStyleSheet("\n"
        "font: 75 15pt \"MS Sans Serif\";\n"
        "border-radius: 10px; \n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(136, 202, 94);")
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(self.BackButton)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(0, 440, 811, 41))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setGeometry(QtCore.QRect(310, 10, 231, 21))
        self.label_7.setStyleSheet("color: rgb(136, 202, 94);\n"
        "font: 75 6pt \"MS Sans Serif\";")
        self.label_7.setObjectName("label_7")
        ChangeNotice.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChangeNotice)
        QtCore.QMetaObject.connectSlotsByName(ChangeNotice)

    ##Numpad Functions
    def one_key_add(self):
        if len(self.amountExpected.text()) < 4:
                self.amountExpected.setText(self.amountExpected.text() + "1")
    def two_key_add(self):
        if len(self.amountExpected.text()) < 4:
                self.amountExpected.setText(self.amountExpected.text() + "2")
    def three_key_add(self):
        if len(self.amountExpected.text()) < 4:
                self.amountExpected.setText(self.amountExpected.text() + "3")
    def four_key_add(self):
        if len(self.amountExpected.text()) < 4:
                self.amountExpected.setText(self.amountExpected.text() + "4")
    def five_key_add(self):
        if len(self.amountExpected.text()) < 4:
                self.amountExpected.setText(self.amountExpected.text() + "5")
    def six_key_add(self):
        if len(self.amountExpected.text()) < 4:
                self.amountExpected.setText(self.amountExpected.text() + "6")
    def seven_key_add(self):
        if len(self.amountExpected.text()) < 4:
                self.amountExpected.setText(self.amountExpected.text() + "7")
    def eight_key_add(self):
        if len(self.amountExpected.text()) < 4:
                self.amountExpected.setText(self.amountExpected.text() + "8")
    def nine_key_add(self):
        if len(self.amountExpected.text()) < 4:
                self.amountExpected.setText(self.amountExpected.text() + "9")
    def zero_key_add(self):
        if len(self.amountExpected.text()) < 4:
                if self.amountExpected.text() != "0":
                        self.amountExpected.setText(self.amountExpected.text() + "0")
    def backspace_key_add(self):
        current_text = self.amountExpected.text()
        if current_text:
                updated_text = current_text[:-1]
                self.amountExpected.setText(updated_text)
    ##Numpad Functions

    ##Error Dialogue Box Function
    def ChangeDispensingLimit(self):
        StartScreen.ErrorDialogue = "The system can not provide sufficient change."
        from ErrorDialogue import Ui_ErrorMessage
        self.error = QtWidgets.QMainWindow()
        self.ui = Ui_ErrorMessage()
        self.ui.setupUi(self.error)
        self.error.show()

        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Critical)
        # msg.setText("The system can not provide sufficient change.")
        # msg.setWindowTitle("Change Policy")
        # msg.exec_()

    def InsufficientFund(self):
        StartScreen.ErrorDialogue = "Insufficient Payment"
        from ErrorDialogue import Ui_ErrorMessage
        self.error = QtWidgets.QMainWindow()
        self.ui = Ui_ErrorMessage()
        self.ui.setupUi(self.error)
        self.error.show()
        
        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Critical)
        # msg.setText("Insufficient Payment")
        # msg.setWindowTitle("Payment Notice")
        # msg.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # msg.setMaximumWidth(600)
        # msg.exec_()
    ##Error Dialogue Box Function

    ##Navigation Functions
    def ProceedToCashPayment(self):
        change = int(self.amountExpected.text( )) - StartScreen.totalPrice
        #print(change)
        if int(self.amountExpected.text( )) >= StartScreen.totalPrice:
            if change <= StartScreen.moneyChangeAvailable:
                    from CashPayment import Ui_CashPayment
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_CashPayment()
                    self.ui.setupUi(self.window)
                    self.window.showFullScreen()
                    self.centralwidget.window().close()
            else:
                    self.ChangeDispensingLimit()
        else:
              self.InsufficientFund()

    def BackButton(self):
        from PaymentMethod import Ui_PaymentMethod
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PaymentMethod()
        self.ui.setupUi(self.window)
        self.window.showFullScreen()
        self.centralwidget.window().close()
    ##Navigation Functions

    def retranslateUi(self, ChangeNotice):
        _translate = QtCore.QCoreApplication.translate
        ChangeNotice.setWindowTitle(_translate("ChangeNotice", "MainWindow"))
        self.label.setText(_translate("ChangeNotice", "How much money are you inserting?"))
        self.one_key.setText(_translate("ChangeNotice", "1"))
        self.two_key.setText(_translate("ChangeNotice", "2"))
        self.three_key.setText(_translate("ChangeNotice", "3"))
        self.four_key.setText(_translate("ChangeNotice", "4"))
        self.five_key.setText(_translate("ChangeNotice", "5"))
        self.six_key.setText(_translate("ChangeNotice", "6"))
        self.seven_key.setText(_translate("ChangeNotice", "7"))
        self.eight_key.setText(_translate("ChangeNotice", "8"))
        self.nine_key.setText(_translate("ChangeNotice", "9"))
        self.zero_key.setText(_translate("ChangeNotice", "0"))
        self.backspace_key.setText(_translate("ChangeNotice", "⌫"))
        self.proceed_Button.setText(_translate("ChangeNotice", "Proceed"))
        self.back_button.setText(_translate("ChangeNotice", "Back"))
        self.label_7.setText(_translate("ChangeNotice", "© 2024 LMMN, Inc. All rights reserved"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangeNotice = QtWidgets.QMainWindow()
    ui = Ui_ChangeNotice()
    ui.setupUi(ChangeNotice)
    ChangeNotice.show()
    sys.exit(app.exec_())
