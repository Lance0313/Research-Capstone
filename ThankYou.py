import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
import firebase_admin
from firebase_admin import credentials, db
import sys
import os
import StartScreen
import serial
from serial import Serial
import time

## Database Insert
if not firebase_admin._apps:
    cred = credentials.Certificate("keywords-e2507-firebase-adminsdk-ruto8-cc3abd39a8.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://keywords-e2507-default-rtdb.firebaseio.com/'
    })
ref = db.reference()
## Database Insert 

## Convert tuple to dictionary
for i, item_tuple in enumerate(StartScreen.cartContent, start=1):
    item_dict = dict(item_tuple)
    doc_id = "{:02}".format(i)
    db.collection("TotalSales").document(doc_id).set(item_dict)
## Convert tuple to dictionary

## Loading Screen
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
        timer.singleShot(4000, self.stopAnimation)

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()
## Loading Screen
class Ui_ThankYou(object):
    def setupUi(self, ThankYou):

        ## Initialize Serial Port
        #self.arduino_port = 'COM5'
        self.arduino_port = '/dev/ttyUSB0'
    
        try:
            self.ser = Serial(self.arduino_port, 9600)
            time.sleep(2) 
        except serial.SerialException as e:
            print("Error initializing serial connection:", e)
            self.ser = None  
        ## Initialize Serial Port

        ## Split the items in cartContent list
        prod_name = [item[0] for item in StartScreen.cartContent]
        prod_quantity = [item[1] for item in StartScreen.cartContent]
        prod_price = [item[2] for item in StartScreen.cartContent]
        # print("Product Names:", prod_name)
        # print("Product Quantities:", prod_quantity)
        # print("Product Prices:", prod_price)
        ## Split the items in cartContent list

        ## Concatenate items for sending to serial port
        self.concatenated_items = self.concatenateItemCodes(prod_name, prod_quantity)
        #print("Concatenated Item Codes:", self.concatenated_items)
        #print(StartScreen.cartContent)
        ## Concatenate items for sending to serial port

        ## Write
        self.writeDataToRealtimeDB(prod_name, prod_quantity, prod_price)
        self.writeDataToVendingMachine(prod_name, prod_quantity)
        self.send_to_arduino(self.concatenated_items)
        if StartScreen.moneyChange != 0:
            self.writeChange()
            self.writeChangetoRealTimeDB()
        ThankYou.setObjectName("ThankYou")
        ThankYou.resize(800, 480)
        ThankYou.setStyleSheet("background-color: rgb(136, 202, 94);")
        ThankYou.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(ThankYou)
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 20, 451, 111))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 75 100pt \"MS Sans Serif\";\n"
        "")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Resources/images/SMART.png"))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 120, 461, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Resources/images/Pharmakeutical Kiosk.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 180, 451, 41))
        self.label_6.setStyleSheet("font: 75 12pt \"MS Sans Serif\";\n"
        "color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(320, 10, 211, 31))
        self.label_7.setStyleSheet("font: 75 12pt \"MS Sans Serif\";\n"
        "color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(120, 340, 581, 31))
        self.label_8.setStyleSheet("font: 75 12pt \"MS Sans Serif\";\n"
        "color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.back_Button = QtWidgets.QPushButton(self.centralwidget)
        self.back_Button.setGeometry(QtCore.QRect(650, 20, 131, 31))
        self.back_Button.setStyleSheet("font: 75 15pt \"MS Sans Serif\";\n"
        "border-radius: 10px; \n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(136, 202, 94);")
        self.back_Button.setObjectName("back_Button")
        self.back_Button.clicked.connect(self.BackToStart)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 200, 471, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Resources/images/thankyou_people.png"))
        self.label_2.setObjectName("label_2")
        self.waterButton = QtWidgets.QPushButton(self.centralwidget)
        self.waterButton.setGeometry(QtCore.QRect(300, 380, 191, 31))
        self.waterButton.setStyleSheet("font: 75 15pt \"MS Sans Serif\";\n"
        "border-radius: 10px; \n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(136, 202, 94);")
        self.waterButton.setObjectName("waterButton")
        self.water_button_clicked = False
        self.waterButton.clicked.connect(self.WaterButton)
        
        self.label_5.raise_()
        self.label_3.raise_()
        self.frame.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_6.raise_()
        self.label_2.raise_()
        self.waterButton.raise_()
        ThankYou.setCentralWidget(self.centralwidget)
        # timer = QTimer(ThankYou)
        # timer.singleShot(14690, self.BackToStart)
        # timer.start()
        self.retranslateUi(ThankYou)
        QtCore.QMetaObject.connectSlotsByName(ThankYou)

    def send_to_arduino(self, command):
        if self.ser is not None:
            self.ser.write(command.encode())
            print(f"Sent command: {command}")

        else:
            print("Serial connection not initialized. Cannot send command to Arduino.")
    
    ## Write updates to database
    def writeDataToRealtimeDB(self, prod_name, prod_quantity, prod_price):
        threading.Thread(target=self._writeDataToRealtimeDB, args=(prod_name, prod_quantity, prod_price)).start()
        

    def _writeDataToRealtimeDB(self, prod_name, prod_quantity, prod_price):
        max_doc_id = max(int(doc_id) for doc_id in ref.child("TotalSales").get().keys()) if ref.child("TotalSales").get() else 0

        for i in range(len(prod_name)):
            
            doc_id = max_doc_id + 1 + i
            if(doc_id < 10):
                real_id = "0" + str(doc_id)
                
            else:
                real_id = str(doc_id)
            item_data = {
                "ID": real_id,
                "itemName": prod_name[i],
                "itemSold": prod_quantity[i],
                "totalPrice": prod_price[i]
            }

            ref.child("TotalSales").child(real_id).set(item_data)
            print("Data written to Realtime Database for item:", prod_name[i])

        
    def writeDataToVendingMachine(self, prod_name, prod_quantity):
        thread = threading.Thread(target=self._writeDataToVendingMachine, args=(prod_name, prod_quantity))
        thread.start()
        

    def _writeDataToVendingMachine(self, prod_name, prod_quantity):
        vending_machine_ref = ref.child("VendingMachine")
        for i in range(len(prod_name)):
            item_name = prod_name[i]
            item_quantity = int(prod_quantity[i])

            item_found = False
            for key in vending_machine_ref.get():
                item_data = vending_machine_ref.child(key).get()
                if item_data.get("itemName") == item_name:
                    current_stock = int(item_data.get("itemStock"))
                    new_stock = max(current_stock - item_quantity, 0)
                    vending_machine_ref.child(key).child("itemStock").set(str(new_stock))
                    item_found = True

            if not item_found:
                print("Item", item_name, "does not exist in VendingMachine node.")

    def writeChangetoRealTimeDB(self):
        updatedChange = int(StartScreen.moneyChangeAvailable) - int(StartScreen.moneyChange)
        #print(updatedChange)
        ref.child("Sukli").child("01").child("available").set(updatedChange)
    ## Writing updates to database

    def concatenateItemCodes(self, prod_name, prod_quantity):
        item_codes_dict = {
            "Ascof Forte": "A",
            "Biogesic": "B",
            "Bonamine": "C",
            "Cetirizine": "D",
            "Fern C": "E",
            "Kremil S": "F",
            "Imodium": "G",
            "Medicol Advance 400": "H",
            "Neozep Forte": "I",
            "Neozep Non Drowsy": "J"
        }

        concatenated_item_codes = ""

        for i in range(len(prod_name)):
            item_name = prod_name[i]
            item_quantity = int(prod_quantity[i])
            item_code = item_codes_dict.get(item_name, "")
            concatenated_item_codes += item_code * item_quantity

        return concatenated_item_codes
    
    def writeChange(self):
        concatenated_change = ""
        for i in range(StartScreen.moneyChange, 0, -1):
            concatenated_change += "1"
        self.send_to_arduino(concatenated_change)
        #print(concatenated_change)
    

    def WaterButton(self):
        # Check if the button hasn't been clicked before
        if not self.water_button_clicked:
            # Set flag to True to indicate button has been clicked
            self.water_button_clicked = True

            # Send command to Arduino for water
            command = "K"
            threading.Thread(target=self.send_to_arduino, args=(command,)).start()

            # Set timer to go back to start screen after 4 seconds
            timer = QTimer()
            timer.singleShot(10000, self.BackToStart)
            timer.start()

    def close_firebase(self):
        # Close the Firebase app
        firebase_admin.delete_app(firebase_admin.get_app())
    
    def open_startscreen(self):
        import subprocess
        subprocess.Popen(["python", "StartScreen.py"])
        #subprocess.Popen(["StartScreen.exe"])

    def close_serial_connection(self):
        if self.ser is not None:
            self.ser.close()
            print("Serial connection closed.")
        else:
            print("Serial connection is already closed or not initialized.")

    def BackToStart(self):
        # Start a new thread to close Firebase
        firebase_thread = threading.Thread(target=self.close_firebase)
        firebase_thread.start()
        
        startscreen_thread = threading.Thread(target=self.open_startscreen)
        startscreen_thread.start()

        self.loading = LoadingScreen()
        self.loading.showFullScreen()
        self.close_serial_connection()
        # Close the current window
        self.centralwidget.window().close()
        
    def retranslateUi(self, ThankYou):
        _translate = QtCore.QCoreApplication.translate
        ThankYou.setWindowTitle(_translate("ThankYou", "MainWindow"))
        self.label.setText(_translate("ThankYou", "© 2024 LMMN, Inc. All rights reserved"))
        self.label_6.setText(_translate("ThankYou", "Streamlined Over-the-Counter Medicine Dispensing Innovation\n"""))
        self.label_7.setText(_translate("ThankYou", "Thank you for using"))
        self.label_8.setText(_translate("ThankYou", "Please don\'t forget to collect you medicine and change on the bin"))
        self.waterButton.setText(_translate("ThankYou", "Click me for water"))
        self.back_Button.setText(_translate("ThankYou", "Home"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThankYou = QtWidgets.QMainWindow()
    ui = Ui_ThankYou()
    ui.setupUi(ThankYou)
    ThankYou.showFullScreen()
    sys.exit(app.exec_())