# --- Day 8: Matchsticks ---
# Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.
# However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.

import re
filename = './inputs/day8.txt'

#Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?
def part_1():
	code_chars = 0
	string_chars = 0
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip()
			code_chars += len(line)
			string_chars += len(eval(line))
	print(code_chars, string_chars, code_chars-string_chars)

#Now, let's go the other way. In addition to finding the number of characters of code, you should now encode each code representation as a new string and find the number of characters of the new encoded representation, including the surrounding double quotes.
def part_2():
	escaped = 0
	code_string = 0
	with open(filename, 'r') as f:
		count = 0
		for line in f:
			line = line.strip()
			escaped += len(re.escape(line)) + 2
			code_string += len(line)
	print(escaped, code_string, escaped-code_string)