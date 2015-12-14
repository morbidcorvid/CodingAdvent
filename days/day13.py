# --- Day 13: Knights of the Dinner Table ---

filename = './inputs/day13.txt'

def find_best_path(seek, map, path = [], current = None):
	if len(path) == len(map):
		dist = 0
		for c in range(0,len(path)):
			d = (c+1) % len(path)
			dist += map[path[c]][path[d]] + map[path[d]][path[c]]
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
			la = line.split()
			p1, pm, u, p2 = la[0], la[2], la[3], la[10][:len(la[10])-1]
			for p in (p1,p2):
				if p not in map:
					map[p] = {}
			if pm == 'gain':
				map[p1][p2] = int(u)
			else:
				map[p1][p2] = -int(u)
	return map

def add_me(map):
	me = 'Colin'
	map[me] = {}
	for person in map.keys():
		map[person][me], map[me][person] = 0, 0
	return map
	
def part_1():
	print(find_best_path('max', get_map()))

def part_2():
	print(find_best_path('max', add_me(get_map())))