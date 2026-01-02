from PyQt5.QtWidgets import *
from services.customer_service import get_accounts_by_customer, update_account_status

class AccountManageGUI(QWidget):
    def __init__(self, ma_kh):
        super().__init__()
        self.setWindowTitle(f"Tài khoản của KH {ma_kh}")
        self.setGeometry(350, 220, 650, 360)

        self.ma_kh = ma_kh
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(
            ["Số TK", "Số dư", "Trạng thái", "Ngày mở"]
        )

        self.btnLock = QPushButton("Khóa tài khoản")
        self.btnUnlock = QPushButton("Mở khóa tài khoản")
        self.btnLock.clicked.connect(lambda: self.update_status("Khóa"))
        self.btnUnlock.clicked.connect(lambda: self.update_status("Hoạt động"))

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.btnLock)
        layout.addWidget(self.btnUnlock)
        self.setLayout(layout)

        self.load_data()

    def load_data(self):
        rows = get_accounts_by_customer(self.ma_kh)
        self.table.setRowCount(len(rows))
        for i, r in enumerate(rows):
            for j in range(4):
                self.table.setItem(i, j, QTableWidgetItem(str(r[j])))

    def update_status(self, status):
        row = self.table.currentRow()
        if row < 0:
            return
        so_tk = self.table.item(row, 0).text()
        ok, msg = update_account_status(so_tk, status)
        QMessageBox.information(self, "Kết quả", msg if ok else f"Lỗi: {msg}")
        if ok:
            self.load_data()
