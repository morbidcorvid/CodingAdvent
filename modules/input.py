class Input:
	def __init__(self, file_name):
		input_dir = './inputs/'
		with open(input_dir+file_name, 'r') as f:
			self.input = f.read()
		self.position = 0
	def next_char(self):
		self.position += 1
		return self.input[self.position]
	def prev_char(self):
		self.position -= 1
		return self.input[self.position]
		