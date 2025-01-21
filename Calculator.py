print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Remainder (mod)")

choice = input("Enter choice (1/2/3/4/5): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = num1 + num2
    print("The result of addition is:", result)
elif choice == '2':
    result = num1 - num2
    print("The result of subtraction is:", result)
elif choice == '3':
    result = num1 * num2
    print("The result of multiplication is:", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("The result of division is:", result)
    else:
        print("Error! Division by zero.")
elif choice == '5':
    if num2 != 0:
        result = num1 % num2
        print("The remainder (mod) is:", result)
    else:
        print("Error! Division by zero for remainder.")
else:
    print("Invalid input! Please select a valid operation.")
