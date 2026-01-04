from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox
)
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

        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels([
            "Mã GD", "Ngày giờ", "Loại",
            "Số tiền", "Nội dung", "Trạng thái"
        ])

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Số tài khoản"))
        layout.addWidget(self.txtTK)
        layout.addWidget(btn)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def load_history(self):
        so_tk = self.txtTK.text().strip()

        # 1. Chưa nhập số tài khoản
        if not so_tk:
            QMessageBox.warning(
                self,
                "Thiếu thông tin",
                "Vui lòng nhập số tài khoản"
            )
            self.txtTK.setFocus()
            return

        # 2. Gọi service
        ok, rows_or_msg = get_history_by_account(so_tk)

        # 3. Số tài khoản không tồn tại
        if not ok:
            QMessageBox.warning(
                self,
                "Lỗi",
                rows_or_msg
            )
            self.table.setRowCount(0)
            return

        rows = rows_or_msg

        # 4. Tồn tại tài khoản nhưng chưa có giao dịch
        if len(rows) == 0:
            QMessageBox.information(
                self,
                "Thông báo",
                "Tài khoản chưa có giao dịch nào"
            )
            self.table.setRowCount(0)
            return

        # 5. Hiển thị lịch sử giao dịch
        self.table.setRowCount(len(rows))
        for i, r in enumerate(rows):
            for j in range(6):
                self.table.setItem(i, j, QTableWidgetItem(str(r[j])))
