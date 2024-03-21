# Câu hỏi:

# Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện
# điều khiển, tạo ra một danh sách và một tuple chứa mọi số.

value=input('Nhập các giá trị: ')

list_value=value.split(',')

tuple_value=tuple(list_value)
print (tuple_value)
print(list_value)