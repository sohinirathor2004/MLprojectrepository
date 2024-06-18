main_string = input("Enter the main string: ")

substring = input("Enter the substring to check: ")

if substring in main_string:
    print("The substring ",substring, "is present in the main string")
else:
    print("The substring ",substring," is not present in the main string")
