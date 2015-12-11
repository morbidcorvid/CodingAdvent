# Day 11: Corporate Policy ---
# Santa's previous password expired, and he needs help choosing a new one.
# To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.
# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.
# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:
# 	Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
# 	Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
# 	Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

def check(password):
	has_straight = False
	num_doubles = 0
	prev = ''
	smaller = False
	skip = False
	l = len(password)
	for i in range(1,l+1):
		c = password[l-i]
		if c in 'iol':
			return False
		if i > 1:
			if not skip and c == prev:
				num_doubles += 1
				skip = True
			else:
				skip = False
			if ord(prev) - ord(c) == 1:
				if smaller:
					has_straight = True
				else:
					smaller = True
			else:
				smaller = False
		prev = c
	return has_straight and num_doubles > 1
				
def increment(password):
	password = list(password)
	l = len(password)
	for i in range(1,l+1):
		c = password[l-i]
		c = chr((ord(c)+1) % 123 % 97 + 97)
		if c in 'iol':
			c = chr((ord(c)+1) % 123 % 97 + 97)
			password = password[0:l-i] + list('a'*i)
		password[l-i] = c
		if c != 'a':
			break
	return ''.join(password)

def find_next(password):
	next = increment(password)
	while not check(next):
		next = increment(next)
		print('\rCurrent: '+next, end="", flush=True)
	print('\rFound:   '+next, end="\n", flush=True)
	return next

def part_1():
	print("\nSanta's new password is: ", find_next("cqjxjnds"))
	
def part_2():
	print("\nSanta's new password is: ", find_next(find_next("cqjxjnds")))
