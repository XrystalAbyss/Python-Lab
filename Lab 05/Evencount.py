count = 1
even_numbers = 0
while count <= 10:
    if count % 2 == 0:
        print(count)
        even_numbers += 1
    if even_numbers == 5:
        break
    count += 1
