# --- Day 12: JSAbacusFramework.io ---
# Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

import re
import json

filename = './inputs/day12.txt'

# They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

def part_1():
	with open(filename, 'r') as f:
		found = re.findall(r'-?\d+', f.read())
	print(sum(int(i) for i in found))


def sum_non_reds(s):
	if isinstance(s, int):
		return s
	elif isinstance(s, list):
		return sum(sum_non_reds(i) for i in s)
	elif isinstance(s, dict):
		if "red" in s.values():
			return 0
		else:
			return sum(sum_non_reds(i) for i in s.values())
	return 0	
	
def part_2():
	with open(filename) as f:
		print(sum_non_reds(json.load(f)))