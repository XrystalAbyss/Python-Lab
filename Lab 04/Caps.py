input_string = input("Enter a string: ")
words = input_string.split()
result = []

for word in words:
    if len(word) > 1:
        word = word[0].upper() + word[1:-1] + word[-1].upper()
    else:
        word = word.upper()
    result.append(word)

print("Modified string:", ' '.join(result))
