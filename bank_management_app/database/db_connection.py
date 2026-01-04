import pyodbc

def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=VTDLAPTOP;"
        "DATABASE=quan_ly_ngan_hang;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
