from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox,
    QTableWidget, QTableWidgetItem
)
from services.saving_service import open_saving


class SavingGUI(QWidget):
    def __init__(self, nhan_vien):
        super().__init__()
        self.nv = nhan_vien

        self.setWindowTitle("Gửi tiết kiệm")
        self.setGeometry(450, 200, 520, 420)

        self.txtTK = QLineEdit()
        self.txtTK.setPlaceholderText("Số tài khoản")

        self.txtTien = QLineEdit()
        self.txtTien.setPlaceholderText("Số tiền gửi")

        self.txtKyHan = QLineEdit()
        self.txtKyHan.setPlaceholderText("Kỳ hạn (tháng)")

        self.txtLai = QLineEdit()
        self.txtLai.setPlaceholderText("Lãi suất (%)")

        btn = QPushButton("Mở sổ tiết kiệm")
        btn.clicked.connect(self.do_open)

        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels([
            "Mã sổ", "Số TK", "Số tiền gửi",
            "Thời hạn", "Lãi suất", "Mã NV"
        ])
        self.table.setVisible(False)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Số tài khoản"))
        layout.addWidget(self.txtTK)
        layout.addWidget(QLabel("Số tiền gửi"))
        layout.addWidget(self.txtTien)
        layout.addWidget(QLabel("Kỳ hạn (tháng)"))
        layout.addWidget(self.txtKyHan)
        layout.addWidget(QLabel("Lãi suất (%)"))
        layout.addWidget(self.txtLai)
        layout.addWidget(btn)
        layout.addWidget(QLabel("Sổ tiết kiệm vừa mở"))
        layout.addWidget(self.table)

        self.setLayout(layout)

    def do_open(self):
        so_tk = self.txtTK.text().strip()
        if not so_tk:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập số tài khoản")
            return

        try:
            so_tien = float(self.txtTien.text())
            ky_han = int(self.txtKyHan.text())
            lai = float(self.txtLai.text())

            if so_tien <= 0 or ky_han <= 0 or lai <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Dữ liệu không hợp lệ")
            return

        ok, result = open_saving(
            so_tk,
            so_tien,
            ky_han,
            lai,
            self.nv[0]
        )

        if not ok:
            QMessageBox.warning(self, "Không thể mở sổ", result)
            return

        QMessageBox.information(self, "Thành công", "Mở sổ tiết kiệm thành công")
        self.show_saving(result)

        # Reset input
        self.txtTien.clear()
        self.txtKyHan.clear()
        self.txtLai.clear()

    def show_saving(self, s):
        self.table.setRowCount(1)
        self.table.setVisible(True)

        values = [
            s["MaTietKiem"],
            s["MaTaiKhoan"],
            f"{s['SoTienGui']:,}",
            s["ThoiHan"],
            f"{s['LaiSuat']}%",
            s["MaNV"]
        ]

        for i, v in enumerate(values):
            self.table.setItem(0, i, QTableWidgetItem(str(v)))
