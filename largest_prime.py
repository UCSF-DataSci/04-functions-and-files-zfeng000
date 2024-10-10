#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

import argparse
from math import isqrt
from fibonnaci import generate_fibonnaci

def is_prime(n):
	if n < 2:
		return False
	for i in range(2, isqrt(n)+1):
		if n % i == 0:
			return False
	return True

def find_largest_prime_fibonacci(limit):
	fsequence = generate_fibonnaci(limit)
	prime_f = [num for num in fsequence if is_prime(num)]

	if prime_f:
		return max(prime_f)
	else:
		return None

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = "Find the largest prime Fibonnaci numbers less than a limit.")
	parser.add_argument('limit', type=int, help='Upper limit for the Fibonacci numbers')
	args = parser.parse_args()
	largest_prime_f = find_largest_prime_fibonacci(args.limit)
	if largest_prime_f is not None:
		print(f"The largest prime Fibonacci numbers less than {args.limit} is {largest_prime_f}")
	else:
		print(f"There is no prime Fibonacci number less than {args.limit}")
