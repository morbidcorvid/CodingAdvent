# --- Day 5: Doesn't He Have Intern-Elves For This? ---

# Santa needs help figuring out which strings in his text file are naughty or nice.

import re

input_dir = './inputs/'
file = 'day5.txt'

# --- Part One ---
# A nice string is one with all of the following properties:
# 	It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# 	It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# 	It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# How many strings are nice?
def part_1():
	vowels = re.compile(r'[aeiou]\w*[aeiou]\w*[aeiou]')
	double = re.compile(r'(.)\1')
	bad = re.compile(r'(ab)|(cd)|(pq)|(xy)')

	nice = 0
	with open(input_dir+file, 'r') as f:
		for line in f:
			if vowels.search(line) and double.search(line) and not bad.search(line):
				nice += 1
			
	print('Santa needs presents for the {} nice strings.'.format(nice))

# --- Part Two ---
# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.
# Now, a nice string is one with all of the following properties:
# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
# How many strings are nice under these new rules?
def part_2():
	double_pair = re.compile(r'(..).*\1')
	repeat = re.compile(r'(.).\1')
	
	nice = 0
	with open(input_dir+file, 'r') as f:
		for line in f:
			if double_pair.search(line) and repeat.search(line):
				nice += 1
			
	print('Santa needs presents for the {} nice strings.'.format(nice))
	
	#line = "aaa"
	#print ('vowels: {}\ndouble: {}\nbad: {}'.format(vowels.search(line), double.search(line), bad.search(line)))