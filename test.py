import sys
import pyqrcode
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from io import BytesIO

class QRCodeGenerator(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.initUI()

    def initUI(self):
        # Generate QR code
        qr = pyqrcode.create(self.data)

        # Convert QR code to bytes
        qr_bytes = BytesIO()
        qr.png(qr_bytes, scale=5)  # Scaling the QR code for better visibility

        # Convert bytes to QPixmap
        qr_pixmap = QPixmap()
        qr_pixmap.loadFromData(qr_bytes.getvalue())

        # Create QLabel to display QR code
        self.qr_label = QLabel()
        self.qr_label.setPixmap(qr_pixmap)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.qr_label)

        self.setLayout(layout)
        self.setWindowTitle('QR Code Generator')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    data = "123"
    window = QRCodeGenerator(data)
    window.show()
    sys.exit(app.exec_())
