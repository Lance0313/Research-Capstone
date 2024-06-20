from PyQt5 import QtCore, QtGui, QtWidgets
from oauth2client.service_account import ServiceAccountCredentials
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox, QWidget, QLabel
import StartScreen
from ThankYou import Ui_ThankYou
import qrcode
import gspread
import os

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

class Ui_Epayment(object):
    def setupUi(self, Epayment):

        #self.total_price = total_price
        StartScreen.totalPrice
        StartScreen.cartContent
        #self.cart_contents = cart_contents
        self.cell_value = None  # Variable to store the value from the spreadsheet
        self.fetchDataFromSpreadsheet()

        self.timer = QTimer()  # Initialize the timer
        self.timer.timeout.connect(self.checkData)  # Connect the timeout signal to checkData method
        self.startTimer()  # Start the timer

        # Store reference to the main window
        self.Epayment = Epayment
        Epayment.setObjectName("Epayment")
        Epayment.resize(800, 480)
        Epayment.setStyleSheet("background-color: rgb(136, 202, 94);")
        Epayment.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(Epayment)
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
        "font: 75 6pt \"MS Sans Serif\";")
        self.label.setObjectName("label")
        self.back_Button = QtWidgets.QPushButton(self.centralwidget)
        self.back_Button.setGeometry(QtCore.QRect(10, 20, 131, 31))
        self.back_Button.setStyleSheet("font: 75 15pt \"MS Sans Serif\";\n"
        "border-radius: 10px; \n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(136, 202, 94);")
        self.back_Button.setObjectName("back_Button")
        self.back_Button.clicked.connect(self.BackToCartSummary)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 40, 371, 41))
        self.label_2.setStyleSheet("font: 75 19pt \"MS Sans Serif\";\n"
        "color: rgb(255, 255, 255);")
         self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 70, 371, 41))
        self.label_3.setStyleSheet("font: 75 10pt \"MS Sans Serif\";\n"
        "color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.QRbitMapFrame = QtWidgets.QFrame(self.centralwidget)
        self.QRbitMapFrame.setGeometry(QtCore.QRect(240, 170, 311, 221))
        self.QRbitMapFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.QRbitMapFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.QRbitMapFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.QRbitMapFrame.setObjectName("QRbitMapFrame")
        self.QRBitMap = QtWidgets.QLabel(self.QRbitMapFrame)
        self.QRBitMap.setGeometry(QtCore.QRect(40, 20, 231, 191))
        self.QRBitMap.setText("")
        self.QRBitMap.setObjectName("QRBitMap")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(240, 110, 311, 51))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 151, 16))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.TotalPrice = QtWidgets.QLabel(self.frame_3)
        self.TotalPrice.setGeometry(QtCore.QRect(260, 20, 31, 16))
        self.TotalPrice.setStyleSheet("color: rgb(255, 0, 0);")
        self.TotalPrice.setObjectName("TotalPrice")
        self.TotalPrice.setText(str(StartScreen.totalPrice))
        self.proceed_Button = QtWidgets.QPushButton(self.centralwidget)
        self.proceed_Button.setGeometry(QtCore.QRect(650, 390, 131, 31))
        self.proceed_Button.setStyleSheet("\n"
         "font: 75 15pt \"MS Sans Serif\";\n"
        "border-radius: 10px; \n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(136, 202, 94);")
        self.proceed_Button.setObjectName("proceed_Button")
        self.proceed_Button.clicked.connect(self.proceedClicked)
        Epayment.setCentralWidget(self.centralwidget)
        self.generateQRCode()
        self.retranslateUi(Epayment)
        QtCore.QMetaObject.connectSlotsByName(Epayment)

    def retranslateUi(self, Epayment):
        _translate = QtCore.QCoreApplication.translate
        Epayment.setWindowTitle(_translate("Epayment", "MainWindow"))
        self.label.setText(_translate("Epayment", "© 2024 LMMN, Inc. All rights reserved"))
        self.back_Button.setText(_translate("Epayment", "Back"))
        self.label_2.setText(_translate("Epayment", "Payment Method: E-Cash"))
        self.label_3.setText(_translate("Epayment", "Please scan the provided QR code below"))
        self.label_5.setText(_translate("Epayment", "Total Amount to be Paid"))
        self.proceed_Button.setText(_translate("Epayment", "Proceed"))

    def fetchDataFromSpreadsheet(self):
        # Define the scope and credentials
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name("epayment-420521-46b551fd114c.json", scope)

        # Authorize the client
        gc = gspread.authorize(credentials)

        # Open the spreadsheet
        spreadsheet = gc.open_by_key("1-X6uzIDHpbrS2l4zp3rvSw-NIVDfLJJBiOMl8GU1F4Y")

        # Access the first worksheet
        worksheet = spreadsheet.get_worksheet(1)

        # Get the value from column 1, row 2
        self.cell_value = int(worksheet.cell(2, 1).value)
        
    def generateQRCode(self):
    # Generate QR code
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(str(StartScreen.totalPrice))
        qr.make(fit=True)
        
        # Create image
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Convert to bytes
        image_byte_array = QtCore.QByteArray()
        buffer = QtCore.QBuffer(image_byte_array)
        buffer.open(QtCore.QIODevice.WriteOnly)
        qr_img.save(buffer, "PNG")

        # Convert to QImage
        image = QtGui.QImage.fromData(image_byte_array)

        pixmap = QtGui.QPixmap.fromImage(image).scaled(self.QRBitMap.size(), QtCore.Qt.KeepAspectRatio)
        # Display in QLabel
        self.QRBitMap.setPixmap(pixmap)

    def BackToCartSummary(self):
        from CartSummary import Ui_CartSummary
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CartSummary()
        self.ui.setupUi(self.window)
             self.window.showFullScreen()

    def proceedClicked(self):
        if self.cell_value is not None and self.cell_value >= StartScreen.totalPrice:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ThankYou()
            self.ui.setupUi(self.window)
            self.loading = LoadingScreen()
            self.loading.showFullScreen()
            self.updateSpreadsheet() 
            self.window.showFullScreen()
            self.Epayment.close()
        else:
            self.PaymentChecking()

    def PaymentChecking(message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Double check your payment")
        msg.setWindowTitle("Payment error")
        msg.exec_()

    def updateSpreadsheet(self):
        # Define the scope and credentials
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name("epayment-420521-46b551fd114c.json", scope)

        # Authorize the client
        gc = gspread.authorize(credentials)

        # Open the spreadsheet
        spreadsheet = gc.open_by_key("1-X6uzIDHpbrS2l4zp3rvSw-NIVDfLJJBiOMl8GU1F4Y")

        # Access the first worksheet
        worksheet = spreadsheet.get_worksheet(1)

        # Update the value in column 1, row 2 to "0"
        worksheet.update_cell(2, 1, "0")

    def startTimer(self):
        self.timer.start(5000)  # Start the timer with a timeout of 5000 milliseconds (5 seconds)

    def stopTimer(self):
        self.timer.stop()  # Stop the timer

    def checkData(self):
        # Method to check for data periodically
        self.fetchDataFromSpreadsheet()
        if self.cell_value is not None and self.cell_value >= StartScreen.totalPrice:
            self.stopTimer()  # Stop the timer if condition is met


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Epayment = QtWidgets.QMainWindow()
    ui = Ui_Epayment()
    ui.setupUi(Epayment)
    Epayment.showFullScreen()
    sys.exit(app.exec_())
