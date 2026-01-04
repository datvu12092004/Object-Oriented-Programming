from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from gui.login_staff_gui import LoginStaffGUI
from gui.login_customer_gui import LoginCustomerGUI


class RoleSelectGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hệ thống ngân hàng")

        # Kích thước cửa sổ
        self.resize(500, 300)
        self.setMinimumSize(500, 300)

        # Căn giữa màn hình
        self.center()

        # ===== TITLE =====
        lblTitle = QLabel("LỰA CHỌN ĐĂNG NHẬP")
        lblTitle.setAlignment(Qt.AlignCenter)
        lblTitle.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
        """)

        lblSub = QLabel("Vui lòng chọn vai trò truy cập hệ thống")
        lblSub.setAlignment(Qt.AlignCenter)
        lblSub.setStyleSheet("font-size: 13px; color: gray;")

        # ===== BUTTONS =====
        btnStaff = QPushButton("Nhân viên")
        btnCustomer = QPushButton("Khách hàng")

        for btn in (btnStaff, btnCustomer):
            btn.setFixedHeight(45)
            btn.setStyleSheet("""
                font-size: 15px;
            """)

        btnStaff.clicked.connect(self.open_staff_login)
        btnCustomer.clicked.connect(self.open_customer_login)

        # ===== LAYOUT =====
        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(15)
        mainLayout.setContentsMargins(40, 30, 40, 30)

        mainLayout.addWidget(lblTitle)
        mainLayout.addWidget(lblSub)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(btnStaff)
        mainLayout.addWidget(btnCustomer)
        mainLayout.addStretch()

        self.setLayout(mainLayout)

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def open_staff_login(self):
        self.login = LoginStaffGUI()
        self.login.show()
        self.close()

    def open_customer_login(self):
        self.login = LoginCustomerGUI()
        self.login.show()
        self.close()
