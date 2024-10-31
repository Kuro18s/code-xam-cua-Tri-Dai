from random import randint

print("~~~Tro Choi Keo Bua Bao~~~") 
print("Make a decision:")

player = input()
computer = randint(1,3)

print("________________________")
print("You choose: ", player)

if computer == 1:
	computer = "Keo"
if computer == 2:
	computer = "Bua"
if computer == 3:
	computer = "Bao"

print("Computer chooses: ", computer)
print("________________________")

#conclusion_message
a = "~~~Congrats, You win~~~"
b = "~~~Draw~~~"
c = "~~~You lose~~~"
d = "~~~Invalid choice. Please choose between 'Keo', 'Bua', or 'Bao'~~~"

#extra message
x = "Good job budd"
y = "Nice Try"
z = "Not badd"

if player == "Keo":
	if computer == "Keo":
		print(b)
		print(z)
	elif computer == "Bua":
		print(c)
		print(y)
	elif computer == "Bao":
		print(a)
		print(x)

elif player == "Bua":
	if computer == "Bua":
		print(b)
		print(z)
	elif computer == "Keo":
		print(a)
		print(x)
	elif computer == "Bao":
		print(c)
		print(y)

elif player == "Bao":
	if computer == "Bao":
		print(b)
		print(z)
	elif computer == "Keo":
		print(c)
		print(y)
	elif computer == "Bua":
		print(a)
		print(z)

else:
	print(d)
