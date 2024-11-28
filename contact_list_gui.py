import psycopg2 as psg
from PyQt6.QtWidgets import QApplication,QGridLayout,QLabel,QLineEdit,QMainWindow,\
    QTableWidget,QTableWidgetItem,\
    QVBoxLayout,QDialog,QComboBox,QPushButton,QToolBar,QStatusBar,QMessageBox,QWidget
from PyQt6.QtGui import QAction,QIcon
import sys

class DBConnection:
    pass


class ContactList(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Contact List App")
        self.setFixedWidth(200)
        self.setFixedHeight(200)

        layout=QGridLayout()

        self.user_name_label=QLabel("UserName")
        layout.addWidget(self.user_name_label,0,0)
        self.user_name_editor=QLineEdit()
        layout.addWidget(self.user_name_editor,1,0)
        self.pwd_label=QLabel("PassWord")
        layout.addWidget(self.pwd_label)
        self.pwd_editor=QLineEdit()
        layout.addWidget(self.pwd_editor)

        self.sign_in_button=QPushButton("Sign In")
        self.sign_in_button.clicked.connect(self.sign_in_method)
        layout.addWidget(self.sign_in_button)
        self.sign_up_button = QPushButton("Sign UP")
        self.sign_up_button.clicked.connect(self.sign_up_method)
        layout.addWidget(self.sign_up_button)


        self.setLayout(layout)

    def sign_up_method(self):
        sign_up=SignUpPage()
        sign_up.exec()

    def sign_in_method(self):
        dailog=SignInPage()
        dailog.exec()

class SignInPage(QMainWindow):
    def __init__(self):
        super().__init__()
        layout=QGridLayout()

        #print("insdide new class")
        self.setWindowTitle("Contact App Details")
        self.table = QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(("Contact Name", "Phone Number", "Email Address"))
        layout.addWidget(self.table)

        self.setLayout(layout)

        def valid_check(self):
            # print("enter sign_in main method")
            connection = psg.connect(dbname="python_practice", user="postgres",
                                     password="admin", host="localhost", port=5432)
            cursor = connection.cursor()
            cursor.execute("select * from contact_list where contact_name=%s and contact_password=%s",
                           ((self.user_name_editor.text(), self.pwd_editor.text())))
            res = cursor.fetchall()
            cursor.close()
            connection.close()
            print("connection tested to check sing validity")
            if res:
                print(res)
                self.table_display()
            else:
                print("signup method again due to invalid credentials")
                self.sign_up_method()

        def table_display(self):

            connection = psg.connect(dbname="python_practice", user="postgres",
                                     password="admin", host="localhost", port=5432)
            cursor = connection.cursor()
            cursor.execute("select contact_name,contact_number,contact_emial from contact_list ")
            res = cursor.fetchall()
            print("after db connection in new class")

            self.table.setRowCount(0)
            for row_number, row_data in enumerate(res):
                print("any issue here?")
                self.table.insertRow(row_number)
                for column_num, data in enumerate(row_data):
                    self.table.setItem(row_number, column_num, QTableWidgetItem(str(data)))
        self.setCentralWidget(self.table)




class SignUpPage(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SignIn Page")
        self.setMaximumSize(300,400)

        SignUP_layout=QVBoxLayout()

        self.name_label=QLabel("Contact Name")
        SignUP_layout.addWidget(self.name_label)
        self.contact_name_editor=QLineEdit()
        SignUP_layout.addWidget(self.contact_name_editor)

        self.phone_label = QLabel("Phone Number")
        SignUP_layout.addWidget(self.phone_label)
        self.contact_phone_editor=QLineEdit()
        SignUP_layout.addWidget(self.contact_phone_editor)

        self.mail_label = QLabel("Contact Email")
        SignUP_layout.addWidget(self.mail_label)
        self.contact_email_editor=QLineEdit()
        SignUP_layout.addWidget(self.contact_email_editor)

        self.password = QLabel("Password")
        SignUP_layout.addWidget(self.password)
        self.contact_password_editor = QLineEdit()
        SignUP_layout.addWidget(self.contact_password_editor)



        self.Submit_button=QPushButton("Submit")
        SignUP_layout.addWidget(self.Submit_button)

        self.Submit_button.clicked.connect(self.insert_data)


        self.setLayout(SignUP_layout)

    def insert_data(self):
        connection = psg.connect(dbname="python_practice", user="postgres",
                                 password="admin", host="localhost", port=5432)
        #connection=DBConnection()
        #connection_name=connection.self.connection
        cursor=connection.cursor()
        cursor.execute(f"insert into contact_list (contact_name,contact_number,contact_emial,contact_password) values (%s,%s,%s,%s) ",
                       ((self.contact_name_editor.text(),
                         self.contact_phone_editor.text(),
                         self.contact_email_editor.text(),
                         self.contact_password_editor.text())))

        connection.commit()
        cursor.close()
        connection.close()
        self.close()




app=QApplication(sys.argv)
concat_app =ContactList()
concat_app.show()
#signin=SignInPage()
#signin.show()
sys.exit(app.exec())


