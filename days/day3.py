# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
# Santa is delivering presents to an infinite two-dimensional grid of houses.

from modules.input import Input

i = Input('day3.txt')
directions = {'<':(-1,0), '^':(0,1), '>':(1,0), 'v':(0,-1)}

def tup_add(t1, t2):
	a, b = t1
	x, y = t2
	return (a+x, b+y)

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.
# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

def part_1():
	santa = (0,0)
	visited = [santa]
	
	while i.position < i.len-1:
		direction = i.next_char()
		santa = tup_add(santa,directions[direction])
		if santa not in visited:
			visited.append(santa)
	
	print('Santa visited {} houses.'.format(len(visited)))
	
# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.
# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.
# This year, how many houses receive at least one present?

def part_2():
	santa = (0,0)
	robo = (0,0)
	visited = [santa]
	
	while i.position < i.len-1:
		direction = i.next_char()
		if i.position % 2 == 0:
			santa = tup_add(santa,directions[direction])
			if santa not in visited:
				visited.append(santa)
		else:
			robo = tup_add(robo,directions[direction])
			if robo not in visited:
				visited.append(robo)
		
	print('Santa and Robo-Santa visited {} houses.'.format(len(visited)))
	