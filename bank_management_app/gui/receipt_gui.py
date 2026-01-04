from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class ReceiptGUI(QWidget):
    def __init__(self, giao_dich):
        super().__init__()
        self.setWindowTitle("Biên lai giao dịch")
        self.setGeometry(480, 260, 360, 240)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("BIÊN LAI GIAO DỊCH"))
        layout.addWidget(QLabel(f"Mã GD: {giao_dich['MaGiaoDich']}"))
        layout.addWidget(QLabel(f"Ngày giờ: {giao_dich['NgayGio']}"))
        layout.addWidget(QLabel(f"Loại GD: {giao_dich['LoaiGiaoDich']}"))
        layout.addWidget(QLabel(f"Số tiền: {giao_dich['SoTien']}"))
        layout.addWidget(QLabel(f"Nội dung: {giao_dich['NoiDung']}"))

        self.setLayout(layout)
