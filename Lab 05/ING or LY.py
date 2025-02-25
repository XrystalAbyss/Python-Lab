input_string = input("Enter a string: ")

if len(input_string) >= 3:
    if input_string.endswith('ing'):
        result = input_string + 'ly'
    else:
        result = input_string + 'ing'
else:
    result = input_string

print("Result:", result)
