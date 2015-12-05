# --- Day 2: I Was Told There Would Be No Math ---

input_dir = './inputs/'
file = 'day2.txt'

def dimensions(line):
	l, w, h = tuple(line.split('x'))
	l = int(l)
	w = int(w)
	h = int(h)
	return (l, w, h)

# The elves are running low on wrapping paper, and so they need to submit an order for more. 
# They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.
# Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift 
# a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present:
# the area of the smallest side.
# All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
def part_1():
	total = 0
	with open(input_dir+file, 'r') as f:
		for line in f:
			l, w, h = dimensions(line)
			sides = [l*w, w*h, h*l]
			slack = min(sides)
			surface = 2 * sum(sides)
			total += surface + slack
			
	print('The elves should order {} square feet of wrapping paper'.format(total))

# The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

# The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.
def part_2():
	total = 0
	with open(input_dir+file, 'r') as f:
		for line in f:
			l, w, h = dimensions(line)
			sides = [l, w, h]
			sides.remove(max(sides))
			volume = l*w*h
			total += 2 * sum(sides) + volume
			
	print('The elves should order {} square feet of ribbon'.format(total))