n = int(input("Enter the number of Fibonacci numbers to generate: "))

fibonacci_sequence = []

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    fibonacci_sequence = [0]
else:
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
print("The first" ,n,"numbers in the Fibonacci sequence are: ",fibonacci_sequence)
