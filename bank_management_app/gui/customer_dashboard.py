from PyQt5.QtWidgets import *


class CustomerDashboard(QWidget):
    def __init__(self, kh):
        super().__init__()
        self.setWindowTitle("Trang khách hàng")
        self.setGeometry(400, 250, 500, 300)

        lbl = QLabel(f"Xin chào khách hàng: {kh[1]}")
        lbl.setStyleSheet("font-size:16px; font-weight:bold;")

        btnAcc = QPushButton("Xem tài khoản")
        btnHistory = QPushButton("Xem lịch sử giao dịch")

        layout = QVBoxLayout()
        layout.addWidget(lbl)
        layout.addWidget(btnAcc)
        layout.addWidget(btnHistory)

        self.setLayout(layout)
