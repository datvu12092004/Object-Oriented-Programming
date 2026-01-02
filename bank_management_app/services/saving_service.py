import uuid
from database.db_connection import get_connection


def open_saving_account(so_tk, so_tien, thoi_han, lai_suat):
    conn = get_connection()
    cur = conn.cursor()

    try:
        # 1. Kiểm tra số dư
        cur.execute("""
            SELECT SoDu FROM TaiKhoan
            WHERE SoTaiKhoan = ? AND TrangThai = N'Hoạt động'
        """, (so_tk,))
        row = cur.fetchone()

        if not row:
            raise Exception("Tài khoản không tồn tại hoặc không hoạt động")

        if row[0] < so_tien:
            raise Exception("Số dư không đủ để gửi tiết kiệm")

        # 2. Trừ tiền tài khoản thanh toán
        cur.execute("""
            UPDATE TaiKhoan
            SET SoDu = SoDu - ?
            WHERE SoTaiKhoan = ?
        """, (so_tien, so_tk))

        # 3. Tạo tài khoản tiết kiệm
        ma_tk = str(uuid.uuid4())

        cur.execute("""
            INSERT INTO TaiKhoanTietKiem
            (MaTietKiem, MaTaiKhoan, NgayMo, ThoiHan, LaiSuat, SoTienGui, TrangThai)
            VALUES (?, ?, GETDATE(), ?, ?, ?, N'Đang gửi')
        """, (ma_tk, so_tk, thoi_han, lai_suat, so_tien))

        conn.commit()
        conn.close()
        return True, "Mở tài khoản tiết kiệm thành công"

    except Exception as e:
        conn.rollback()
        conn.close()
        return False, str(e)
