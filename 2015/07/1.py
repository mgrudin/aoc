import re

base_instructions = {}
instructions = {}

def get_instruction_value(id):
	value = instructions[id]
	if type(value) is not int:
		value = value.strip()
	else:
		return value
	command = re.findall(r'AND|OR|NOT|RSHIFT|LSHIFT', value)
	if len(command) == 0:
		numbers = re.findall(r'\d+', value)
		if len(numbers) > 0:
			instructions[id] = int(numbers[0])
			return int(numbers[0])
		else:
			return get_instruction_value(value)
	else:
		command = command[0]
		parts = value.split(command)
		part_a = parts[0].strip()
		part_b = parts[1].strip()
		signal_a = 0
		signal_b = 0
		if len(part_a) > 0:
			numbers_a = re.findall(r'\d+', part_a)
			signal_a = int(numbers_a[0]) if len(numbers_a) > 0 else get_instruction_value(part_a)
		if len(part_b) > 0:
			numbers_b = re.findall(r'\d+', part_b)
			signal_b = int(numbers_b[0]) if len(numbers_b) > 0 else get_instruction_value(part_b)

		signal = 0
		match command:
			case 'AND':
				signal = signal_a & signal_b
			case 'OR':
				signal = signal_a | signal_b
			case 'NOT':
				signal = ~ signal_b
			case 'RSHIFT':
				signal = signal_a >> signal_b
			case 'LSHIFT':
				signal = signal_a << signal_b
			case _:
				pass

		instructions[id] = signal
		return signal


with open('input.txt', 'r') as f:
	for line in f:
		splited_line = line.rstrip().split("->")
		base_instructions[splited_line[1].lstrip()] = splited_line[0]

instructions = base_instructions.copy()
wire_a_signal = get_instruction_value('a')
instructions = base_instructions.copy()
instructions['b'] = wire_a_signal

print(get_instruction_value('a'))
