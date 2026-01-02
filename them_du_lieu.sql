USE quan_ly_ngan_hang;
GO

/* ===================== 1. QuanLy ===================== */
INSERT INTO QuanLy (MaQuanLy, HoTen, SDT, Email, CoSoLamViec, MatKhau) VALUES
('QL01', N'Nguyễn Văn Quản', '0901000001', 'ql1@bank.com', N'Hà Nội', '123'),
('QL02', N'Trần Thị Quản', '0901000002', 'ql2@bank.com', N'TP.HCM', '123'),
('QL03', N'Lê Văn Quản', '0901000003', 'ql3@bank.com', N'Đà Nẵng', '123'),
('QL04', N'Phạm Thị Quản', '0901000004', 'ql4@bank.com', N'Cần Thơ', '123'),
('QL05', N'Hoàng Văn Quản', '0901000005', 'ql5@bank.com', N'Hải Phòng', '123');

/* ===================== 2. NhanVien ===================== */
INSERT INTO NhanVien
(MaNV, HoTen, NgaySinh, SDT, Email, ChucVu, Luong, TrangThai, MatKhau, MaQuanLy) VALUES
('NV01', N'Lê Văn An', '1995-01-01', '0910000001', 'nv1@bank.com', N'Giao dịch', 12000000, N'Đang làm', '123', 'QL01'),
('NV02', N'Phạm Thị Bình', '1994-02-02', '0910000002', 'nv2@bank.com', N'Tín dụng', 15000000, N'Đang làm', '123', 'QL02'),
('NV03', N'Nguyễn Văn Cường', '1993-03-03', '0910000003', 'nv3@bank.com', N'Giao dịch', 11000000, N'Đang làm', '123', 'QL03'),
('NV04', N'Trần Thị Dung', '1992-04-04', '0910000004', 'nv4@bank.com', N'Kế toán', 13000000, N'Đang làm', '123', 'QL04'),
('NV05', N'Hoàng Văn Em', '1991-05-05', '0910000005', 'nv5@bank.com', N'Tín dụng', 16000000, N'Đang làm', '123', 'QL05');

/* ===================== 3. KhachHang ===================== */
INSERT INTO KhachHang
(MaKH, HoTen, NgaySinh, DiaChi, SDT, Email) VALUES
('KH01', N'Nguyễn Minh Long', '2001-01-01', N'Hà Nội', '0980000001', 'kh1@gmail.com'),
('KH02', N'Trần Hoàng Nam', '2000-02-02', N'TP.HCM', '0980000002', 'kh2@gmail.com'),
('KH03', N'Lê Thu Trang', '1999-03-03', N'Đà Nẵng', '0980000003', 'kh3@gmail.com'),
('KH04', N'Phạm Quốc Huy', '1998-04-04', N'Cần Thơ', '0980000004', 'kh4@gmail.com'),
('KH05', N'Hoàng Gia Bảo', '1997-05-05', N'Hải Phòng', '0980000005', 'kh5@gmail.com');

/* ===================== 4. TaiKhoan ===================== */
INSERT INTO TaiKhoan
(SoTaiKhoan, SoDu, NgayMo, TrangThai, MatKhau, DiemTinDung, HanMucThauChi, MaKH) VALUES
('TK001', 50000000, GETDATE(), N'Hoạt động', '123', 700, 10000000, 'KH01'),
('TK002', 30000000, GETDATE(), N'Hoạt động', '123', 680, 8000000, 'KH02'),
('TK003', 20000000, GETDATE(), N'Hoạt động', '123', 650, 5000000, 'KH03'),
('TK004', 40000000, GETDATE(), N'Hoạt động', '123', 720, 12000000, 'KH04'),
('TK005', 10000000, GETDATE(), N'Hoạt động', '123', 600, 3000000, 'KH05');

/* ===================== 5. GiaoDich ===================== */
INSERT INTO GiaoDich
(MaGiaoDich, NgayGio, SoTien, LoaiGiaoDich, NoiDung, TrangThai, SoTaiKhoan, MaNVGiaoDich) VALUES
('GD01', GETDATE(), 5000000, N'Nộp tiền', N'Nộp tiền mặt', N'Hoàn thành', 'TK001', 'NV01'),
('GD02', GETDATE(), 2000000, N'Rút tiền', N'Rút tại quầy', N'Hoàn thành', 'TK002', 'NV01'),
('GD03', GETDATE(), 3000000, N'Chuyển khoản', N'Chuyển nội bộ', N'Hoàn thành', 'TK003', 'NV03'),
('GD04', GETDATE(), 4000000, N'Nộp tiền', N'Nộp tiền ATM', N'Hoàn thành', 'TK004', 'NV02'),
('GD05', GETDATE(), 1000000, N'Rút tiền', N'Rút ATM', N'Hoàn thành', 'TK005', 'NV04');

