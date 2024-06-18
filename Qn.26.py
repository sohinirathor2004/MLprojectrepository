string_input=input("Enter the string : ")
prefix=input("Enter the prefix : ")
suffix=input("Enter the suffix : ")
if (string_input[:len(prefix)]==prefix):
    print(f"The string starts with the prefix {prefix}")
else:
    print(f"The string starts not  with the prefix {prefix}")


if (string_input[:len(suffix)]==suffix):
    print(f"The string starts with the prefix {suffix}")
else:
    print(f"The string starts not  with the prefix {suffix}")