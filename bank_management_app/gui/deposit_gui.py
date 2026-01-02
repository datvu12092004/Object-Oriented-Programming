from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
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
        try:
            so_tien = float(self.txtTien.text())
            ok, msg = deposit(self.txtTK.text(), so_tien, self.nv[0])
            if ok:
                QMessageBox.information(self, "Thành công", msg)
            else:
                QMessageBox.warning(self, "Lỗi", msg)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Số tiền không hợp lệ")
