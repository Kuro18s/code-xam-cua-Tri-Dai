import math
from fractions import Fraction

# Nhập liệu từ hsing
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

def Bam_may_ptrinh_bac_2(a, b, c):
	"""
	Giải phương trình bậc 2: ax^2 + bx + c = 0
	"""
	if a == 0:
		print("Phương Trình bậc 1 tự tính đi mày")
		if b != 0:
			x = -c / b
			print("Nghiệm của ptrinh bậc 1 đây em: x = ", x)
		else:
			print("Ko có nghiệm")
		return

	delta = b**2 - 4*a*c

	if delta > 0:
		x1 = (-b + math.sqrt(delta)) / (2*a)
		x2 = (-b - math.sqrt(delta)) / (2*a)
		print("PT có hai nghiệm phân biệt: x1 =", x1 , "và x2 =", x2 )	
	
		# Chuyển đổi thành phân số
		fraction1 = Fraction.from_float(x1).limit_denominator()
		fraction2 = Fraction.from_float(x2).limit_denominator()
    
		print("    ~~~Kết quả làm tròn~~~ ")
		print("x1 =", fraction1)
		print("x2 =", fraction2)
	elif delta == 0:
		x = -b / (2*a)
		print("Phương trình có nghiệm kép: x =", x)
	else:
		print("Phương trình vô nghiệm")

# Gọi hàm với các hệ số nhập vào
Bam_may_ptrinh_bac_2(a, b, c)
