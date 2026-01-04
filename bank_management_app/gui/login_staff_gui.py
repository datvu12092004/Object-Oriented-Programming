from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from services.auth_service import login_staff
from gui.teller_main_window import TellerMainWindow


class LoginStaffGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đăng nhập nhân viên")

        # Kích thước cửa sổ
        self.resize(420, 260)
        self.setMinimumSize(420, 260)

        # Căn giữa màn hình
        self.center()

        # ===== TITLE =====
        lblTitle = QLabel("ĐĂNG NHẬP NHÂN VIÊN")
        lblTitle.setAlignment(Qt.AlignCenter)
        lblTitle.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
        """)

        lblSub = QLabel("Hệ thống giao dịch nội bộ")
        lblSub.setAlignment(Qt.AlignCenter)
        lblSub.setStyleSheet("color: gray; font-size: 13px;")

        # ===== INPUTS =====
        self.txtMaNV = QLineEdit()
        self.txtMaNV.setPlaceholderText("Nhập mã nhân viên")

        self.txtPass = QLineEdit()
        self.txtPass.setPlaceholderText("Nhập mật khẩu")
        self.txtPass.setEchoMode(QLineEdit.Password)

        for inp in (self.txtMaNV, self.txtPass):
            inp.setFixedHeight(32)

        # ===== BUTTON =====
        btnLogin = QPushButton("Đăng nhập")
        btnLogin.setFixedHeight(40)
        btnLogin.clicked.connect(self.login)

        # ===== LAYOUT =====
        formLayout = QFormLayout()
        formLayout.addRow("Mã nhân viên:", self.txtMaNV)
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
        ma_nv = self.txtMaNV.text().strip()
        mat_khau = self.txtPass.text().strip()

        if not ma_nv or not mat_khau:
            QMessageBox.warning(
                self,
                "Thiếu thông tin",
                "Vui lòng nhập đầy đủ mã nhân viên và mật khẩu"
            )
            return

        nv = login_staff(ma_nv, mat_khau)

        if not nv:
            QMessageBox.warning(
                self,
                "Đăng nhập thất bại",
                "Sai mã nhân viên hoặc mật khẩu"
            )
            return

        # ===== PHÂN QUYỀN THEO CHỨC VỤ =====
        chuc_vu = nv[5]   # Cột ChucVu trong bảng NhanVien

        if chuc_vu != "Giao dịch":
            QMessageBox.warning(
                self,
                "Từ chối truy cập",
                "Tài khoản của bạn không có quyền truy cập các chức năng giao dịch"
            )
            return

        # ===== ĐÚNG VAI TRÒ → MỞ GIAO DIỆN =====
        self.main = TellerMainWindow(nv)
        self.main.show()
        self.close()
