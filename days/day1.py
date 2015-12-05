# Day 1: Not Quite Lisp
# Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.
# An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
# The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

from modules.input import Input

i = Input('day1.txt')

def part_1():
	floor = 0

	while i.position < i.len-1:
		c = i.next_char()
		if c == '(':
			floor += 1
		elif c == ')':
			floor -= 1

	print(floor)

#What is the position of the character that causes Santa to first enter the basement?
def part_2():
	floor = 0

	while i.position < i.len-1:
		c = i.next_char()
		if c == '(':
			floor += 1
		elif c == ')':
			floor -= 1
		if floor < 0:
			#Question stipulates that first char in intructions has position 1 vs list position 0, increment position to match
			print('position: '+str(i.position+1)+'    floor:'+str(floor)+'    char:' + c)
			break
	if floor > 0:
		print('Santa never reaches the basement!')