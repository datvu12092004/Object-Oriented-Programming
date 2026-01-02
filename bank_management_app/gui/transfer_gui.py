from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from services.transaction_service import transfer

class TransferGUI(QWidget):
    def __init__(self, nhan_vien):
        super().__init__()
        self.nv = nhan_vien
        self.setWindowTitle("Chuyển khoản nội bộ")
        self.setGeometry(450, 240, 320, 260)

        self.txtSrc = QLineEdit()
        self.txtSrc.setPlaceholderText("TK nguồn")

        self.txtDst = QLineEdit()
        self.txtDst.setPlaceholderText("TK đích")

        self.txtTien = QLineEdit()
        self.txtTien.setPlaceholderText("Số tiền")

        btn = QPushButton("Thực hiện chuyển khoản")
        btn.clicked.connect(self.do_transfer)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Tài khoản nguồn"))
        layout.addWidget(self.txtSrc)
        layout.addWidget(QLabel("Tài khoản đích"))
        layout.addWidget(self.txtDst)
        layout.addWidget(QLabel("Số tiền"))
        layout.addWidget(self.txtTien)
        layout.addWidget(btn)
        self.setLayout(layout)

    def do_transfer(self):
        try:
            so_tien = float(self.txtTien.text())
            ok, msg = transfer(
                self.txtSrc.text(),
                self.txtDst.text(),
                so_tien,
                self.nv[0]
            )
            if ok:
                QMessageBox.information(self, "Thành công", msg)
            else:
                QMessageBox.warning(self, "Lỗi", msg)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Số tiền không hợp lệ")
