from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox,
    QTableWidget, QTableWidgetItem
)
from services.transaction_service import withdraw


class WithdrawGUI(QWidget):
    def __init__(self, nhan_vien):
        super().__init__()
        self.nv = nhan_vien

        self.setWindowTitle("Rút tiền")
        self.setGeometry(450, 200, 500, 380)

        # ===== INPUT =====
        self.txtTK = QLineEdit()
        self.txtTK.setPlaceholderText("Số tài khoản")

        self.txtTien = QLineEdit()
        self.txtTien.setPlaceholderText("Số tiền")

        btn = QPushButton("Thực hiện rút tiền")
        btn.clicked.connect(self.do_withdraw)

        # ===== TABLE HIỂN THỊ GIAO DỊCH =====
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels([
            "Mã GD", "Số TK", "Số tiền", "Loại GD", "Mã NV"
        ])
        self.table.setVisible(False)

        # ===== LAYOUT =====
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Số tài khoản"))
        layout.addWidget(self.txtTK)
        layout.addWidget(QLabel("Số tiền"))
        layout.addWidget(self.txtTien)
        layout.addWidget(btn)
        layout.addWidget(QLabel("Giao dịch vừa thực hiện"))
        layout.addWidget(self.table)

        self.setLayout(layout)

    def do_withdraw(self):
        so_tk = self.txtTK.text().strip()
        so_tien_text = self.txtTien.text().strip()

        # 1. Validate
        if not so_tk:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập số tài khoản")
            return

        try:
            so_tien = float(so_tien_text)
            if so_tien <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Số tiền không hợp lệ")
            return

        # 2. Gọi service
        ok, result = withdraw(so_tk, so_tien, self.nv[0])

        if not ok:
            QMessageBox.warning(self, "Không thể rút tiền", result)
            return

        # 3. Thành công
        QMessageBox.information(self, "Thành công", "Rút tiền thành công")
        self.show_transaction(result)

        self.txtTien.clear()

    def show_transaction(self, gd):
        self.table.setRowCount(1)
        self.table.setVisible(True)

        values = [
            gd["MaGiaoDich"],
            gd["SoTaiKhoan"],
            f"{gd['SoTien']:,}",
            gd["LoaiGiaoDich"],
            gd["MaNV"]
        ]

        for col, val in enumerate(values):
            self.table.setItem(0, col, QTableWidgetItem(str(val)))
