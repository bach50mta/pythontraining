# Câu hỏi:

# Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.

# Giả sử đầu vào là: Quản Trị Mạng


s = input('Nhập chuỗi: ')
d = {'upper':0, 'lower':0}

for i in s:
    if i.isupper():
        d['upper']+=1
    elif i.islower():
        d['lower']+=1
print(f"Số chữ Hoa: {d['upper']}")

print(f"Số chữ thường: {d['lower']}")