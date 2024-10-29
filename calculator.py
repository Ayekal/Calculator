# Checking if choice is one of the four options
if choice in ['1', '2', '3', '4']:
	try:
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
	except ValueError:
		print("Invalid input. Please enter numbers only.")
		return

	if choice == '1':
		print(f"The result is: {add(num1, num2)}")

	elif choice == '2':
		print(f"The result is: {subtract(num1, num2)}")

	elif choice == '3':
		print(f"The result is: {multiply(num1, num2)}")

	elif choice == '4':
		print(f"The result is: {divide(num1, num2)}")

else:
	print("Invalid Input")

# Run the calculator
calculator()