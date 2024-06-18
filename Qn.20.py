numbers = input("Enter a list of numbers, separated by spaces: ")

# Convert the input string into a list of numbers and calculate the sum
total_sum = sum(map(float, numbers.split()))

print("The sum of the numbers is:" ,total_sum)



#2nd method

numbers = input("Enter a list of numbers, separated by spaces: ")

# Convert the input string into a list of numbers
number_list = [int(num) for num in numbers.split()]

total_sum = sum(number_list)
print(f"The sum of the numbers is: {total_sum}")
