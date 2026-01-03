-- 1. Bảng Quản lý
CREATE TABLE QuanLy (
    MaQuanLy VARCHAR(20) PRIMARY KEY,
    HoTen NVARCHAR(100),
    SDT VARCHAR(15),
    Email VARCHAR(100),
    CoSoLamViec NVARCHAR(255),
    MatKhau VARCHAR(255)
);

-- 2. Bảng Nhân Viên
CREATE TABLE NhanVien (
    MaNV VARCHAR(20) PRIMARY KEY,
    HoTen NVARCHAR(100),
    NgaySinh DATE,
    SDT VARCHAR(15),
    Email VARCHAR(100),
    ChucVu NVARCHAR(50),
    Luong FLOAT,
    TrangThai NVARCHAR(50),
    MatKhau VARCHAR(255),
    MaQuanLy VARCHAR(20),
    FOREIGN KEY (MaQuanLy) REFERENCES QuanLy(MaQuanLy)
);

-- 3. Bảng Khách Hàng
CREATE TABLE KhachHang (
    MaKH VARCHAR(20) PRIMARY KEY,
    HoTen NVARCHAR(100),
    NgaySinh DATE,
    DiaChi NVARCHAR(255),
    SDT VARCHAR(15),
    Email VARCHAR(100)
);

-- 4. Bảng Tài Khoản
CREATE TABLE TaiKhoan (
    SoTaiKhoan VARCHAR(20) PRIMARY KEY,
    SoDu FLOAT DEFAULT 0,
    NgayMo DATETIME,
    TrangThai NVARCHAR(50),
    MatKhau VARCHAR(255),
    DiemTinDung INT,
    HanMucThauChi FLOAT,
    MaKH VARCHAR(20),
    FOREIGN KEY (MaKH) REFERENCES KhachHang(MaKH)
);

-- 5. Bảng Giao Dịch
CREATE TABLE GiaoDich (
    MaGiaoDich VARCHAR(20) PRIMARY KEY,
    NgayGio DATETIME,
    SoTien FLOAT,
    LoaiGiaoDich NVARCHAR(50),
    NoiDung NVARCHAR(255),
    TrangThai NVARCHAR(50),
    SoTaiKhoan VARCHAR(20),
    MaNVGiaoDich VARCHAR(20),
    FOREIGN KEY (SoTaiKhoan) REFERENCES TaiKhoan(SoTaiKhoan),
    FOREIGN KEY (MaNVGiaoDich) REFERENCES NhanVien(MaNV)
);

-- 6. Bảng Hồ Sơ Tín Dụng
CREATE TABLE HoSoTinDung (
    MaHoSo VARCHAR(20) PRIMARY KEY,
    SoTienVay FLOAT,
    LaiSuat FLOAT,
    ThoiHan INT, -- Số tháng
    TrangThai NVARCHAR(50),
    MaTaiKhoan VARCHAR(20),
    MaNVTinDung VARCHAR(20),
    FOREIGN KEY (MaTaiKhoan) REFERENCES TaiKhoan(SoTaiKhoan),
    FOREIGN KEY (MaNVTinDung) REFERENCES NhanVien(MaNV)
);

-- 7. Bảng Admin
CREATE TABLE Admin (
    MaQuanTri VARCHAR(20) PRIMARY KEY,
    HoTen NVARCHAR(100),
    SDT VARCHAR(15),
    Email VARCHAR(100),
    TrangThai NVARCHAR(50),
    MatKhau VARCHAR(255)
);

-- 8. Bảng Hệ Thống Ngoài
CREATE TABLE HeThongNgoai (
    MaHeThong VARCHAR(20) PRIMARY KEY,
    TenHeThong NVARCHAR(100), -- NAPAS/CIC
    APIEndpoint VARCHAR(255),
    MaQuanTri VARCHAR(20),
    TrangThai NVARCHAR(50),
    FOREIGN KEY (MaQuanTri) REFERENCES Admin(MaQuanTri)
);

-- 9. Bảng Kế Toán
CREATE TABLE KeToan (
    MaHachToan VARCHAR(20) PRIMARY KEY,
    NgayThang DATETIME,
    SoTien FLOAT,
    TaiKhoanChuyen VARCHAR(20),
    TaiKhoanNhan VARCHAR(20),
    LoaiSuKien NVARCHAR(100),
    TrangThai NVARCHAR(50),
    MaSuKien VARCHAR(20)
);

-- 10. Bảng Tài Khoản Tiết Kiệm
CREATE TABLE TaiKhoanTietKiem (
    MaTietKiem VARCHAR(20) PRIMARY KEY,
    MaTaiKhoan VARCHAR(20),
    NgayMo DATE,
    ThoiHan INT, -- Số tháng
    LaiSuat FLOAT,
    SoTienGui FLOAT,
    TrangThai NVARCHAR(50),
    FOREIGN KEY (MaTaiKhoan) REFERENCES TaiKhoan(SoTaiKhoan)
);
