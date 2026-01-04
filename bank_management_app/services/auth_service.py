from database.db_connection import get_connection


def login_staff(ma_nv, mat_khau):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM dbo.NhanVien
        WHERE MaNV = ? AND MatKhau = ?
    """, (ma_nv, mat_khau))
    row = cur.fetchone()
    conn.close()
    return row


def login_customer(sdt, mat_khau):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM dbo.KhachHang kh
        JOIN dbo.TaiKhoan tk ON kh.MaKH = tk.MaKH
        WHERE kh.SDT = ? AND tk.MatKhau = ?
    """, (sdt, mat_khau))
    row = cur.fetchone()
    conn.close()
    return row
