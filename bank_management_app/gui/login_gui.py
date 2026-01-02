from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QRadioButton, QMessageBox
)
from services.auth_service import login_employee, login_customer

class LoginGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đăng nhập hệ thống ngân hàng")
        self.setGeometry(500, 300, 360, 260)

        self.txtEmail = QLineEdit()
        self.txtEmail.setPlaceholderText("Email")

        self.txtPass = QLineEdit()
        self.txtPass.setPlaceholderText("Mật khẩu")
        self.txtPass.setEchoMode(QLineEdit.Password)

        self.rbNV = QRadioButton("Nhân viên")
        self.rbKH = QRadioButton("Khách hàng")
        self.rbNV.setChecked(True)

        btnLogin = QPushButton("Đăng nhập")
        btnLogin.clicked.connect(self.handle_login)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Email"))
        layout.addWidget(self.txtEmail)
        layout.addWidget(QLabel("Mật khẩu"))
        layout.addWidget(self.txtPass)
        layout.addWidget(self.rbNV)
        layout.addWidget(self.rbKH)
        layout.addWidget(btnLogin)

        self.setLayout(layout)

    def handle_login(self):
        email = self.txtEmail.text().strip()
        password = self.txtPass.text().strip()

        if not email or not password:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập đủ Email và Mật khẩu.")
            return

        if self.rbNV.isChecked():
            nv = login_employee(email, password)
            if nv:
                QMessageBox.information(self, "Thành công", "Đăng nhập nhân viên thành công.")
                # PHẦN 2 sẽ mở Teller Dashboard tại đây


                #from gui.teller_dashboard import TellerDashboard   # Phan 2 them vao
               # self.dashboard = TellerDashboard(nv)
                #self.dashboard.show()
                #self.close()
                from gui.teller_main_window import TellerMainWindow   # Phan 4 them vao
                self.dashboard = TellerMainWindow(nv)
                self.dashboard.show()
                self.close()



            else:
                QMessageBox.warning(self, "Lỗi", "Sai thông tin nhân viên.")
        else:
            kh = login_customer(email, password)
            if kh:
                QMessageBox.information(self, "Thành công", "Đăng nhập khách hàng thành công.")
                # PHẦN 2 sẽ mở Customer Dashboard tại đây
            else:
                QMessageBox.warning(self, "Lỗi", "Sai thông tin khách hàng.")
