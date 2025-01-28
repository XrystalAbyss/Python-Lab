a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

if a == b:
    print(f"The comman number is {b}")
elif b == c:
    print(f"The comman number is {c}")
elif a == c:
    print(f"The comman number is {a}")
else:
    print("No two numbers are equal.")
