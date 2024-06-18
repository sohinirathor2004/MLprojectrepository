number = int(input("Enter a number: "))

sum_of_digits = 0

for digit in str(number):
    sum_of_digits += int(digit)

print("The sum of the digits of the number",number," is ",sum_of_digits)
