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

def write_fibonnaci_to_file(fsequence, filename):
	try:
		with open(filename, 'w') as f:
			for number in fsequence:
				f.write(f"{number}\n")
		print(f"Fibonacci sequence successfully written to {filename}")
	except IOError as e:
		print(f"Error writing to file: {e}")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = "Generate the Fibonnaci numbers less than a limit.")
	parser.add_argument('limit', type=int, help='Upper limit for the Fibonacci numbers')
	parser.add_argument('filename', type=str, help='Output file name')
	args = parser.parse_args()
	fsequence = generate_fibonnaci(args.limit)
	print("The Fibonnaci numbers less than", args.limit, "are:", fsequence)
	write_fibonnaci_to_file(fsequence, args.filename)