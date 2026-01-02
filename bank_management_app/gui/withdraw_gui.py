from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from services.transaction_service import withdraw

class WithdrawGUI(QWidget):
    def __init__(self, nhan_vien):
        super().__init__()
        self.nv = nhan_vien
        self.setWindowTitle("Rút tiền")
        self.setGeometry(450, 250, 300, 220)

        self.txtTK = QLineEdit()
        self.txtTK.setPlaceholderText("Số tài khoản")

        self.txtTien = QLineEdit()
        self.txtTien.setPlaceholderText("Số tiền")

        btn = QPushButton("Thực hiện rút tiền")
        btn.clicked.connect(self.do_withdraw)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Số tài khoản"))
        layout.addWidget(self.txtTK)
        layout.addWidget(QLabel("Số tiền"))
        layout.addWidget(self.txtTien)
        layout.addWidget(btn)

        self.setLayout(layout)

    def do_withdraw(self):
        try:
            so_tien = float(self.txtTien.text())
            ok, msg = withdraw(self.txtTK.text(), so_tien, self.nv[0])
            if ok:
                QMessageBox.information(self, "Thành công", msg)
            else:
                QMessageBox.warning(self, "Lỗi", msg)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Số tiền không hợp lệ")
