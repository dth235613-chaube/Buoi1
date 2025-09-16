variable = input( " Thong bao ")

name= input(" Nhap ten")
print(" xin chao",name)

age=int(input(" Nhap tuoi "))
print(" Tuoi",age)

try:
    num = int(input("Nhập một số nguyên: "))
    print("Số bạn nhập là:",num)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")

    a,b= map(int, input(" nhap hai so nguyen:").split())
    print("Tong :", a+b)

    numbers = list(map(int, input("Nhập các số, cách nhau bởi dấu cách: ").split()))
print("Danh sách:", numbers)

n = int(input("Nhập số lượng dòng: "))
data = []
for i in range(n):
    line = input(f"Nhập dòng {i+1}: ")
    data.append(line)
print("Dữ liệu đã nhập:", data)

import sys
for line in sys.stdin:
    print("Dòng nhập:", line.strip())