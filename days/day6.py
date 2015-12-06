# --- Day 6: Probably a Fire Hazard ---
# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

input_dir = './inputs/'
file = 'day6.txt'

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.
# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.
# After following the instructions, how many lights are lit?

def part_1():
	grid = [[0 for x in range(1000)] for x in range(1000)]
	#print_grid(grid)
	with open(input_dir+file, 'r') as f:
		for line in f:
			instr, tl, br = get_instructions(line)
			for x in range(tl[0], br[0]+1):
				for y in range(tl[1], br[1]+1):
					if instr == 'on' or (instr == 'toggle' and grid[x][y] == 0):
						grid[x][y] = 1
					elif instr == 'off' or (instr == 'toggle' and grid[x][y] == 1):
						grid[x][y] = 0
			#print_grid(grid)
	total_on = sum(sum(grid,[]))
	print("Santa's instructions turn on {} lights.".format(total_on))

# --- Part Two ---
# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.
# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.
	# The phrase turn on actually means that you should increase the brightness of those lights by 1.
	# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
	# The phrase toggle actually means that you should increase the brightness of those lights by 2.
# What is the total brightness of all lights combined after following Santa's instructions?

def part_2():
	grid = [[0 for x in range(1000)] for x in range(1000)]
	#print_grid(grid)
	with open(input_dir+file, 'r') as f:
		for line in f:
			instr, tl, br = get_instructions(line)
			for x in range(tl[0], br[0]+1):
				for y in range(tl[1], br[1]+1):
					if instr == 'on':
						grid[x][y] += 1
					elif instr == 'off' and grid[x][y] > 0:
						grid[x][y] -= 1
					elif instr == 'toggle':
						grid[x][y] += 2
			#print_grid(grid)
	total_bright = sum(sum(grid,[]))
	print("The total brightness of Santa's instructions is {}.".format(total_bright))
	

def get_instructions(line):
	i = line.split()
	if len(i) == 5:
		if i[1] == 'on':
			instr = 'on'
		else:
			instr = 'off'
		c = 2
	else:
		instr = 'toggle'
		c = 1
		
	tl = i[c].split(',')
	tl = (int(tl[0]), int(tl[1]))
	
	br = i[c+2].split(',')
	br = (int(br[0]), int(br[1]))
	
	return (instr, tl, br)

#for testing
def print_grid(grid):
	for row in grid:
		print(row)
	print('\n')
