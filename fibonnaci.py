#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

import argparse

def generate_fibonnaci(limit):
	fsequence = [0,1]
	while True:
		next_fnumber = fsequence[-1] + fsequence[-2]
		if next_fnumber >= limit:
			break
		fsequence.append(next_fnumber)
	return fsequence

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = "Generate the Fibonnaci numbers less than a limit.")
	parser.add_argument('limit', type=int, help='Upper limit for the Fibonacci numbers')
	args = parser.parse_args()
	fsequence = generate_fibonnaci(args.limit)
	print("The Fibonnaci numbers less than", args.limit, "are:", fsequence)