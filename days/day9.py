#--- Day 9: All in a Single Night ---
# Every year, Santa manages to deliver all of his presents in a single night.
# This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once.

filename = './inputs/day9.txt'

def find_best_path(seek, map, path = [], current = None):
	if len(path) == len(map):
		dist = 0
		for c in range(0,len(path)-1):
			dist += map[path[c]][path[c+1]]
		return (dist, path)
		
	best_dist, best_path = 0, []
	if current == None:
		current = map
	
	for city in current.keys():
		if city not in path:
			branch = path + [city]
			dist, branch = find_best_path(seek, map, branch, map[city])
			if (seek == 'min' and dist < best_dist) or (seek == 'max' and dist > best_dist) or best_dist == 0:
				best_dist, best_path = dist, branch
	
	return (best_dist, best_path)

def get_map():
	map = {}
	with open(filename, 'r') as f:
		for line in f:
			c1, t, c2, e, dist = line.split()
			for c in (c1,c2):
				if c not in map:
					map[c] = {}
			map[c1][c2], map[c2][c1] = int(dist), int(dist)
	return map

#What is the distance of the shortest route?
def part_1():
	print(find_best_path('min', get_map()))

#What is the distance of the longest route?
def part_2():
	print(find_best_path('max', get_map()))