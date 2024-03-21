# Câu hỏi: Tính tuổi dựa trên ngày tháng năm sinh nhập vào.

# Ví dụ: Nhập vào ngày tháng năm sinh dạng y/m/d, hãy tính tuổi của người này.

# Gợi ý: Sử dụng module datetime. Sử dụng datetime, chúng ta có thể tìm tuổi bằng 
# cách trừ năm sinh cho năm hiện tại.

import datetime

birthday= input("Nhập vào ngày tháng năm sinh: ")
list_value = birthday.split('/')

year_birthday = int(list_value[2])
month_birthday = int(list_value[1])
day_birthday = int(list_value[0])

current_year = datetime.date.today().year

print(f'Bạn sinh ngày: {day_birthday}/{month_birthday}/{year_birthday}')
print(f'Và bạn {current_year-year_birthday} tuổi')