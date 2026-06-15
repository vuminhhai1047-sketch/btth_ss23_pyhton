



from datetime import datetime 
from hrm_package.attendance_logic import check_id as ci

def clock_out(attendance_book):
    while True:
        id_output = input('Nhập mã NV:').strip().upper()
        index = ci(attendance_book , id_output)
        if index == -1:
            print('Mã nhân viên không tồn tại - Xin vui lòng nhập lại')
        else:
            break
    while True:
        try:
            time_output = input('Nhập giờ ra (HH:MM):')
            time_input = datetime.strptime(attendance_book[index]['times'][0] , "%H:%M")
            time_out = datetime.strptime(
                time_output,
                "%H:%M"
            )
            if time_out < time_input:
                print('Giờ ra không thể bé hơn giờ vào')
        except ValueError:
            print('Bạn nhập sai định dạng - Xin vui lòng nhập lại')
    attendance_book[index]['times'] = (attendance_book[index]['times'][0] , time_output)
    print('Thành công')
