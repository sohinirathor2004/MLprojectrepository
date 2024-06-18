user_input = input("Enter a string: ")

filename = "output.txt"

# Open the file in write mode and write the user's input to the file
with open(filename, "w") as file:
    file.write(user_input)

print("The string has been written to ",filename)