/* ===================== 6. HoSoTinDung ===================== */
INSERT INTO HoSoTinDung
(MaHoSo, SoTienVay, LaiSuat, ThoiHan, TrangThai, MaTaiKhoan, MaNVTinDung) VALUES
('HS01', 100000000, 8.5, 24, N'Đang vay', 'TK001', 'NV02'),
('HS02', 80000000, 9.0, 36, N'Đã duyệt', 'TK002', 'NV05'),
('HS03', 60000000, 9.2, 12, N'Đang vay', 'TK003', 'NV05'),
('HS04', 120000000, 8.0, 48, N'Đã duyệt', 'TK004', 'NV02'),
('HS05', 50000000, 10.0, 12, N'Từ chối', 'TK005', 'NV05');

/* ===================== 7. Admin ===================== */
INSERT INTO Admin
(MaQuanTri, HoTen, SDT, Email, TrangThai, MatKhau) VALUES
('AD01', N'Admin Tổng', '0990000001', 'admin1@bank.com', N'Hoạt động', 'admin'),
('AD02', N'Admin Hệ thống', '0990000002', 'admin2@bank.com', N'Hoạt động', 'admin'),
('AD03', N'Admin Mạng', '0990000003', 'admin3@bank.com', N'Hoạt động', 'admin'),
('AD04', N'Admin Bảo mật', '0990000004', 'admin4@bank.com', N'Hoạt động', 'admin'),
('AD05', N'Admin Vận hành', '0990000005', 'admin5@bank.com', N'Hoạt động', 'admin');

/* ===================== 8. HeThongNgoai ===================== */
INSERT INTO HeThongNgoai
(MaHeThong, TenHeThong, APIEndpoint, MaQuanTri, TrangThai) VALUES
('HT01', N'NAPAS', 'https://api.napas.vn', 'AD01', N'Hoạt động'),
('HT02', N'CIC', 'https://api.cic.vn', 'AD02', N'Hoạt động'),
('HT03', N'VNPAY', 'https://api.vnpay.vn', 'AD03', N'Hoạt động'),
('HT04', N'MOMO', 'https://api.momo.vn', 'AD04', N'Hoạt động'),
('HT05', N'ZALOPAY', 'https://api.zalopay.vn', 'AD05', N'Hoạt động');

/* ===================== 9. KeToan ===================== */
INSERT INTO KeToan
(MaHachToan, NgayThang, SoTien, TaiKhoanChuyen, TaiKhoanNhan, LoaiSuKien, TrangThai, MaSuKien) VALUES
('KT01', GETDATE(), 5000000, 'TK001', NULL, N'Nộp tiền', N'Đã hạch toán', 'GD01'),
('KT02', GETDATE(), 2000000, NULL, 'TK002', N'Rút tiền', N'Đã hạch toán', 'GD02'),
('KT03', GETDATE(), 3000000, 'TK003', 'TK001', N'Chuyển khoản', N'Đã hạch toán', 'GD03'),
('KT04', GETDATE(), 4000000, 'TK004', NULL, N'Nộp tiền', N'Đã hạch toán', 'GD04'),
('KT05', GETDATE(), 1000000, NULL, 'TK005', N'Rút tiền', N'Đã hạch toán', 'GD05');

/* ===================== 10. TaiKhoanTietKiem ===================== */
INSERT INTO TaiKhoanTietKiem
(MaTietKiem, MaTaiKhoan, NgayMo, ThoiHan, LaiSuat, SoTienGui, TrangThai) VALUES
('TKK01', 'TK001', '2024-01-01', 12, 6.5, 30000000, N'Đang gửi'),
('TKK02', 'TK002', '2024-02-01', 6, 5.8, 20000000, N'Đang gửi'),
('TKK03', 'TK003', '2024-03-01', 12, 6.7, 15000000, N'Đang gửi'),
('TKK04', 'TK004', '2024-04-01', 24, 7.0, 40000000, N'Đang gửi'),
('TKK05', 'TK005', '2024-05-01', 6, 5.5, 8000000, N'Đang gửi');
