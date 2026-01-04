from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox
)
from services.transaction_service import deposit


class DepositGUI(QWidget):
    def __init__(self, nhan_vien):
        super().__init__()
        self.nv = nhan_vien

        self.setWindowTitle("Nộp tiền")
        self.setGeometry(450, 250, 300, 220)

        self.txtTK = QLineEdit()
        self.txtTK.setPlaceholderText("Số tài khoản")

        self.txtTien = QLineEdit()
        self.txtTien.setPlaceholderText("Số tiền")

        btn = QPushButton("Thực hiện nộp tiền")
        btn.clicked.connect(self.do_deposit)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Số tài khoản"))
        layout.addWidget(self.txtTK)
        layout.addWidget(QLabel("Số tiền"))
        layout.addWidget(self.txtTien)
        layout.addWidget(btn)

        self.setLayout(layout)

    def do_deposit(self):
        so_tk = self.txtTK.text().strip()
        so_tien_text = self.txtTien.text().strip()

        # 1. Kiểm tra nhập số tài khoản
        if not so_tk:
            QMessageBox.warning(
                self,
                "Thiếu thông tin",
                "Vui lòng nhập số tài khoản"
            )
            self.txtTK.setFocus()
            return

        # 2. Kiểm tra số tiền
        try:
            so_tien = float(so_tien_text)
            if so_tien <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Số tiền không hợp lệ"
            )
            self.txtTien.setFocus()
            return

        # 3. Thực hiện nộp tiền
        ok, msg = deposit(so_tk, so_tien, self.nv[0])

        # 4. Thông báo kết quả (bao gồm sai số tài khoản)
        if ok:
            QMessageBox.information(self, "Thành công", msg)
            self.txtTK.clear()
            self.txtTien.clear()
        else:
            QMessageBox.warning(self, "Không thể nộp tiền", msg)
