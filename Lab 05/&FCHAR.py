input_string = input("Enter a string: ")

if not input_string:
    print(input_string) 
else:
    first_char = input_string[0]
    modified_string = first_char + input_string[1:].replace(first_char, '$')
    print(modified_string)


print("\n--- Example Usages ---")

test_strings = ["restart", "google", "programming", "anaconda", "", "x"]

for test_str in test_strings:
    if not test_str:
        result = test_str
    else:
        first_char = test_str[0]
        result = first_char + test_str[1:].replace(first_char, '$')

    print(f"'{test_str}' becomes '{result}'")
