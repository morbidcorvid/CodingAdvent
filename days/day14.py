#--- Day 14: Reindeer Olympics ---
from math import floor

filename = './inputs/day14.txt'

def traveled(time, speed, fly, rest):
	cycles = floor(time / (fly + rest))
	curr = time % (fly + rest)
	dist = speed * (cycles * fly + min(curr, fly))
	return dist

def get_reindeer():
	reindeer = {}
	with open(filename, 'r') as f:
		for line in f:
			la = line.split()
			reindeer[la[0]] = {'stats':(int(la[3]), int(la[6]), int(la[13])), 'score':0}
	return reindeer
	
def part_1():
	race = 2503
	reindeer = get_reindeer()
	winner = ''
	best = 0
	for deer in reindeer:
		s, f, r = reindeer[deer]['stats']
		dist = traveled(race, s, f, r)
		if dist > best:
			winner, best = deer, dist
		print(deer, dist)
	print('\nWinner:', winner, 'Travelled:', best, 'miles.')

def part_2():
	race = 2503
	reindeer = get_reindeer()
	leader = ''
	best = 0
	for t in range(1,race+1):
		for deer in reindeer:
			s, f, r = reindeer[deer]['stats']
			dist = traveled(t, s, f, r)
			if dist > best:
				leader, best = deer, dist
		reindeer[leader]['score'] += 1
	for deer in reindeer:
		print(deer, reindeer[deer]['score'])
	winner = max(reindeer, key = lambda x: reindeer[x]['score'])
	print('\nWinner:', winner, 'Points:', reindeer[winner]['score'])

