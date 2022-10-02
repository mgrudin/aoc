rows, cols = (1000, 1000)
grid = [[0 for y in range(cols)] for x in range(rows)]

def get_prefix(s):
	instructions = ['turn on', 'turn off', 'toggle']
	for i in instructions:
		if s.startswith(i):
			return i

def change_grid(coords, prefix):
	start = coords[0].split(',')
	start_x, start_y = (int(start[0]), int(start[1]))
	end = coords[1].split(',')
	end_x, end_y = (int(end[0]), int(end[1]))
	for x in range(start_x, end_x + 1):
		for y in range(start_y, end_y + 1):
			change_bulb(prefix, x, y)


def change_bulb(prefix, x, y):
	match prefix:
		case 'turn on':
			grid[x][y] += 1
		case 'turn off':
			if grid[x][y] > 0:
				grid[x][y] -= 1
		case 'toggle':
			grid[x][y] += 2
		case _:
			print('Prefix does not fined')

with open('input.txt', 'r') as f:
	for line in f:
		prefix = get_prefix(line)
		coords = line.removeprefix(prefix).strip().split('through')
		change_grid(coords, prefix)



print(sum(sum(x) for x in grid))
