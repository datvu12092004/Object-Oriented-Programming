import uuid
from database.db_connection import get_connection


def deposit(so_tk, so_tien, ma_nv):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            UPDATE dbo.TaiKhoan
            SET SoDu = SoDu + ?
            WHERE SoTaiKhoan = ? AND TrangThai = N'Hoạt động'
        """, (so_tien, so_tk))

        if cur.rowcount == 0:
            raise Exception("Không cập nhật được số dư tài khoản")

        ma_gd = str(uuid.uuid4())

        cur.execute("""
            INSERT INTO dbo.GiaoDich
            (MaGiaoDich, NgayGio, SoTien, LoaiGiaoDich, NoiDung, TrangThai, SoTaiKhoan, MaNVGiaoDich)
            VALUES (?, GETDATE(), ?, N'Nộp tiền', N'Nộp tại quầy', N'Hoàn thành', ?, ?)
        """, (ma_gd, so_tien, so_tk, ma_nv))

        conn.commit()
        return True, "Nộp tiền thành công"

    except Exception as e:
        conn.rollback()
        return False, str(e)

    finally:
        conn.close()


def withdraw(so_tk, so_tien, ma_nv):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT SoDu FROM dbo.TaiKhoan
            WHERE SoTaiKhoan = ? AND TrangThai = N'Hoạt động'
        """, (so_tk,))
        row = cur.fetchone()
        if not row:
            raise Exception("Tài khoản không tồn tại hoặc không hoạt động")

        if row[0] < so_tien:
            raise Exception("Số dư không đủ")

        cur.execute("""
            UPDATE dbo.TaiKhoan
            SET SoDu = SoDu - ?
            WHERE SoTaiKhoan = ?
        """, (so_tien, so_tk))

        if cur.rowcount == 0:
            raise Exception("Không cập nhật được số dư")

        ma_gd = str(uuid.uuid4())

        cur.execute("""
            INSERT INTO dbo.GiaoDich
            (MaGiaoDich, NgayGio, SoTien, LoaiGiaoDich, NoiDung, TrangThai, SoTaiKhoan, MaNVGiaoDich)
            VALUES (?, GETDATE(), ?, N'Rút tiền', N'Rút tại quầy', N'Hoàn thành', ?, ?)
        """, (ma_gd, so_tien, so_tk, ma_nv))

        conn.commit()
        return True, "Rút tiền thành công"

    except Exception as e:
        conn.rollback()
        return False, str(e)

    finally:
        conn.close()


def transfer(so_tk_nguon, so_tk_dich, so_tien, ma_nv):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT SoDu FROM dbo.TaiKhoan
            WHERE SoTaiKhoan = ? AND TrangThai = N'Hoạt động'
        """, (so_tk_nguon,))
        src = cur.fetchone()
        if not src:
            raise Exception("TK nguồn không tồn tại hoặc không hoạt động")
        if src[0] < so_tien:
            raise Exception("Số dư TK nguồn không đủ")

        cur.execute("""
            SELECT SoTaiKhoan FROM dbo.TaiKhoan
            WHERE SoTaiKhoan = ? AND TrangThai = N'Hoạt động'
        """, (so_tk_dich,))
        if not cur.fetchone():
            raise Exception("TK đích không tồn tại hoặc không hoạt động")

        cur.execute("""
            UPDATE dbo.TaiKhoan
            SET SoDu = SoDu - ?
            WHERE SoTaiKhoan = ?
        """, (so_tien, so_tk_nguon))

        if cur.rowcount == 0:
            raise Exception("Không trừ được tiền TK nguồn")

        cur.execute("""
            UPDATE dbo.TaiKhoan
            SET SoDu = SoDu + ?
            WHERE SoTaiKhoan = ?
        """, (so_tien, so_tk_dich))

        if cur.rowcount == 0:
            raise Exception("Không cộng được tiền TK đích")

        ma_gd_nguon = str(uuid.uuid4())
        ma_gd_dich = str(uuid.uuid4())

        cur.execute("""
            INSERT INTO dbo.GiaoDich
            VALUES (?, GETDATE(), ?, N'Chuyển khoản',
                    N'Chuyển khoản nội bộ', N'Hoàn thành', ?, ?)
        """, (ma_gd_nguon, so_tien, so_tk_nguon, ma_nv))

        cur.execute("""
            INSERT INTO dbo.GiaoDich
            VALUES (?, GETDATE(), ?, N'Nhận chuyển khoản',
                    N'Nhận từ chuyển khoản nội bộ', N'Hoàn thành', ?, ?)
        """, (ma_gd_dich, so_tien, so_tk_dich, ma_nv))

        conn.commit()
        return True, "Chuyển khoản thành công"

    except Exception as e:
        conn.rollback()
        return False, str(e)

    finally:
        conn.close()


def get_history_by_account(so_tk):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT MaGiaoDich, NgayGio, LoaiGiaoDich, SoTien, NoiDung, TrangThai
        FROM dbo.GiaoDich
        WHERE SoTaiKhoan = ?
        ORDER BY NgayGio DESC
    """, (so_tk,))
    rows = cur.fetchall()
    conn.close()
    return rows
