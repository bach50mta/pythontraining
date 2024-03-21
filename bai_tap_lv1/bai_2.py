"""
Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in 
thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì
kết quả đầu ra phải là 40320.
"""

def giaithua(number):
    while (number<0):
        print("Phải nhập vào số nguyên dương")
        number = input("Nhập lại đi: ")
    if number==0:
        return 1
    return number*giaithua(number-1)

number = int(input("Nhập vào giá trị cần tính giai thừa: "))
print (giaithua(number))