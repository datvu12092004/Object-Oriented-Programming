import uuid
from database.db_connection import get_connection


def open_saving(so_tk, so_tien, ky_han, lai_suat, ma_nv):
    conn = get_connection()
    cur = conn.cursor()
    try:
        # 1. Kiểm tra tài khoản nguồn
        cur.execute("""
            SELECT SoDu
            FROM dbo.TaiKhoan
            WHERE SoTaiKhoan = ? AND TrangThai = N'Hoạt động'
        """, (so_tk,))
        row = cur.fetchone()

        if not row:
            return False, "Tài khoản không tồn tại hoặc không hoạt động"

        if row[0] < so_tien:
            return False, "Số dư không đủ để gửi tiết kiệm"

        # 2. Trừ tiền tài khoản
        cur.execute("""
            UPDATE dbo.TaiKhoan
            SET SoDu = SoDu - ?
            WHERE SoTaiKhoan = ?
        """, (so_tien, so_tk))

        # 3. Tạo sổ tiết kiệm (ĐÚNG TÊN BẢNG + CỘT)
        ma_tk = str(uuid.uuid4())
        cur.execute("""
            INSERT INTO dbo.TaiKhoanTietKiem
            (MaTietKiem, MaTaiKhoan, NgayMo,
             ThoiHan, LaiSuat, SoTienGui, TrangThai)
            VALUES (?, ?, GETDATE(), ?, ?, ?, N'Đang gửi')
        """, (
            ma_tk,
            so_tk,
            ky_han,
            lai_suat,
            so_tien
        ))

        # 4. Ghi giao dịch
        ma_gd = str(uuid.uuid4())
        cur.execute("""
            INSERT INTO dbo.GiaoDich
            (MaGiaoDich, NgayGio, SoTien, LoaiGiaoDich,
             NoiDung, TrangThai, SoTaiKhoan, MaNVGiaoDich)
            VALUES (?, GETDATE(), ?, N'Gửi tiết kiệm',
                    N'Mở sổ tiết kiệm', N'Hoàn thành', ?, ?)
        """, (ma_gd, so_tien, so_tk, ma_nv))

        conn.commit()

        return True, {
            "MaTietKiem": ma_tk,
            "MaTaiKhoan": so_tk,
            "SoTienGui": so_tien,
            "ThoiHan": ky_han,
            "LaiSuat": lai_suat,
            "MaNV": ma_nv
        }

    except Exception as e:
        conn.rollback()
        return False, str(e)

    finally:
        conn.close()
