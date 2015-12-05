#One stop shop for pulling up solutions

from days import day1

def run_part(d, p):
	day = globals()['day%d' % d]
	part = getattr(day, 'part_%d' % p)
	part()

def get_inputs():
	day = input('Day: ')
	part = input('Part: ')
	try:
		return (int(day), int(part))
	except (TypeError, ValueError):
		return (False, False)

def main():
	print('\n{0}Advent of Code{0}\nEnter the day and part you wish to see the solution for.\n(Non-numeric input to quit)\n'.format('*'*10))
	
	day, part = get_inputs()
	while day:
		print('\nDay {}, Part {} \n{}\n'.format(day, part, '-'*40))
		run_part(day,part)
		print('\n{}\n'.format('-'*40))
		day, part = get_inputs()
		
main()