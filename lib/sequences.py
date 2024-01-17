#!/usr/bin/env python3

def print_fibonacci(length):
    fib_numbers=[]
    for i in range(length):
        if i == 0:
            fib_numbers.append(0)
        elif i == 1:
            fib_numbers.append(1)
        else:
            next_number = fib_numbers[-1] + fib_numbers[-2]
            fib_numbers.append(next_number)
    print(fib_numbers)

print_fibonacci(10)