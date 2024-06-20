from PyQt5 import QtCore, QtGui, QtWidgets
import StartScreen
class Ui_ErrorMessage(object):
    def setupUi(self, ErrorMessage):
        ErrorMessage.setObjectName("ErrorMessage")
        ErrorMessage.setWindowModality(QtCore.Qt.ApplicationModal)
        ErrorMessage.setFixedSize(400, 200)
        ErrorMessage.setStyleSheet("background-color: rgb(255, 255, 247);\n"
        "border-radius: 10px")
        ErrorMessage.setWindowFlags(QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint)
        self.centralwidget = QtWidgets.QWidget(ErrorMessage)
        self.centralwidget.setObjectName("centralwidget")
        self.ErrorDialogue = QtWidgets.QLabel(self.centralwidget)
        self.ErrorDialogue.setGeometry(QtCore.QRect(150, 40, 221, 101))
        self.ErrorDialogue.setStyleSheet("\n"
        "font: 12pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 247);\n"
        "background-color: rgb(136, 202, 94);\n"
        "border-radius: 20px")
        self.ErrorDialogue.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorDialogue.setWordWrap(True) 
        self.ErrorDialogue.setObjectName("ErrorDialogue")
        self.ErrorDialogue.setText(StartScreen.ErrorDialogue)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 101, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Resources/images/Error.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.proceed_button = QtWidgets.QPushButton(self.centralwidget)
        self.proceed_button.setGeometry(QtCore.QRect(260, 160, 131, 31))
        self.proceed_button.setStyleSheet("\n"
        "font: 75 15pt \"MS Sans Serif\";\n"
        "border-radius: 10px; \n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(136, 202, 94);\n"
        "")
        self.proceed_button.setObjectName("proceed_button")
        self.proceed_button.clicked.connect(self.close)
        ErrorMessage.setCentralWidget(self.centralwidget)

        self.retranslateUi(ErrorMessage)
        QtCore.QMetaObject.connectSlotsByName(ErrorMessage)

    def retranslateUi(self, ErrorMessage):
        _translate = QtCore.QCoreApplication.translate
        ErrorMessage.setWindowTitle(_translate("ErrorMessage", "Error"))
        self.proceed_button.setText(_translate("ErrorMessage", "OK"))
    def close(self):
        self.centralwidget.window().close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ErrorMessage = QtWidgets.QMainWindow()
    ui = Ui_ErrorMessage()
    ui.setupUi(ErrorMessage)
    ErrorMessage.setWindowFlags(ErrorMessage.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
    ErrorMessage.setWindowModality(QtCore.Qt.ApplicationModal)
    ErrorMessage.show()
    sys.exit(app.exec_())

