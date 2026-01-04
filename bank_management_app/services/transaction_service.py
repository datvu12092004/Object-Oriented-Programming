import uuid
from database.db_connection import get_connection


# ======================================================
# NỘP TIỀN
# ======================================================
def deposit(so_tk, so_tien, ma_nv):
    conn = get_connection()
    cur = conn.cursor()
    try:
        # 1. Cộng tiền
        cur.execute("""
            UPDATE dbo.TaiKhoan
            SET SoDu = SoDu + ?
            WHERE SoTaiKhoan = ? AND TrangThai = N'Hoạt động'
        """, (so_tien, so_tk))

        if cur.rowcount == 0:
            return False, "Số tài khoản không tồn tại hoặc không hoạt động"

        # 2. Ghi giao dịch
        ma_gd = str(uuid.uuid4())
        cur.execute("""
            INSERT INTO dbo.GiaoDich
            (MaGiaoDich, NgayGio, SoTien, LoaiGiaoDich,
             NoiDung, TrangThai, SoTaiKhoan, MaNVGiaoDich)
            VALUES (?, GETDATE(), ?, N'Nộp tiền',
                    N'Nộp tại quầy', N'Hoàn thành', ?, ?)
        """, (ma_gd, so_tien, so_tk, ma_nv))

        conn.commit()

        return True, {
            "MaGiaoDich": ma_gd,
            "SoTaiKhoan": so_tk,
            "SoTien": so_tien,
            "LoaiGiaoDich": "Nộp tiền",
            "MaNV": ma_nv
        }

    except Exception as e:
        conn.rollback()
        return False, str(e)

    finally:
        conn.close()


# ======================================================
# RÚT TIỀN
# ======================================================
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
            return False, "Số tài khoản không tồn tại hoặc không hoạt động"

        if row[0] < so_tien:
            return False, "Số dư không đủ"

        cur.execute("""
            UPDATE dbo.TaiKhoan
            SET SoDu = SoDu - ?
            WHERE SoTaiKhoan = ?
        """, (so_tien, so_tk))

        if cur.rowcount == 0:
            return False, "Không cập nhật được số dư"

        ma_gd = str(uuid.uuid4())
        cur.execute("""
            INSERT INTO dbo.GiaoDich
            (MaGiaoDich, NgayGio, SoTien, LoaiGiaoDich,
             NoiDung, TrangThai, SoTaiKhoan, MaNVGiaoDich)
            VALUES (?, GETDATE(), ?, N'Rút tiền',
                    N'Rút tại quầy', N'Hoàn thành', ?, ?)
        """, (ma_gd, so_tien, so_tk, ma_nv))

        conn.commit()

        return True, {
            "MaGiaoDich": ma_gd,
            "SoTaiKhoan": so_tk,
            "SoTien": so_tien,
            "LoaiGiaoDich": "Rút tiền",
            "MaNV": ma_nv
        }

    except Exception as e:
        conn.rollback()
        return False, str(e)

    finally:
        conn.close()


# ======================================================
# CHUYỂN KHOẢN
# ======================================================
def transfer(so_tk_nguon, so_tk_dich, so_tien, ma_nv):
    conn = get_connection()
    cur = conn.cursor()
    try:
        # TK nguồn
        cur.execute("""
            SELECT SoDu FROM dbo.TaiKhoan
            WHERE SoTaiKhoan = ? AND TrangThai = N'Hoạt động'
        """, (so_tk_nguon,))
        src = cur.fetchone()
        if not src:
            return False, "Tài khoản nguồn không tồn tại hoặc không hoạt động"

        if src[0] < so_tien:
            return False, "Số dư tài khoản nguồn không đủ"

        # TK đích
        cur.execute("""
            SELECT 1 FROM dbo.TaiKhoan
            WHERE SoTaiKhoan = ? AND TrangThai = N'Hoạt động'
        """, (so_tk_dich,))
        if not cur.fetchone():
            return False, "Tài khoản đích không tồn tại hoặc không hoạt động"

        # Trừ tiền nguồn
        cur.execute("""
            UPDATE dbo.TaiKhoan
            SET SoDu = SoDu - ?
            WHERE SoTaiKhoan = ?
        """, (so_tien, so_tk_nguon))

        # Cộng tiền đích
        cur.execute("""
            UPDATE dbo.TaiKhoan
            SET SoDu = SoDu + ?
            WHERE SoTaiKhoan = ?
        """, (so_tien, so_tk_dich))

        ma_gd = str(uuid.uuid4())
        cur.execute("""
            INSERT INTO dbo.GiaoDich
            (MaGiaoDich, NgayGio, SoTien, LoaiGiaoDich,
             NoiDung, TrangThai, SoTaiKhoan, MaNVGiaoDich)
            VALUES (?, GETDATE(), ?, N'Chuyển khoản',
                    N'Chuyển khoản nội bộ', N'Hoàn thành', ?, ?)
        """, (ma_gd, so_tien, so_tk_nguon, ma_nv))

        conn.commit()

        return True, {
            "MaGiaoDich": ma_gd,
            "TuTK": so_tk_nguon,
            "DenTK": so_tk_dich,
            "SoTien": so_tien,
            "LoaiGiaoDich": "Chuyển khoản",
            "MaNV": ma_nv
        }

    except Exception as e:
        conn.rollback()
        return False, str(e)

    finally:
        conn.close()


# ======================================================
# LỊCH SỬ GIAO DỊCH
# ======================================================
def get_history_by_account(so_tk):
    conn = get_connection()
    cur = conn.cursor()
    try:
        # Kiểm tra tài khoản tồn tại
        cur.execute("""
            SELECT 1 FROM dbo.TaiKhoan
            WHERE SoTaiKhoan = ?
        """, (so_tk,))
        if cur.fetchone() is None:
            return False, "Số tài khoản không tồn tại"

        # Lấy lịch sử
        cur.execute("""
            SELECT MaGiaoDich, NgayGio, LoaiGiaoDich,
                   SoTien, NoiDung, TrangThai
            FROM dbo.GiaoDich
            WHERE SoTaiKhoan = ?
            ORDER BY NgayGio DESC
        """, (so_tk,))

        rows = cur.fetchall()
        return True, rows

    finally:
        conn.close()
