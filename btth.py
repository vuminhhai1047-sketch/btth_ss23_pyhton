


from hrm_package.ui_display import display_records as dr
from hrm_package.attendance_logic import clock_in as ci
from hrm_package.attendance_lockout import clock_out as co
from hrm_package.time_calc import time_calc as tc

attendance_book = [
    {"id": "NV01", "name": "Nguyễn Văn A", "times": ("08:30", "17:30")},
    {"id": "NV02", "name": "Trần Thị B", "times": ("09:30", None)}, # Đang làm việc, chưa chấm công ra
    {"id": "NV03", "name": "Lê Văn C", "times": ("10:15", "19:15")}
]


while True:
    print('''
        === HỆ THỐNG CHẤM CÔNG RIKKEI (FLEX-TIME) ===
        1. Xem bảng chấm công ngày
        2. Chấm công Vào (Clock-in)
        3. Chấm công Ra (Clock-out)
        4. Đánh giá vi phạm
        5. Thoát chương trình 
        ================================================= 
    ''')
    while True:
        try:
            choice = int(input('Nhập chức năng (1-5):'))
            if choice < 1 or choice > 5:
                print('LỖI - Xin vui lòng nhập lại')
            else:
                break
        except ValueError:
            print('Bạn phải nhập số')
    match choice:
        case 1:
            dr(attendance_book)
        case 2:
            ci(attendance_book)
        case 3:
            co(attendance_book)
        case 4:
            tc(attendance_book)
        case 5:
            print('Thoát chương trình')
            break
        case _:
            print('Bạn nhập sai yêu cầu - Xin vui lòng nhập lại')