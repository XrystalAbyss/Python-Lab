a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))
c = float(input("Enter the 3rd number: "))

if a <= b and a <= c:
    print(f"The numbers in ascending order are: {a}, {min(b, c)}, {max(b, c)}")
elif b <= a and b <= c:
    print(f"The numbers in ascending order are: {b}, {min(a, c)}, {max(a, c)}")
else:
    print(f"The numbers in ascending order are: {c}, {min(a, b)}, {max(a, b)}")
