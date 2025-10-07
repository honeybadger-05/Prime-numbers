# fibonacci_series.py

n = int(input("Enter how many terms you want: "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to 1 term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        next_num = a + b
        a = b
        b = next_num
        count += 1
