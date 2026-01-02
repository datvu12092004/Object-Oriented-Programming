from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QApplication
)
from PyQt5.QtCore import Qt

from gui.deposit_gui import DepositGUI
from gui.withdraw_gui import WithdrawGUI
from gui.transfer_gui import TransferGUI
from gui.history_gui import HistoryGUI
from gui.customer_create_gui import CustomerCreateGUI
from gui.customer_search_gui import CustomerSearchGUI
from gui.saving_gui import SavingGUI


class TellerMainWindow(QWidget):
    def __init__(self, nhan_vien):
        super().__init__()
        self.nv = nhan_vien
        self.setWindowTitle("Bank Teller System")
        self.resize(1000, 600)

        mainLayout = QHBoxLayout(self)

        # ===== SIDEBAR =====
        self.sidebarLayout = QVBoxLayout()
        sidebarWidget = QWidget()
        sidebarWidget.setObjectName("Sidebar")
        sidebarWidget.setLayout(self.sidebarLayout)
        sidebarWidget.setFixedWidth(260)

        lblTitle = QLabel("BANK SYSTEM")
        lblTitle.setAlignment(Qt.AlignCenter)
        lblTitle.setStyleSheet("""
            color: #2c3e50;
            font-size: 20px;
            font-weight: bold;
        """)

        lblUser = QLabel(f"NV: {nhan_vien[1]}")
        lblUser.setAlignment(Qt.AlignCenter)
        lblUser.setStyleSheet("""
            color: #34495e;
            font-size: 14px;
        """)

        # ===== BUTTON FACTORY =====
        def make_btn(text):
            btn = QPushButton(text)
            btn.setFixedHeight(42)
            btn.setStyleSheet("font-size: 14px;")
            return btn

        # ===== BUTTONS =====
        btnDeposit = make_btn("Nộp tiền")
        btnWithdraw = make_btn("Rút tiền")
        btnTransfer = make_btn("Chuyển khoản")
        btnHistory = make_btn("Lịch sử giao dịch")
        btnSaving = make_btn("Gửi tiết kiệm")

        btnAddKH = make_btn("Đăng ký khách hàng")
        btnSearchKH = make_btn("Tra cứu khách hàng")

        btnLogout = make_btn("Đăng xuất")
        btnLogout.setStyleSheet("""
            background-color: #c0392b;
            color: white;
            font-size: 14px;
        """)

        # ===== ADD TO SIDEBAR =====
        self.sidebarLayout.addWidget(lblTitle)
        self.sidebarLayout.addWidget(lblUser)
        self.sidebarLayout.addSpacing(20)

        self.sidebarLayout.addWidget(btnDeposit)
        self.sidebarLayout.addWidget(btnWithdraw)
        self.sidebarLayout.addWidget(btnTransfer)
        self.sidebarLayout.addWidget(btnHistory)
        self.sidebarLayout.addWidget(btnSaving)

        self.sidebarLayout.addSpacing(15)
        self.sidebarLayout.addWidget(btnAddKH)
        self.sidebarLayout.addWidget(btnSearchKH)

        self.sidebarLayout.addStretch()
        self.sidebarLayout.addWidget(btnLogout)

        # ===== CONTENT =====
        self.content = QWidget()
        self.contentLayout = QVBoxLayout(self.content)

        lblWelcome = QLabel("Chào mừng đến hệ thống giao dịch ngân hàng")
        lblWelcome.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
        """)
        self.contentLayout.addWidget(lblWelcome)

        # ===== EVENTS =====
        btnDeposit.clicked.connect(lambda: self.load_widget(DepositGUI(self.nv)))
        btnWithdraw.clicked.connect(lambda: self.load_widget(WithdrawGUI(self.nv)))
        btnTransfer.clicked.connect(lambda: self.load_widget(TransferGUI(self.nv)))
        btnHistory.clicked.connect(lambda: self.load_widget(HistoryGUI()))
        btnSaving.clicked.connect(lambda: self.load_widget(SavingGUI()))

        btnAddKH.clicked.connect(lambda: self.load_widget(CustomerCreateGUI()))
        btnSearchKH.clicked.connect(lambda: self.load_widget(CustomerSearchGUI()))

        btnLogout.clicked.connect(self.close)

        mainLayout.addWidget(sidebarWidget)
        mainLayout.addWidget(self.content)

    def load_widget(self, widget):
        while self.contentLayout.count():
            child = self.contentLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.contentLayout.addWidget(widget)
