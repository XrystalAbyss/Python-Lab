string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) < 2 or len(string2) < 2:
    print("Strings must be at least 2 characters long to swap the first two.")
else:
    swapped_string1 = string2[:2] + string1[2:]
    swapped_string2 = string1[:2] + string2[2:]

    result_string = swapped_string1 + " " + swapped_string2
    print(result_string)
