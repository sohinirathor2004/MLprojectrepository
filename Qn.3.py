number = int(input("Enter a number: "))
result = 1
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(2, number + 1):
        result *= i
    print("The factorial of ",number," is ",result)
