bank_management_app/
│
├── gui/                # Giao diện PyQt5
│   ├── role_select_gui.py
│   ├── login_staff_gui.py
│   ├── login_customer_gui.py
│   ├── teller_main_window.py
│   ├── saving_gui.py
│   └── ...
│
├── services/           # Xử lý nghiệp vụ
│   ├── auth_service.py
│   ├── transaction_service.py
│   ├── saving_service.py
│   └── ...
│
├── database/           # Kết nối CSDL
│   └── db_connection.py
│
├── styles/             # Giao diện (QSS)
│   └── bank_theme.qss
│
├── main.py             # Entry point
└── README.md


===================================================

Công nghệ sử dụng

Python 3

PyQt5 – xây dựng giao diện desktop

SQL Server – quản lý dữ liệu

pyodbc – kết nối Python với SQL Server

UUID – sinh khóa chính
============================================

Hướng dẫn chạy chương trình
pip install pyqt5 pyodbc
database/db_connection.py
python main.py              // cần trỏ đến địa chỉ thư mục chứa dự án
