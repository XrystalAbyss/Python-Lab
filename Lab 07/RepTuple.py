my_tuple = (1, 2, 3, 4, 5, 2, 6, 3, 7, 8, 2)

repeated_items = []
for item in my_tuple:
    if my_tuple.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)

print("Repeated items:", repeated_items)
