from PyQt5 import QtCore, QtGui, QtWidgets
import firebase_admin
from firebase_admin import credentials, db
from MainSuggestion import Ui_MainSuggestion


class Ui_SuggestionQuery(object):
    def setupUi(self, SuggestionQuery):
        SuggestionQuery.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        SuggestionQuery.setObjectName("SuggestionQuery")
        SuggestionQuery.resize(800, 480)
        SuggestionQuery.setStyleSheet("background-color: rgb(136, 202, 94);")
        self.centralwidget = QtWidgets.QWidget(SuggestionQuery)
        self.centralwidget.setObjectName("centralwidget")
        self.textBox1 = QtWidgets.QLineEdit(self.centralwidget)
        self.textBox1.setGeometry(QtCore.QRect(92, 175, 591, 41))
        self.textBox1.setStyleSheet("background-color: rgb(241, 192, 185);\n"
        "background-color: rgb(255, 255, 255);")
        self.textBox1.setObjectName("textBox1")
        self.textBox1.textChanged.connect(self.text_changed)
        self.q_Key = QtWidgets.QPushButton(self.centralwidget)
        self.q_Key.setGeometry(QtCore.QRect(90, 250, 51, 41))
        self.q_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.q_Key.setObjectName("q_Key")
        self.q_Key.clicked.connect(lambda: self.update_text("q"))
        self.w_Key = QtWidgets.QPushButton(self.centralwidget)
        self.w_Key.setGeometry(QtCore.QRect(150, 250, 51, 41))
        self.w_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.w_Key.setObjectName("w_Key")
        self.w_Key.clicked.connect(lambda: self.update_text("w"))
        self.r_Key = QtWidgets.QPushButton(self.centralwidget)
        self.r_Key.setGeometry(QtCore.QRect(270, 250, 51, 41))
        self.r_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.r_Key.setObjectName("r_Key")
        self.r_Key.clicked.connect(lambda: self.update_text("r"))
        self.t_Key = QtWidgets.QPushButton(self.centralwidget)
        self.t_Key.setGeometry(QtCore.QRect(330, 250, 51, 41))
        self.t_Key.setStyleSheet("background-color: rgb(226, 151, 255);\n"
        "background-color: rgb(255, 255, 255);")
        self.t_Key.setObjectName("t_Key")
        self.t_Key.clicked.connect(lambda: self.update_text("t"))
        self.y_Key = QtWidgets.QPushButton(self.centralwidget)
        self.y_Key.setGeometry(QtCore.QRect(390, 250, 51, 41))
        self.y_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y_Key.setObjectName("y_Key")
        self.y_Key.clicked.connect(lambda: self.update_text("y"))
        self.e_Key = QtWidgets.QPushButton(self.centralwidget)
        self.e_Key.setGeometry(QtCore.QRect(210, 250, 51, 41))
        self.e_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.e_Key.setObjectName("e_Key")
        self.e_Key.clicked.connect(lambda: self.update_text("e"))
        self.u_Key = QtWidgets.QPushButton(self.centralwidget)
        self.u_Key.setGeometry(QtCore.QRect(450, 250, 51, 41))
        self.u_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.u_Key.setObjectName("u_Key")
        self.u_Key.clicked.connect(lambda: self.update_text("u"))
        self.i_Key = QtWidgets.QPushButton(self.centralwidget)
        self.i_Key.setGeometry(QtCore.QRect(510, 250, 51, 41))
        self.i_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.i_Key.setObjectName("i_Key")
        self.i_Key.clicked.connect(lambda: self.update_text("i"))
        self.a_Key = QtWidgets.QPushButton(self.centralwidget)
        self.a_Key.setGeometry(QtCore.QRect(120, 300, 51, 41))
        self.a_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.a_Key.setObjectName("a_Key")
        self.a_Key.clicked.connect(lambda: self.update_text("a"))
        self.p_Key = QtWidgets.QPushButton(self.centralwidget)
        self.p_Key.setGeometry(QtCore.QRect(630, 250, 51, 41))
        self.p_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.p_Key.setObjectName("p_Key")
        self.p_Key.clicked.connect(lambda: self.update_text("p"))
        self.o_Key = QtWidgets.QPushButton(self.centralwidget)
        self.o_Key.setGeometry(QtCore.QRect(570, 250, 51, 41))
        self.o_Key.setStyleSheet("\n"
        "background-color: rgb(255, 255, 255);")
        self.o_Key.setObjectName("o_Key")
        self.o_Key.clicked.connect(lambda: self.update_text("o"))
        self.s_Key = QtWidgets.QPushButton(self.centralwidget)
        self.s_Key.setGeometry(QtCore.QRect(180, 300, 51, 41))
        self.s_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.s_Key.setObjectName("s_Key")
        self.s_Key.clicked.connect(lambda: self.update_text("s"))
        self.d_Key = QtWidgets.QPushButton(self.centralwidget)
        self.d_Key.setGeometry(QtCore.QRect(240, 300, 51, 41))
        self.d_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.d_Key.setObjectName("d_Key")
        self.d_Key.clicked.connect(lambda: self.update_text("d"))
        self.f_Key = QtWidgets.QPushButton(self.centralwidget)
        self.f_Key.setGeometry(QtCore.QRect(300, 300, 51, 41))
        self.f_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.f_Key.setObjectName("f_Key")
        self.f_Key.clicked.connect(lambda: self.update_text("f"))
        self.g_Key = QtWidgets.QPushButton(self.centralwidget)
        self.g_Key.setGeometry(QtCore.QRect(360, 300, 51, 41))
        self.g_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.g_Key.setObjectName("g_Key")
        self.g_Key.clicked.connect(lambda: self.update_text("g"))
        self.h_Key = QtWidgets.QPushButton(self.centralwidget)
        self.h_Key.setGeometry(QtCore.QRect(420, 300, 51, 41))
        self.h_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.h_Key.setObjectName("h_Key")
        self.h_Key.clicked.connect(lambda: self.update_text("h"))
        self.j_Key = QtWidgets.QPushButton(self.centralwidget)
        self.j_Key.setGeometry(QtCore.QRect(480, 300, 51, 41))
        self.j_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.j_Key.setObjectName("j_Key")
        self.j_Key.clicked.connect(lambda: self.update_text("j"))
        self.k_Key = QtWidgets.QPushButton(self.centralwidget)
        self.k_Key.setGeometry(QtCore.QRect(540, 300, 51, 41))
        self.k_Key.setObjectName("k_Key")
        self.k_Key.clicked.connect(lambda: self.update_text("k"))
        self.k_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.l_Key = QtWidgets.QPushButton(self.centralwidget)
        self.l_Key.setGeometry(QtCore.QRect(600, 300, 51, 41))
        self.l_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.l_Key.setObjectName("l_Key")
        self.l_Key.clicked.connect(lambda: self.update_text("l"))
        self.z_Key = QtWidgets.QPushButton(self.centralwidget)
        self.z_Key.setGeometry(QtCore.QRect(170, 350, 51, 41))
        self.z_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.z_Key.setObjectName("z_Key")
        self.z_Key.clicked.connect(lambda: self.update_text("z"))
        self.x_Key = QtWidgets.QPushButton(self.centralwidget)
        self.x_Key.setGeometry(QtCore.QRect(230, 350, 51, 41))
        self.x_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x_Key.setObjectName("x_Key")
        self.x_Key.clicked.connect(lambda: self.update_text("x"))
        self.c_Key = QtWidgets.QPushButton(self.centralwidget)
        self.c_Key.setGeometry(QtCore.QRect(290, 350, 51, 41))
        self.c_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c_Key.setObjectName("c_Key")
        self.c_Key.clicked.connect(lambda: self.update_text("c"))
        self.v_Key = QtWidgets.QPushButton(self.centralwidget)
        self.v_Key.setGeometry(QtCore.QRect(350, 350, 51, 41))
        self.v_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.v_Key.setObjectName("v_Key")
        self.v_Key.clicked.connect(lambda: self.update_text("v"))
        self.b_Key = QtWidgets.QPushButton(self.centralwidget)
        self.b_Key.setGeometry(QtCore.QRect(410, 350, 51, 41))
        self.b_Key.setStyleSheet("alternate-background-color: rgb(255, 255, 255);\n"
        "background-color: rgb(255, 255, 255);")
        self.b_Key.setObjectName("b_Key")
        self.b_Key.clicked.connect(lambda: self.update_text("b"))
        self.n_Key = QtWidgets.QPushButton(self.centralwidget)
        self.n_Key.setGeometry(QtCore.QRect(470, 350, 51, 41))
        self.n_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.n_Key.setObjectName("n_Key")
        self.n_Key.clicked.connect(lambda: self.update_text("n"))
        self.m_Key = QtWidgets.QPushButton(self.centralwidget)
        self.m_Key.setGeometry(QtCore.QRect(530, 350, 51, 41))
        self.m_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.m_Key.setObjectName("m_Key")
        self.m_Key.clicked.connect(lambda: self.update_text("m"))
        self.back_Key = QtWidgets.QPushButton(self.centralwidget)
        self.back_Key.setGeometry(QtCore.QRect(480, 400, 51, 41))
        self.back_Key.setStyleSheet("background-color: rgb(255, 255, 255);\n""")
        self.back_Key.setObjectName("back_Key")
        self.back_Key.setStyleSheet("background-color: rgb(255, 255, 255);\n""")
        self.back_Key.clicked.connect(self.backspace)
        
        self.space_Key = QtWidgets.QPushButton(self.centralwidget)
        self.space_Key.setGeometry(QtCore.QRect(220, 400, 251, 41))
        self.space_Key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.space_Key.setObjectName("space_Key")
        self.space_Key.clicked.connect(self.add_space)
        self.enter_Button = QtWidgets.QPushButton(self.centralwidget)
        self.enter_Button.setGeometry(QtCore.QRect(670, 420, 121, 31))
        self.enter_Button.setStyleSheet("font: 75 15pt \"MS Sans Serif\";\n"
        "border-radius: 10px; \n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(136, 202, 94);")
        self.enter_Button.setObjectName("enter_Button")
        self.enter_Button.clicked.connect(self.check_input)
        self.back_Button = QtWidgets.QPushButton(self.centralwidget)
        self.back_Button.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.back_Button.setStyleSheet("font: 75 15pt \"MS Sans Serif\";\n"
        "border-radius: 10px; \n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(136, 202, 94);")
        self.back_Button.setObjectName("back_Button")
        self.back_Button.clicked.connect(self.BackToStart)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 68, 151, 21))
        self.label.setStyleSheet("font: 75 12pt \"MS Sans Serif\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 75, 321, 51))
        self.label_2.setStyleSheet("color: rgb(241, 192, 185);\n"
"font: 75 24pt \"MS Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 120, 661, 51))
        self.label_3.setStyleSheet("font: 75 12pt \"MS Sans Serif\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.suggestionsListBox = QtWidgets.QListWidget(self.centralwidget)
        self.suggestionsListBox.setEnabled(True)
        self.suggestionsListBox.setGeometry(QtCore.QRect(91, 210, 592, 31))
        self.suggestionsListBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.suggestionsListBox.setObjectName("suggestionsListBox")
        self.suggestionsListBox.itemClicked.connect(self.item_clicked)
        self.textBox1.raise_()
        self.q_Key.raise_()
        self.w_Key.raise_()
        self.r_Key.raise_()
        self.t_Key.raise_()
        self.y_Key.raise_()
        self.e_Key.raise_()
        self.u_Key.raise_()
        self.i_Key.raise_()
        self.a_Key.raise_()
        self.p_Key.raise_()
        self.o_Key.raise_()
        self.s_Key.raise_()
        self.d_Key.raise_()
        self.f_Key.raise_()
        self.g_Key.raise_()
        self.h_Key.raise_()
        self.j_Key.raise_()
        self.k_Key.raise_()
        self.l_Key.raise_()
        self.z_Key.raise_()
        self.x_Key.raise_()
        self.c_Key.raise_()
        self.v_Key.raise_()
        self.b_Key.raise_()
        self.n_Key.raise_()
        self.m_Key.raise_()
        self.back_Key.raise_()

        self.space_Key.raise_()
        self.enter_Button.raise_()
        self.back_Button.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.suggestionsListBox.raise_()
        self.label.raise_()
        SuggestionQuery.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SuggestionQuery)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        SuggestionQuery.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SuggestionQuery)
        self.statusbar.setObjectName("statusbar")
        SuggestionQuery.setStatusBar(self.statusbar)
        
        # Hide the suggestions list box initially
        self.suggestionsListBox.setVisible(False)

        self.retranslateUi(SuggestionQuery)
        QtCore.QMetaObject.connectSlotsByName(SuggestionQuery)
        

        # Initialize Firebase Admin SDK only once
        if not firebase_admin._apps:
            cred = credentials.Certificate("keywords-e2507-firebase-adminsdk-ruto8-cc3abd39a8.json")
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://keywords-e2507-default-rtdb.firebaseio.com/'
            })

        self.db_ref = db.reference()


    def retranslateUi(self, SuggestionQuery):
        _translate = QtCore.QCoreApplication.translate
        SuggestionQuery.setWindowTitle(_translate("SuggestionQuery", "SuggestionQuery"))
        self.q_Key.setText(_translate("SuggestionQuery", "q"))
        self.w_Key.setText(_translate("SuggestionQuery", "w"))
        self.r_Key.setText(_translate("SuggestionQuery", "r"))
        self.t_Key.setText(_translate("SuggestionQuery", "t"))
        self.y_Key.setText(_translate("SuggestionQuery", "y"))
        self.e_Key.setText(_translate("SuggestionQuery", "e"))
        self.u_Key.setText(_translate("SuggestionQuery", "u"))
        self.i_Key.setText(_translate("SuggestionQuery", "i"))
        self.a_Key.setText(_translate("SuggestionQuery", "a"))
        self.p_Key.setText(_translate("SuggestionQuery", "p"))
        self.o_Key.setText(_translate("SuggestionQuery", "o"))
        self.s_Key.setText(_translate("SuggestionQuery", "s"))
        self.d_Key.setText(_translate("SuggestionQuery", "d"))
        self.f_Key.setText(_translate("SuggestionQuery", "f"))
        self.g_Key.setText(_translate("SuggestionQuery", "g"))
        self.h_Key.setText(_translate("SuggestionQuery", "h"))
        self.j_Key.setText(_translate("SuggestionQuery", "j"))
        self.k_Key.setText(_translate("SuggestionQuery", "k"))
        self.l_Key.setText(_translate("SuggestionQuery", "l"))
        self.z_Key.setText(_translate("SuggestionQuery", "z"))
        self.x_Key.setText(_translate("SuggestionQuery", "x"))
        self.c_Key.setText(_translate("SuggestionQuery", "c"))
        self.v_Key.setText(_translate("SuggestionQuery", "v"))
        self.b_Key.setText(_translate("SuggestionQuery", "b"))
        self.n_Key.setText(_translate("SuggestionQuery", "n"))
        self.m_Key.setText(_translate("SuggestionQuery", "m"))
        self.back_Key.setText(_translate("SuggestionQuery", "⌫"))
        self.space_Key.setText(_translate("SuggestionQuery", "Space"))
        self.enter_Button.setText(_translate("SuggestionQuery", "Enter"))
        self.back_Button.setText(_translate("SuggestionQuery", "Back"))
        self.label.setText(_translate("SuggestionQuery", "Welcome to"))
        self.label_2.setText(_translate("SuggestionQuery", "Suggestions"))
        self.label_3.setText(_translate("SuggestionQuery", "Please enter a keyword describing your symptoms so I can <br>provide you suggestions based on your current conditions."))

    def search_firestore(self, keyword):
        # Query the Firebase Realtime Database for keyword suggestions
        ref = self.db_ref.child("Keywords")
        results = ref.order_by_child("keyword").start_at(keyword).end_at(keyword + "\uf8ff").get()

        # Clear the current items in the suggestions list box
        self.suggestionsListBox.clear()

        if results:
            for key, value in results.items():
                if 'keyword' in value:
                    # Add the keyword to the list box
                    self.suggestionsListBox.addItem(value['keyword'])


    def update_text(self, letter):
        current_text = self.textBox1.text()
        self.textBox1.setText(current_text + letter)

    def add_space(self):
        current_text = self.textBox1.text()
        self.textBox1.setText(current_text + ' ')

    def backspace(self):
        current_text = self.textBox1.text()
        self.textBox1.setText(current_text[:-1])     

    def check_input(self):
        # Check if textBox1 is empty
        keyword = self.textBox1.text().strip()
        if keyword:
            self.search_firestore(keyword)
            self.open_main_suggestion(keyword)
        else:
            # Display message box indicating no input
            QtWidgets.QMessageBox.information(None, "Input Required", "Please enter a keyword before proceeding.")

    def open_main_suggestion(self, keyword):
        self.MainSuggestion_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainSuggestion()
        self.ui.setupUi(self.MainSuggestion_window, keyword)  # Pass the keyword
        self.MainSuggestion_window.show()
        self.centralwidget.window().close()  # Close the current window

    def text_changed(self):
        keyword = self.textBox1.text().strip().lower()
        if keyword:
            self.search_firestore(keyword)
            self.suggestionsListBox.setVisible(True)
        else:
            self.suggestionsListBox.clear()
            self.suggestionsListBox.setVisible(False)

    def find_closest_matches(self, keyword, values):
        closest_matches = []
        for value in values:
            if keyword in value.lower():  # Check if the keyword is a substring of the value
                closest_matches.append(value)
        return closest_matches

    def item_clicked(self, item):
            self.textBox1.setText(item.text())
            self.suggestionsListBox.setVisible(False)
    
    def BackToStart(self):
        from StartScreen import Ui_StartScreen
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_StartScreen()
        self.ui.setupUi(self.window)
        self.window.show()
        self.centralwidget.window().close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SuggestionQuery = QtWidgets.QMainWindow()
    ui = Ui_SuggestionQuery()
    ui.setupUi(SuggestionQuery)
    SuggestionQuery.show()
    sys.exit(app.exec_())
    