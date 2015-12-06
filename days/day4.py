# --- Day 4: The Ideal Stocking Stuffer ---
# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

import hashlib
from timeit import default_timer as timer

secret = "bgvyzdsv"

# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

def part_1():
	i = 1
	while True:
		key = secret+str(i)
		hex_hash = hashlib.md5(key.encode('utf-8')).hexdigest()
		if hex_hash[:5] == '00000':
			print('The number {} produces the hash {}'.format(i, hex_hash))
			break
		i += 1

# Now find one that starts with six zeroes.
# (did this lazily...)
def part_2():
	i = 1
	start = timer()
	while True:
		key = secret+str(i)
		hex_hash = hashlib.md5(key.encode('utf-8')).hexdigest()
		if hex_hash[:6] == '000000':
			print('The number {} produces the hash {}'.format(i, hex_hash))
			break
		i += 1
	end = timer()
	print(end - start)  