from database.db_connection import get_connection

def create_customer(ma_kh, ho_ten, ngay_sinh, dia_chi, sdt, email):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO KhachHang (MaKH, HoTen, NgaySinh, DiaChi, SDT, Email)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (ma_kh, ho_ten, ngay_sinh, dia_chi, sdt, email))
        conn.commit()
        return True, "Tạo khách hàng thành công"
    except Exception as e:
        conn.rollback()
        return False, str(e)
    finally:
        conn.close()

def search_customer(keyword):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT MaKH, HoTen, NgaySinh, DiaChi, SDT, Email
        FROM KhachHang
        WHERE MaKH LIKE ? OR HoTen LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    rows = cur.fetchall()
    conn.close()
    return rows

def get_accounts_by_customer(ma_kh):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT SoTaiKhoan, SoDu, TrangThai, NgayMo
        FROM TaiKhoan
        WHERE MaKH = ?
    """, (ma_kh,))
    rows = cur.fetchall()
    conn.close()
    return rows

def update_account_status(so_tk, trang_thai):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            UPDATE TaiKhoan SET TrangThai = ?
            WHERE SoTaiKhoan = ?
        """, (trang_thai, so_tk))
        conn.commit()
        return True, "Cập nhật trạng thái tài khoản thành công"
    except Exception as e:
        conn.rollback()
        return False, str(e)
    finally:
        conn.close()

def get_customer_by_id(ma_kh):     #them chinh sua thong tin khach hang
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT MaKH, HoTen, NgaySinh, DiaChi, SDT, Email
        FROM KhachHang
        WHERE MaKH = ?
    """, (ma_kh,))
    row = cur.fetchone()
    conn.close()
    return row


def update_customer(ma_kh, ho_ten, ngay_sinh, dia_chi, sdt, email):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            UPDATE KhachHang
            SET HoTen = ?, NgaySinh = ?, DiaChi = ?, SDT = ?, Email = ?
            WHERE MaKH = ?
        """, (ho_ten, ngay_sinh, dia_chi, sdt, email, ma_kh))
        conn.commit()
        return True, "Cập nhật thông tin khách hàng thành công"
    except Exception as e:
        conn.rollback()
        return False, str(e)
    finally:
        conn.close()
