print("Input your age here, and we'll see where you belong.")
print("It will classify if you are a child, teen, adult or senior")
while True:
		try:
			age= float(input("input your age here:"))
			if age <=0:
				print("Invalid. Please put a non-negative number.")
			elif age >=65:
				print("You're a senior")
			elif age <=12:
				print("You're a child")
			elif age <=19:
				print("You're a teen")
			elif age >=20:
				print("You're a adult")
			else:
				print("Put your age in numbers. Thank you.")
		except:
			print("Put your age in numbers. Thank you.")