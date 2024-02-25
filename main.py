# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_in.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import colors


class MainWindow(object):
    def __init__(self):
        self.username = None

    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)
        main_window.setStyleSheet("")
        main_window.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.central_widget = QtWidgets.QStackedWidget(main_window)
        self.central_widget.setStyleSheet("#central_widget {\n"
                                         "    background-color: #050b10;\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.central_widget.setObjectName("central_widget")

        self.login_form = QtWidgets.QWidget()
        self.login_form.setEnabled(True)
        self.login_form.setGeometry(QtCore.QRect(420, 420, 321, 401))
        self.login_form.setFixedSize(321, 401)
        self.font = QtGui.QFont()
        self.font.setFamily("Segoe UI")
        self.login_form.setFont(self.font)
        self.login_form.setAcceptDrops(False)
        self.login_form.setAccessibleName("")
        self.login_form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_form.setAutoFillBackground(False)
        self.login_form.setStyleSheet("#login_form {\n"
                                      "    border: 10px;\n"
                                      "    border-radius: 10%;\n"
                                      "    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #050b10, stop:1 #12283a);\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.login_form.setObjectName("login_form")

        self.vertical_layout_widget = QtWidgets.QWidget(self.login_form)
        self.vertical_layout_widget.setGeometry(QtCore.QRect(20, 20, 281, 347))
        self.vertical_layout_widget.setObjectName("vertical_layout_widget")

        self.login_v_layout = QtWidgets.QVBoxLayout(self.vertical_layout_widget)
        self.login_v_layout.setContentsMargins(0, 0, 0, 0)
        self.login_v_layout.setSpacing(13)
        self.login_v_layout.setObjectName("login_v_layout")

        self.form_header = QtWidgets.QVBoxLayout()
        self.form_header.setObjectName("form_header")
        self.form_header_label = QtWidgets.QLabel(self.vertical_layout_widget)
        self.form_header_label.setFont(self.font)
        self.form_header_label.setStyleSheet("#form_header_label {\n"
                                             "    color: rgb(223, 236, 246);\n"
                                             "    font-weight: bold;\n"
                                             "    font-size: 28px;\n"
                                             "    background: transparent;\n"
                                             "}")
        self.form_header_label.setObjectName("form_header_label")
        self.form_header.addWidget(self.form_header_label)

        self.login_v_layout.addLayout(self.form_header)

        self.form_body = QtWidgets.QVBoxLayout()
        self.form_body.setContentsMargins(-1, -1, -1, 20)
        self.form_body.setObjectName("form_body")
        self.username_group = QtWidgets.QVBoxLayout()
        self.username_group.setObjectName("username_group")
        self.username_label = QtWidgets.QLabel(self.vertical_layout_widget)
        self.username_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username_label.setFont(self.font)
        self.username_label.setStyleSheet("#username_label {\n"
                                          "    color: #dfecf6;\n"
                                          "    font-weight: bold;\n"
                                          "    font-size: 14px;\n"
                                          "    background: transparent;\n"
                                          "}")
        self.username_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.username_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.username_label.setLineWidth(1)
        self.username_label.setScaledContents(False)
        self.username_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.username_label.setWordWrap(False)
        self.username_label.setIndent(-1)
        self.username_label.setObjectName("username_label")
        self.username_group.addWidget(self.username_label)
        self.username_input = QtWidgets.QLineEdit(self.vertical_layout_widget)
        self.username_input.setFont(self.font)
        self.username_input.setStyleSheet("#username_input {\n"
                                          "    border: 1.5px solid rgb(152, 195, 225);\n"
                                          "    background-color: transparent;\n"
                                          "    padding: 5px 10px;\n"
                                          "    border-radius: 5px;\n"
                                          "    height: 30px;\n"
                                          "    color: rgb(152, 195, 225);\n"
                                          "    font-size: 14px;\n"
                                          "}\n"
                                          "\n"
                                          "#username_input::placeholder { \n"
                                          "    color: rgb(152, 195, 255, .8);\n"
                                          "}")
        self.username_input.setText("")
        self.username_input.setObjectName("username_input")
        self.username_group.addWidget(self.username_input)

        self.form_body.addLayout(self.username_group)

        self.password_group = QtWidgets.QVBoxLayout()
        self.password_group.setObjectName("password_group")
        self.password_label = QtWidgets.QLabel(self.vertical_layout_widget)
        self.password_label.setFont(self.font)
        self.password_label.setStyleSheet("#password_label {\n"
                                          "    color: #dfecf6;\n"
                                          "    font-weight: bold;\n"
                                          "    font-size: 14px;\n"
                                          "    background: transparent;\n"
                                          "}")
        self.password_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.password_label.setIndent(-1)
        self.password_label.setObjectName("password_label")
        self.password_group.addWidget(self.password_label)

        self.password_input = QtWidgets.QLineEdit(self.vertical_layout_widget)
        self.password_input.setFont(self.font)
        self.password_input.setStyleSheet("#password_input {\n"
                                          "    border: 1.5px solid rgb(152, 195, 225);\n"
                                          "    background-color: transparent;\n"
                                          "    padding: 5px 10px;\n"
                                          "    border-radius: 5px;\n"
                                          "    height: 30px;\n"
                                          "    font-size: 14px;\n"
                                          "    color: rgb(152, 195, 225);\n"
                                          "}\n"
                                          "\n"
                                          "#password_input::placeholder { \n"
                                          "    color: rgb(152, 195, 255, .8);\n"
                                          "}")
        self.password_input.setObjectName("password_input")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_group.addWidget(self.password_input)

        self.form_body.addLayout(self.password_group)
        self.login_v_layout.addLayout(self.form_body)

        self.form_footer = QtWidgets.QVBoxLayout()
        self.form_footer.setContentsMargins(-1, 0, -1, 0)
        self.form_footer.setSpacing(6)
        self.form_footer.setObjectName("form_footer")

        self.sign_in_button = QtWidgets.QPushButton(self.vertical_layout_widget)
        self.sign_in_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sign_in_button.setFont(self.font)
        self.sign_in_button.setStyleSheet("#sign_in_button {\n"
                                          "    background-color: #98c3e1;\n"
                                          "    color: #050b10;\n"
                                          "    font-weight: bold;\n"
                                          "    padding-top: 15px;\n"
                                          "    padding-bottom: 15px;\n"
                                          "    border-radius: 5px;\n"
                                          "    font-size: 15px\n"        
                                          "}")
        self.sign_in_button.setObjectName("sign_in_button")
        self.sign_in_button.clicked.connect(self.handle_submit)

        self.form_footer.addWidget(self.sign_in_button)
        self.login_v_layout.addLayout(self.form_footer)
        self.login_v_layout.setStretch(0, 1)
        self.login_v_layout.setStretch(1, 3)
        self.login_v_layout.setStretch(2, 1)
        main_window.setCentralWidget(self.central_widget)

        self.central_widget.addWidget(self.login_form)

        self.dashboard = QtWidgets.QWidget()
        self.dashboard_layout = QtWidgets.QVBoxLayout()
        self.dashboard.setLayout(self.dashboard_layout)
        self.setup_dashboard()
        self.central_widget.addWidget(self.dashboard)

        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setStyleSheet("#menubar {\n"
                                   "    background-color: #050b10;\n"
                                   "    color: #dfecf6;\n"
                                   "}\n"
                                   "    ")
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setStyleSheet("#statusbar {\n"
                                     "    background-color: #050b10;\n"
                                     "}")
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.form_header_label.setText(_translate("main_window", "Sign In"))
        self.username_label.setText(_translate("main_window", "Username"))
        self.username_input.setPlaceholderText(_translate("main_window", "JohnDoe23"))
        self.password_label.setText(_translate("main_window", "Password"))
        self.password_input.setPlaceholderText(_translate("main_window", "PeTname$12"))
        self.sign_in_button.setText(_translate("main_window", "Sign In"))

    def setup_dashboard(self):
        self.dashboard_greeting = QtWidgets.QLabel()
        self.dashboard_greeting.setObjectName("dashboard_greeting")
        self.dashboard_greeting.setFont(self.font)
        self.dashboard_greeting.setAlignment(QtCore.Qt.AlignTop)
        self.dashboard_greeting.setStyleSheet("""
        #dashboard_greeting {
            color: $text;
            font-size: 20px;
        }
        """.replace('$text', colors.dark_mode_colors.get('text')))
        self.dashboard_layout.addWidget(self.dashboard_greeting)

    def show_dashboard(self):
        self.dashboard_greeting.setText("Hello, " + self.username)
        self.central_widget.setCurrentIndex(1)

    def handle_submit(self):
        # Check form state
        if self.username_input.text() == "username123" and self.password_input.text() == "password123":
            self.display_submit_message("success")

            self.username = self.username_input.text()
            self.show_dashboard()
        elif self.username_input.text() == "" or self.password_input.text() == "":
            self.display_submit_message("empty fields")
        elif self.username_input.text() != "username123":
            self.display_submit_message("no user")
        elif self.password_input.text() != "password123":
            self.display_submit_message("incorrect password")
        else:
            self.display_submit_message("incorrect password")

        # Clear form
        self.username_input.setText('')
        self.password_input.setText('')

    def display_submit_message(self, msg):
        submit_message = QtWidgets.QMessageBox()
        submit_message.setWindowTitle("Form Response")

        if msg == "success":
            submit_message.setIcon(QtWidgets.QMessageBox.Information)
            submit_message.setText("Sign In Success")
            submit_message.setInformativeText("You successfully signed in. Press Ok to continue.")
            submit_message.setStandardButtons(QtWidgets.QMessageBox.Ok)
        elif msg == "empty fields":
            submit_message.setIcon(QtWidgets.QMessageBox.Warning)
            submit_message.setText("Empty Fields")
            submit_message.setInformativeText("Fill in the empty fields to continue.")
            submit_message.setStandardButtons(QtWidgets.QMessageBox.Retry)
        elif msg == "no user":
            submit_message.setIcon(QtWidgets.QMessageBox.Warning)
            submit_message.setText("Unknown User")
            submit_message.setInformativeText("We were unable to find such a user in database. Try again.")
            submit_message.setStandardButtons(QtWidgets.QMessageBox.Retry)
        elif msg == "incorrect password":
            submit_message.setIcon(QtWidgets.QMessageBox.Warning)
            submit_message.setText("Incorrect Password")
            submit_message.setInformativeText("The Inserted password was incorrect. Try again.")
            submit_message.setStandardButtons(QtWidgets.QMessageBox.Retry)
        else:
            submit_message.setIcon(QtWidgets.QMessageBox.Warning)
            submit_message.setText("Unknown Error")
            submit_message.setInformativeText("There has been an unidentified error. Try again")
            submit_message.setStandardButtons(QtWidgets.QMessageBox.Retry)
        return submit_message.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())
