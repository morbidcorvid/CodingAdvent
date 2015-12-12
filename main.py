#One stop shop for pulling up solutions
import time, sys
from days import day1, day2, day3, day4, day5, day6, day7, day8, day9, day11, day12

def run_part(d, p):
	day = globals()['day%d' % d]
	part = getattr(day, 'part_%d' % p)
	print('\nDay {}, Part {} \n{}\n'.format(d, p, '-'*40))
	part()
	print('\n{}\n'.format('-'*40))
	
def get_inputs():
	try:
		day = int(input('Day: '))
		part = int(input('Part: '))
		return (day, part)
	except (TypeError, ValueError):
		return (False, False)

def test(day,part):
	start = time.time()
	run_part(day, part)
	end = time.time()
	print("Time to solve: {} seconds.".format(end - start))
		
def main():
	if len(sys.argv) > 1:
		test(int(sys.argv[1]), int(sys.argv[2]))
	else:
		print('\n{0}Advent of Code{0}\nEnter the day and part you wish to see the solution for.\n(Non-numeric input to quit)\n'.format('*'*10))
		day, part = get_inputs()
		while day:
			run_part(day,part)
			day, part = get_inputs()

if __name__ == "__main__":
	main()
