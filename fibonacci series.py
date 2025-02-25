a= 1
b= 1
print(a, end=" ")
print(b, end=" ")
x=1
for x in range(5):
    next_number = a + b
    print(next_number, end=" ")
    a = b
    b = next_number
