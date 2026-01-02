from PyQt5.QtWidgets import *
from services.customer_service import create_customer

class CustomerCreateGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đăng ký khách hàng mới")
        self.setGeometry(400, 220, 360, 380)

        self.inputs = {}
        fields = [
            ("Mã KH", "ma"),
            ("Họ tên", "ten"),
            ("Ngày sinh (YYYY-MM-DD)", "ngay"),
            ("Địa chỉ", "dc"),
            ("SĐT", "sdt"),
            ("Email", "email")
        ]

        layout = QVBoxLayout()
        for label, key in fields:
            layout.addWidget(QLabel(label))
            le = QLineEdit()
            self.inputs[key] = le
            layout.addWidget(le)

        btn = QPushButton("Tạo khách hàng")
        btn.clicked.connect(self.submit)
        layout.addWidget(btn)
        self.setLayout(layout)

    def submit(self):
        ok, msg = create_customer(
            self.inputs["ma"].text(),
            self.inputs["ten"].text(),
            self.inputs["ngay"].text(),
            self.inputs["dc"].text(),
            self.inputs["sdt"].text(),
            self.inputs["email"].text(),
        )
        QMessageBox.information(self, "Kết quả", msg if ok else f"Lỗi: {msg}")
