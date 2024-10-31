def tong_chu_so (n):
	tong = 0
	while n != 0:
		tong += n % 10
		n //= 10
	return tong

print("_____________________________")
n = int(input("Nhập số để tính tổng 2 chữ số:"))

print("_____________________________")
print(f"Tổng các chữ sô trong sô {n} là: {tong_chu_so(n)}")
