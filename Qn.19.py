import string

input_string = input("Enter a string: ")

# Create a translation table that maps each punctuation character to None
translator = str.maketrans('', '', string.punctuation)

# Remove punctuation from the string
clean_string = input_string.translate(translator)

print("String without punctuation:")
print(clean_string)
