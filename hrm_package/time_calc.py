from datetime import datetime

def time_calc(attendance_book):

    for values in attendance_book:

        time_in = values['times'][0]
        time_out = values['times'][1]

        # Chưa chấm công ra thì bỏ qua
        if time_out is None:
            print(f"{values['id']} - Chưa hoàn thành ca làm việc")
            continue

        # Chuyển chuỗi sang datetime
        time_in_dt = datetime.strptime(time_in, "%H:%M")
        time_out_dt = datetime.strptime(time_out, "%H:%M")

        # Luật đi muộn
        late_limit = datetime.strptime("10:00", "%H:%M")

        if time_in_dt > late_limit:

            print(
                f"{values['id']} - Vi phạm: Đến muộn quá 90 phút."
            )

        else:

            # Tính tổng thời gian làm việc
            total_hours = (
                time_out_dt - time_in_dt
            ).seconds / 3600

            if total_hours < 9:

                print(
                    f"{values['id']} - Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ."
                )

            else:

                print(
                    f"{values['id']} - Hợp lệ: Hoàn thành ca làm việc."
                )