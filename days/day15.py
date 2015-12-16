''' Day 15: Science for Hungry People
	Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

	Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

		- capacity (how well it helps the cookie absorb milk)
		- durability (how well it keeps the cookie intact when full of milk)
		- flavor (how tasty it makes the cookie)
		- texture (how it improves the feel of the cookie)
		- calories (how many calories it adds to the cookie)
		
	You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.
'''

def get_ingredients(filename = './inputs/day15.txt'):
	''' Returns dictionary of ingredients and their properties
	'''
	ingredients = {}
	with open(filename, 'r') as f:
		for line in f:
			i, lp = line.split(':')
			props = {}
			for p in lp.split(','):
				prop, val = p.split()
				props[prop] = int(val)
			ingredients[i] = props
	return ingredients
	
def prop_score(ingredients, mix, prop):
	''' Returns the score for a cookie property in a recipe. 
		Sums the quantity of each ingredient in a mix * value of the ingredients property.
	'''
	score = 0
	for i in ingredients:
		score += ingredients[i][prop] * mix[i]
	return score

def total_score(ingredients, mix):
	''' Returns total score for a cookie recipie. 
		Multiplies the scores of all cookie properties (except calories) to calculate total score
	'''
	total_score = 1
	for p in next(iter(ingredients.values())):
		if p != 'calories':
			score = prop_score(ingredients, mix, p)
			total_score = total_score * max(score, 0)
	return total_score, mix

def find_best(ingredients, used, mix, total, calories = 0):
	''' Returns total score and recipe that makes it. 
		Recursive function to test all possible combinations of ingredients and find highest score. 
	'''
	i,p = ingredients.popitem()
	used[i] = p
	# determine how much space left in recipe
	u = sum([i for i in mix.values()])
	# if all other ingredients used, fill with last ingredient
	if len(ingredients) == 0:
		mix[i] = total - u
		u = total
	# if mix is full, calculate score of recipe and return
	if u == total:
		# if counting calories, ignore scores where calorie counts don't match
		if calories == 0 or (calories > 0 and prop_score(used, mix, 'calories') == 500):
			return total_score(used, mix)
		else:
			return 0, mix		
	best_score, best_mix = 0, {}
	# increment through all possible combinations
	for t in range(0, total+1):
		mix[i] = t
		score, nmix = find_best(ingredients.copy(), used.copy(), mix.copy(), total, calories)
		if score > best_score:
			best_score, best_mix = score, nmix
	return best_score, best_mix
	
def part_1(teaspoons = 100):
	''' Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?
	
		Prints highest total score and the recipe to make it
	'''
	ingredients, mix, used = get_ingredients(), {}, {}
	for i in ingredients:
		mix[i] = 0
	print(find_best(ingredients, used, mix, teaspoons))

def part_2(teaspoons = 100, calories = 500):
	'''	Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?
	
		Prints highest total score and the recipe to make it
	'''
	ingredients, mix, used = get_ingredients(), {}, {}
	for i in ingredients:
		mix[i] = 0
	print(find_best(ingredients, used, mix, teaspoons, calories))