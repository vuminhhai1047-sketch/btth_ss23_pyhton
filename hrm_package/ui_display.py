


from datetime import datetime



def display_records(attendance_book):
    print('--- BẢNG CHẤM CÔNG ---')
    print(f"{'Mã' :<5} | {'Tên Nhân Viên' :<20} | {'Giờ vào' :<10} | {'Giờ ra'}")
    for index , values in enumerate(attendance_book):
        print(f"{values['id']:<5} | {values['name'] :<20} | {values['times'][0] :<10} | {'Đang làm việc' if values['times'][1] == None else values['times'][1]}")



