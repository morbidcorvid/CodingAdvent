from time import sleep

def get_initial_state(filename):
	grid = []
	with open(filename, 'r') as f:
		for line in f:
			grid.append([1 if c is '#' else 0 for c in line.strip()])
	return grid

def step(grid):
	new_state = [[0 for x in range(len(grid))] for y in range(len(grid))]
	for x in range(len(grid)):
		for y in range(len(grid)):
			sn = sum([sum(grid[nx][max(y-1,0):min(y+2,len(grid))]) for nx in range(max(x-1,0), min(x+2,len(grid)))])
			new_state[x][y] = 1 if (grid[x][y] and (sn == 3 or sn == 4)) or (not grid[x][y] and sn == 3) else 0
	return new_state

def break_corners(grid):
	for x in (0,len(grid)-1):
		for y in (0,len(grid)-1):
			grid[x][y]=1
	return grid

default_file = './inputs/day18.txt'
def part_1(steps=100, filename = default_file):
	grid = get_initial_state(filename)
	for s in range(steps):
		grid = step(grid)
		#print_grid(grid)
		#sleep(0.4)
	print(sum(sum(grid,[])))
	
def part_2(steps=100, filename = default_file):
	grid = break_corners(get_initial_state(filename))
	for s in range(steps):
		grid = break_corners(step(grid))
	print(sum(sum(grid,[])))

def print_grid(grid):
	str_grid = "\f"
	for string in grid:
		for light in string:
			str_grid+= '.' if light else ' '
		str_grid+="\n"
	print(str_grid,flush=True)