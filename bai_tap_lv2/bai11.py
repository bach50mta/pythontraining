# Viết chương trình Python nhập một mảng hai chiều các số thực A (m hàng, n cột) từ bàn phím.
# a. Tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột
# b. Tìm phần tử lớn nhất và phần tử nhỏ nhất của mảng A cùng các chỉ số hàng và cột của 2 phần tử này.
# c. Trong mảng A có bao nhiêu phần tử bằng phần tử lớn nhất.

# Gợi ý:
# Sử dụng thư viện numpy để khởi tạo mảng A và thực hiện các phép toán trên mảng.
# Câu lệnh np.amax(A, axis=0) trả về giá trị lớn nhất trên mỗi cột của mảng A, còn np.amin(A, axis=0) trả về 
# giá trị nhỏ nhất trên mỗi cột.
# Để tìm phần tử lớn nhất và nhỏ nhất của mảng A cùng với chỉ số hàng và cột của 2 phần tử này, chúng ta sử dụng 
# np.amax(A) và np.amin(A) để tìm giá trị lớn nhất và nhỏ nhất của mảng A, sau đó sử dụng hàm np.unravel_index 
# để chuyển đổi chỉ số dạng 1 chiều thành chỉ số dạng 2 chiều.

import numpy as np
m, n = map(int, input('nhập kích thước của mảng 2 chiều: ').split())
A = np.zeros((m,n))

for i in range(m):
    row = list(map(float, input(f'nhập hàng {i+1}: ').split()))
    A[i][:]=row
max_col = np.amax(A, axis=0)
min_col = np.amin(A, axis=0)

print('giá trị lớn nhất của mỗi cột là: ', max_col)
print('giá trị nhỏ nhất của mỗi cột là: ', min_col)

# Tìm phần tử lớn nhất và nhỏ nhất trong A
max_val = np.amax(A)
min_val = np.amin(A)

# Tìm index ban đầu của 2 giá trị max min đó

max_index = np.unravel_index(np.argmax(A), A.shape)
min_index = np.unravel_index(np.argmin(A), A.shape)

print(f'phần tử lớn nhất trong A là: {max_val} tại A[{max_index}]')
print(f'phần tử nhỏ nhất trong A là: {min_val} tại A[{min_index}]')

#Tính số phần tử trong mảng có giá trị bằng max_val
count_maxval = np.count_nonzero(A == max_val)
print(f'Có {count_maxval} giá trị bằng với giá trị lớn nhất của mảng A')