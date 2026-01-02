from PyQt5.QtWidgets import *
from services.saving_service import open_saving_account


class SavingGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gửi tiết kiệm")

        self.txtSoTK = QLineEdit()
        self.txtSoTien = QLineEdit()
        self.txtThoiHan = QLineEdit()
        self.txtLaiSuat = QLineEdit()

        btn = QPushButton("Xác nhận gửi tiết kiệm")
        btn.clicked.connect(self.submit)

        layout = QFormLayout()
        layout.addRow("Số tài khoản:", self.txtSoTK)
        layout.addRow("Số tiền gửi:", self.txtSoTien)
        layout.addRow("Thời hạn (tháng):", self.txtThoiHan)
        layout.addRow("Lãi suất (%):", self.txtLaiSuat)
        layout.addRow(btn)

        self.setLayout(layout)

    def submit(self):
        ok, msg = open_saving_account(
            self.txtSoTK.text(),
            float(self.txtSoTien.text()),
            int(self.txtThoiHan.text()),
            float(self.txtLaiSuat.text())
        )

        if ok:
            QMessageBox.information(self, "Thành công", msg)
            self.close()
        else:
            QMessageBox.warning(self, "Lỗi", msg)
