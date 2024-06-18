filename = "output.txt"

with open(filename, "r") as file:
    content = file.read()

print("The content of the file is:")
print(content)
