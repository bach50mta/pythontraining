# Câu hỏi:

# Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó. 
# Giả sử đầu vào sau được cấp cho chương trình: hello world! 123

# Thì đầu ra sẽ là:

# Số chữ cái là: 10
# Số chữ số là: 3

s = input("nhập một chuỗi: ")
d = {'digits':0, 'letters':0}

for i in s:
    if i.isdigit():
        d['digits'] += 1
    elif i.isalpha():
        d['letters'] += 1

print(f"Số chữ cái là: {d['letters']}")

print(f"Số chữ số là: {d['digits']}")