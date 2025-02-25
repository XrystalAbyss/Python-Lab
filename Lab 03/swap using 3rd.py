a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print("The two numbers before swap are a: %d b: %d" % (a, b))

c = a
a = b
b = c

print("The two numbers after swap are a: %d b: %d" % (a, b))
