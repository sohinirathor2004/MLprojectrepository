string = input("Enter a string: ")

char_frequency = {}

for char in string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("Character frequency in the given string:")
for char, frequency in char_frequency.items():
    print(char,":" ,frequency)
