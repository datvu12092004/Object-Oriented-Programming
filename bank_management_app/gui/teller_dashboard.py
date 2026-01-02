from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from gui.deposit_gui import DepositGUI
from gui.withdraw_gui import WithdrawGUI
from gui.transfer_gui import TransferGUI # phan 3 them vao
from gui.history_gui import HistoryGUI

class TellerDashboard(QWidget):
    def __init__(self, nhan_vien):
        super().__init__()
        self.nv = nhan_vien
        self.setWindowTitle("Teller Dashboard - Nhân viên giao dịch")
        self.setGeometry(400, 200, 400, 300)

        lblWelcome = QLabel(f"Xin chào: {nhan_vien[1]}")
        lblWelcome.setStyleSheet("font-weight: bold; font-size: 14px;")

        btnDeposit = QPushButton("Nộp tiền")
        btnWithdraw = QPushButton("Rút tiền")

        btnDeposit.clicked.connect(self.open_deposit)
        btnWithdraw.clicked.connect(self.open_withdraw)
        
        btnTransfer = QPushButton("Chuyển khoản")        #phan 3 them vao
        btnHistory = QPushButton("Lịch sử giao dịch")

        btnTransfer.clicked.connect(lambda: TransferGUI(self.nv).show())   #phan 3 them vao
        btnHistory.clicked.connect(lambda: HistoryGUI().show())

        layout = QVBoxLayout()
        layout.addWidget(lblWelcome)
        layout.addWidget(btnDeposit)
        layout.addWidget(btnWithdraw)

        self.setLayout(layout)

    def open_deposit(self):
        self.depositWin = DepositGUI(self.nv)
        self.depositWin.show()

    def open_withdraw(self):
        self.withdrawWin = WithdrawGUI(self.nv)
        self.withdrawWin.show()
