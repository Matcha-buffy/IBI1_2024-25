# 1. Loop from 1 to 10.
# 2. For each number n, calculate the triangular number using the formula: sum(1 to n).
# 3. Print each triangular number directly within the loop.
number = []  # define the triangular numbers
# calculate the first 10 triangular numbers
for n in range(1, 11):
    number = sum(range(1, n + 1))  # Calculate the nth triangular number, triangular number = 1+...+n
    # Print the result
    print(number, end=" ")
