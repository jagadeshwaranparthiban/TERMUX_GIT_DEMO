n= int(input("Enter the number:"))

if n is None:
	print("Enter a valid input")
elif n%2 ==0:
	print(f"{n} is even")
else:
	print(f"{n} is odd")
