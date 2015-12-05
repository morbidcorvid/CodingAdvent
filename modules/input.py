class Input:
	def __init__(self, file_name):
		input_dir = './inputs/'
		with open(input_dir+file_name, 'r') as f:
			self.input = f.read().strip()
		self.len = len(self.input)
		self.position = -1
	def next_char(self):
		if self.position < self.len:
			self.position += 1
			return self.input[self.position]
		else:
			return False
	def prev_char(self):
		self.position -= 1
		return self.input[self.position]
		