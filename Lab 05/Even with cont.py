count = 1
even_numbers = 0
while count <= 10:
    count += 1
    if count % 2 != 0:
        continue
    print(count)
    even_numbers += 1
    if even_numbers == 4:
        break
