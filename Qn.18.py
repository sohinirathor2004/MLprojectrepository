str1 = input("Enter the str1 : ")
str2 = input("Enter the str2 : ")
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()
if len(str1) != len(str2):
    print(f"'{str1}' and '{str2}' are not anagrams.")
else:
    if sorted(str1) == sorted(str2):
        print(f"'{str1}' and '{str2}' are anagrams.")
    else:
        print(f"'{str1}' and '{str2}' are not anagrams.")