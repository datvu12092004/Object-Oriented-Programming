from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from services.auth_service import login_customer
from gui.customer_dashboard import CustomerDashboard


class LoginCustomerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đăng nhập khách hàng")

        # Kích thước cửa sổ
        self.resize(420, 260)
        self.setMinimumSize(420, 260)

        # Căn giữa màn hình
        self.center()

        # ===== TITLE =====
        lblTitle = QLabel("ĐĂNG NHẬP KHÁCH HÀNG")
        lblTitle.setAlignment(Qt.AlignCenter)
        lblTitle.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
        """)

        lblSub = QLabel("Truy cập tài khoản cá nhân")
        lblSub.setAlignment(Qt.AlignCenter)
        lblSub.setStyleSheet("color: gray; font-size: 13px;")

        # ===== INPUTS =====
        self.txtPhone = QLineEdit()
        self.txtPhone.setPlaceholderText("Nhập số điện thoại")

        self.txtPass = QLineEdit()
        self.txtPass.setPlaceholderText("Nhập mật khẩu")
        self.txtPass.setEchoMode(QLineEdit.Password)

        for inp in (self.txtPhone, self.txtPass):
            inp.setFixedHeight(32)

        # ===== BUTTON =====
        btnLogin = QPushButton("Đăng nhập")
        btnLogin.setFixedHeight(40)
        btnLogin.clicked.connect(self.login)

        # ===== LAYOUT =====
        formLayout = QFormLayout()
        formLayout.setLabelAlignment(Qt.AlignLeft)
        formLayout.addRow("Số điện thoại:", self.txtPhone)
        formLayout.addRow("Mật khẩu:", self.txtPass)

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(40, 30, 40, 30)
        mainLayout.setSpacing(12)

        mainLayout.addWidget(lblTitle)
        mainLayout.addWidget(lblSub)
        mainLayout.addSpacing(15)
        mainLayout.addLayout(formLayout)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(btnLogin)

        self.setLayout(mainLayout)

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def login(self):
        sdt = self.txtPhone.text().strip()
        mat_khau = self.txtPass.text().strip()

        if not sdt or not mat_khau:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin")
            return

        kh = login_customer(sdt, mat_khau)
        if kh:
            self.main = CustomerDashboard(kh)
            self.main.show()
            self.close()
        else:
            QMessageBox.warning(self, "Đăng nhập thất bại", "Sai số điện thoại hoặc mật khẩu")
