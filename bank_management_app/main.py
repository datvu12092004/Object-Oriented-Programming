import sys
from PyQt5.QtWidgets import QApplication
from gui.role_select_gui import RoleSelectGUI


def main():
    app = QApplication(sys.argv)

    # LOAD THEME
    try:
        with open("styles/bank_theme.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Không tìm thấy file theme, chạy giao diện mặc định")

    win = RoleSelectGUI()
    win.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
