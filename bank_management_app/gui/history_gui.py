from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem
from services.transaction_service import get_history_by_account

class HistoryGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lịch sử giao dịch")
        self.setGeometry(300, 200, 700, 400)

        self.txtTK = QLineEdit()
        self.txtTK.setPlaceholderText("Nhập số tài khoản")

        btn = QPushButton("Xem lịch sử")
        btn.clicked.connect(self.load_history)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Mã GD", "Ngày giờ", "Loại", "Số tiền", "Nội dung", "Trạng thái"
        ])

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Số tài khoản"))
        layout.addWidget(self.txtTK)
        layout.addWidget(btn)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def load_history(self):
        rows = get_history_by_account(self.txtTK.text())
        self.table.setRowCount(len(rows))
        for i, r in enumerate(rows):
            for j in range(6):
                self.table.setItem(i, j, QTableWidgetItem(str(r[j])))
