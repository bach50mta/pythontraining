# Câu hỏi:

# Viết một method tính giá trị bình phương của một số.


def square(number):
    return number**2

try:
    x = float(input('Nhập giá trị cần tính bình phương: '))
    print('Bình phương của',x, 'là',square(x))
except:
    print('Giá trị nhập vào không đúng')


