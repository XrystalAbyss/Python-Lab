input_string = input("Enter a string: ")
words = input_string.split()

smallest_word = min(words, key=len)
print("Smallest word:", smallest_word)
