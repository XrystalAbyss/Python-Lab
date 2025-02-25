input_string = input("Enter a string: ")
vowels = 'aeiou'
vowel_count = {vowel: 0 for vowel in vowels}

for char in input_string.lower():
    if char in vowels:
        vowel_count[char] += 1

for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")
