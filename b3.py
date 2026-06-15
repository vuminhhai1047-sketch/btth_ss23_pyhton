# 4 tính chất OOP



from package.logistics import display as dp
from package.manager import add_new_flight as anf
from package.time_helper import calculator as ca
from package.file_helper import create_log_folder as clf

flights = [
    {"flight_id": "RA001", "passengers": 148, "depart_time": "2026-06-15 08:00:00", "duration_min": 120}, # Hà Nội - TP.HCM
    {"flight_id": "RA002", "passengers": 85,  "depart_time": "2026-06-15 13:30:00", "duration_min": 45}   # Hà Nội - Vinh
]


while True:
    print('''
        ===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====
        1. Hiển thị lịch trình và Thống kê hậu cần
        2. Tiếp nhận chuyến bay mới
        3. Tính thời gian hạ cánh dự kiến (ETA)
        4. Khởi tạo thư mục lưu trữ log hệ thống5
        5. Thoát chương trình
        ===================================================
    ''')
    while True:
        try:
            choice = int(input('Nhập lựa chọn của bạn:'))
            if choice < 1 or choice > 5:
                print('Lỗi - Xin vui lòng nhập lại')
            else:
                break
        except ValueError:
            print('Bạn phải nhập số')
    match choice:
        case 1:
            dp(flights)
        case 2:
            anf(flights)
        case 3:
            ca(flights)
        case 4:
            clf(flights)
        case 5:
            print('Thoát chương trình')
            break 
        case _:
            print('Lỗi - Xin vui lòng nhập lại')

