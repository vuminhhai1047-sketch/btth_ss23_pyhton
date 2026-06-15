
from datetime import datetime


def check_id(attendance_book, id_check):
    for index , values in enumerate(attendance_book):
        if values['id'] == id_check:
            return index
    return -1

def clock_in(attendance_book):
    while True:
        id_input = input('Nhập mã nhân viên:').strip().upper()
        index = check_id(attendance_book , id_input)
        if index != -1:
            print('Mã nhân viên đã tồn tại - Xin vui lòng nhập lại')
        else:
            break
    while True:
        name_input = input('Nhập tên nhân viên:')
        if not name_input:
            print('Tên nhân viên không được để trống - Xin vui lòng nhập lại')
        else:
            break
    while True:
        time_input = input('Nhập giờ vào (HH:MM): ')
        try:
            datetime.strptime(
                time_input,
                "%H:%M"
            )
            break
        except ValueError:
            print('Bạn nhập sai đingj dạng - Xin vui lòng nhập lại')
    attendance_book.append(
        {
        'id' : id_input,
        'name' : name_input,
        'times' : (time_input , None)
        }
    )
    print(f'Thành công: Đã ghi nhân {id_input} chấm công vào lúc {time_input}!')

