tuple1 = (10, 20, 30, 40, 50)
item_to_remove = 30
temp_list = list(tuple1)
temp_list.remove(item_to_remove)
tuple1 = tuple(temp_list)
print(tuple1)
