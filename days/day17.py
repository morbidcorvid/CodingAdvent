''' Day 17: No Such Thing as Too Much
'''

def get_containers(filename = './inputs/day17.txt'):
	containers = []
	with open(filename, 'r') as f:
		for line in f:
			containers.append(int(line.strip()))
	return containers
	
def find_combos(containers, eggnog, combo=[]):
	left = eggnog - sum(combo)
	combos, min, min_combos = 0, 0, 0
	cc = containers.copy()
	
	for container in containers:
		if left - container == 0:
			cc.remove(container)
			combos += 1
			if len(combo)+1 < min or min == 0:
				min, min_combos = len(combo)+1, 1
			elif len(combo)+1 == min:
				min_combos += 1
		elif left - container > 0 and len(cc) > 1:
			x = combo.copy()
			x.append(container)
			cc.remove(container)
			c, m, mc = find_combos(cc.copy(), eggnog, x)
			combos += c
			if m > 0 and (m < min or min == 0):
				min, min_combos = m, mc
			elif m > 0 and m == min:
				min_combos += mc
	return (combos, min, min_combos)
			
def part_1(eggnog = 150):
	#eggnog = 25
	#containers = [20,15,10,5,5]
	print(find_combos(get_containers(),eggnog))