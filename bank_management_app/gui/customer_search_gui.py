from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox
)
from services.customer_service import search_customer
from gui.account_manage_gui import AccountManageGUI
from gui.customer_edit_gui import CustomerEditGUI


class CustomerSearchGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tra cứu khách hàng")
        self.setGeometry(300, 200, 700, 420)

        # Ô nhập tìm kiếm
        self.txt = QLineEdit()
        self.txt.setPlaceholderText("Nhập mã KH hoặc tên")

        # Nút tìm kiếm
        btn = QPushButton("Tìm kiếm")
        btn.clicked.connect(self.search)

        # Bảng kết quả
        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels(
            ["MaKH", "Họ tên", "Ngày sinh", "Địa chỉ", "SĐT", "Email"]
        )

        # Double click để chọn thao tác
        self.table.doubleClicked.connect(self.open_menu)

        layout = QVBoxLayout()
        layout.addWidget(self.txt)
        layout.addWidget(btn)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def search(self):
        keyword = self.txt.text().strip()

        # 1. Chưa nhập gì
        if not keyword:
            QMessageBox.warning(
                self,
                "Thiếu thông tin",
                "Vui lòng nhập mã hoặc tên khách hàng"
            )
            self.txt.setFocus()
            return

        rows = search_customer(keyword)

        # 2. Không tồn tại khách hàng
        if not rows:
            QMessageBox.information(
                self,
                "Không tìm thấy",
                "Không tồn tại khách hàng với thông tin đã nhập"
            )
            self.table.setRowCount(0)
            return

        # 3. Có dữ liệu
        self.table.setRowCount(len(rows))
        for i, r in enumerate(rows):
            for j in range(6):
                self.table.setItem(i, j, QTableWidgetItem(str(r[j])))

    def open_menu(self):
        # Không cho thao tác khi bảng rỗng
        if self.table.rowCount() == 0:
            return

        row = self.table.currentRow()
        if row < 0:
            return

        ma_kh = self.table.item(row, 0).text()

        menu = QMessageBox(self)
        menu.setWindowTitle("Chọn thao tác")
        menu.setText(f"Khách hàng: {ma_kh}")

        btnEdit = menu.addButton("Chỉnh sửa thông tin", QMessageBox.AcceptRole)
        btnAccount = menu.addButton("Xem tài khoản", QMessageBox.ActionRole)
        menu.addButton("Hủy", QMessageBox.RejectRole)

        menu.exec_()

        if menu.clickedButton() == btnEdit:
            self.editWin = CustomerEditGUI(ma_kh)
            self.editWin.show()

        elif menu.clickedButton() == btnAccount:
            self.accWin = AccountManageGUI(ma_kh)
            self.accWin.show()
