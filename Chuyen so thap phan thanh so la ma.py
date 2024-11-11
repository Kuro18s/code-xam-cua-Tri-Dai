#Bai code giup chuyen so thap phan thanh so La Ma
#Credit: KuroInu

def decimal_to_roman(num):
	#Danh sach so de chuyen o day
	roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), 
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), 
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I') ]
	
	roman = ""
	for value, symbol in roman_numerals:
		while num >= value:
			roman += symbol
			num -= value
	return roman

decimal_number = int(input("Nhap so can chuyen:"))
print(f"So la ma cua {decimal_number} la:", decimal_to_roman(decimal_number))