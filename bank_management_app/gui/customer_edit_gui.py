from PyQt5.QtWidgets import *
from services.customer_service import get_customer_by_id, update_customer

class CustomerEditGUI(QWidget):
    def __init__(self, ma_kh):
        super().__init__()
        self.ma_kh = ma_kh
        self.setWindowTitle("Chỉnh sửa thông tin khách hàng")
        self.setGeometry(420, 240, 360, 360)

        self.inputs = {}

        labels = [
            ("Họ tên", "HoTen"),
            ("Ngày sinh (YYYY-MM-DD)", "NgaySinh"),
            ("Địa chỉ", "DiaChi"),
            ("SĐT", "SDT"),
            ("Email", "Email")
        ]

        layout = QVBoxLayout()

        for text, key in labels:
            layout.addWidget(QLabel(text))
            le = QLineEdit()
            self.inputs[key] = le
            layout.addWidget(le)

        btnSave = QPushButton("Lưu thay đổi")
        btnSave.clicked.connect(self.save)

        layout.addWidget(btnSave)
        self.setLayout(layout)

        self.load_data()

    def load_data(self):
        row = get_customer_by_id(self.ma_kh)
        if row:
            self.inputs["HoTen"].setText(row[1])
            self.inputs["NgaySinh"].setText(str(row[2]))
            self.inputs["DiaChi"].setText(row[3])
            self.inputs["SDT"].setText(row[4])
            self.inputs["Email"].setText(row[5])

    def save(self):
        ok, msg = update_customer(
            self.ma_kh,
            self.inputs["HoTen"].text(),
            self.inputs["NgaySinh"].text(),
            self.inputs["DiaChi"].text(),
            self.inputs["SDT"].text(),
            self.inputs["Email"].text()
        )
        QMessageBox.information(self, "Kết quả", msg)
        if ok:
            self.close()
