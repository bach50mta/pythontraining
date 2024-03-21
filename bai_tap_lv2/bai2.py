# Câu hỏi:

# Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. 
# Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.

# Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.

# Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: 
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


inputString = input('Nhập vào giá trị của x, y: ')
dimension = [int(x) for x in inputString.split(',')]
rowNum = dimension[0]
colNum = dimension[1]

multilist = [[0 for i in range(colNum)] for j in range(rowNum)]

for i in range(rowNum):
    for j in range(colNum):
        multilist[i][j]= i*j

print (multilist)