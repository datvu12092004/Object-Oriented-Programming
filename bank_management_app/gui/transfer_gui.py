from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox,
    QTableWidget, QTableWidgetItem
)
from services.transaction_service import transfer


class TransferGUI(QWidget):
    def __init__(self, nhan_vien):
        super().__init__()
        self.nv = nhan_vien

        self.setWindowTitle("Chuyển khoản")
        self.setGeometry(450, 200, 520, 420)

        # ===== INPUT =====
        self.txtNguon = QLineEdit()
        self.txtNguon.setPlaceholderText("TK nguồn")

        self.txtDich = QLineEdit()
        self.txtDich.setPlaceholderText("TK đích")

        self.txtTien = QLineEdit()
        self.txtTien.setPlaceholderText("Số tiền")

        btn = QPushButton("Thực hiện chuyển khoản")
        btn.clicked.connect(self.do_transfer)

        # ===== TABLE HIỂN THỊ GIAO DỊCH =====
        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels([
            "Mã GD", "TK nguồn", "TK đích",
            "Số tiền", "Loại GD", "Mã NV"
        ])
        self.table.setVisible(False)

        # ===== LAYOUT =====
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Tài khoản nguồn"))
        layout.addWidget(self.txtNguon)
        layout.addWidget(QLabel("Tài khoản đích"))
        layout.addWidget(self.txtDich)
        layout.addWidget(QLabel("Số tiền"))
        layout.addWidget(self.txtTien)
        layout.addWidget(btn)
        layout.addWidget(QLabel("Giao dịch vừa thực hiện"))
        layout.addWidget(self.table)

        self.setLayout(layout)

    def do_transfer(self):
        so_tk_nguon = self.txtNguon.text().strip()
        so_tk_dich = self.txtDich.text().strip()
        so_tien_text = self.txtTien.text().strip()

        # 1. Validate
        if not so_tk_nguon or not so_tk_dich:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập đầy đủ số tài khoản")
            return

        if so_tk_nguon == so_tk_dich:
            QMessageBox.warning(self, "Lỗi", "Tài khoản nguồn và đích không được trùng nhau")
            return

        try:
            so_tien = float(so_tien_text)
            if so_tien <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Số tiền không hợp lệ")
            return

        # 2. Gọi service
        ok, result = transfer(so_tk_nguon, so_tk_dich, so_tien, self.nv[0])

        if not ok:
            QMessageBox.warning(self, "Không thể chuyển khoản", result)
            return

        # 3. Thành công
        QMessageBox.information(self, "Thành công", "Chuyển khoản thành công")
        self.show_transaction(result)

        self.txtTien.clear()

    def show_transaction(self, gd):
        self.table.setRowCount(1)
        self.table.setVisible(True)

        values = [
            gd["MaGiaoDich"],
            gd["TuTK"],
            gd["DenTK"],
            f"{gd['SoTien']:,}",
            gd["LoaiGiaoDich"],
            gd["MaNV"]
        ]

        for col, val in enumerate(values):
            self.table.setItem(0, col, QTableWidgetItem(str(val)))
