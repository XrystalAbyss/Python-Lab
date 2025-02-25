a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print(f"The two numbers before swap are a: {a} b: {b}")

a = a + b
b = a - b
a = a - b

print(f"The two numbers after swap are a: {a} b: {b}")
