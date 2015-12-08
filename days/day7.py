# --- Day 7: Some Assembly Required ---
# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.
# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

class Input:
	global wires
	def __init__(self,val):
		try:
			self.val = int(val)
			self.is_wire = False
		except ValueError:
			self.val = val
			self.is_wire = True			
	def has_signal(self):
		if self.is_wire:
			return self.val in wires
	def signal(self):
		if self.is_wire:
			return wires[self.val]
		else:
			return self.val

def get_instructions():
	with open('./inputs/day7.txt', 'r') as f:
		for line in f:
			instructions.append(parse_line(line))

def parse_line(line):
	i = line.split()
	if len(i) == 3:
		return ('SET', [Input(i[0])], i[2])
	elif len(i) == 4:
		return ('NOT', [Input(i[1])], i[3])
	elif len(i) == 5:
		return (i[1], [Input(i[0]), Input(i[2])], i[4])
			
def have_signals(inputs):
	for input in inputs:
		if input.is_wire and not input.has_signal():
			return False
	return True
	
def gate(type, i):
	if type == 'AND':
		return i[0].signal() & i[1].signal()
	elif type == 'OR':
		return i[0].signal() | i[1].signal()
	elif type == 'LSHIFT':
		return i[0].signal() << i[1].signal()
	elif type == 'RSHIFT':
		return i[0].signal() >> i[1].signal()
	elif type == 'NOT':
		return 0xffff & ~i[0].signal()

def run_circuit(output_wire = 'a', override_wire = None, input_signal = None):
	global wires, instructions
	wires.clear()
	run_instructions = instructions.copy()
	while len(run_instructions) > 0:
		line = run_instructions.pop(0)
		instr, inputs, output = line
		if have_signals(inputs):
			if instr == 'SET':
				if output == override_wire:
					wires[output] = input_signal
				else:
					wires[output] = inputs[0].signal()
			else:
				wires[output] = gate(instr, inputs)
		else:
			run_instructions.append(line)
	return wires[output_wire]
	
#--- Part One ---	
#In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
def part_1(output_wire = 'a'):
	print('Wire [{}] has the signal {} after running the circuit.'.format(output_wire, run_circuit(output_wire)))
	
#--- Part Two ---
#Now, take the signal you got on wire [a], override wire [b] to that signal, and reset the other wires (including wire [a]). What new signal is ultimately provided to wire [a]?
def part_2(output_wire = 'a', override_wire = 'b', override_signal = 'a'):
	input_signal = run_circuit(override_signal)
	print('Wire [{}] has the signal {} after running the circuit.'.format(output_wire, run_circuit(output_wire, override_wire, input_signal)))
	
wires, instructions = {}, []
get_instructions()