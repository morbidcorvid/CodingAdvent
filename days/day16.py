''' Day 16: Aunt Sue
'''

MFCSAM_Output = {'children':3, 'cats':7, 'samoyeds':2, 'pomeranians':3, 'akitas':0, 'vizslas':0, 'goldfish':5, 'trees':3, 'cars':2, 'perfumes':1}

def get_aunts(filename = './inputs/day16.txt'):
	aunts = {}
	with open(filename, 'r') as f:
		for line in f:
			name, line_props = line.split(':', 1)
			props = {}
			for p in line_props.split(','):
				prop, val = p.split(':')
				props[prop.strip()] = int(val)
			aunts[name] = props
	return aunts

def find_aunt(aunts, tape, type, greater = [], less = []):
	aunts = get_aunts()
	for aunt in aunts:
		match = True
		for compound in tape:
			if compound in aunts[aunt]:
				if type == 'range' and compound in greater+less:
					if (compound in greater and aunts[aunt][compound] <= tape[compound]) or (compound in less and aunts[aunt][compound] >= tape[compound]):
						match = False
						break
				elif aunts[aunt][compound] != tape[compound]:
					match = False
					break
		if match:
			return aunt
	
def part_1():
	aunts = get_aunts()
	print(find_aunt(aunts, MFCSAM_Output, 'exact'))

def part_2(greater = ['cats','trees'], less = ['pomeranians','goldfish']):
	aunts = get_aunts()
	print(find_aunt(aunts, MFCSAM_Output, 'range', greater, less))