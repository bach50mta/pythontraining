# Câu hỏi:
# Định nghĩa một class có ít nhất 2 method:
# getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
# printString: in chuỗi vừa nhập sang chữ hoa.
# Thêm vào các hàm kiểm tra đơn giản để kiểm tra method của class.

class toString(object): 
    def __init__(self):
        self.t = ''
    def getString(self):
        self.t = input('Nhập chuỗi: ')

    def printString(self):
        print(self.t.upper())

stri = toString()

stri.getString()

stri.printString()