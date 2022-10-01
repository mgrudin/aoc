instructions = ['turn on', 'turn off', 'toggle']
rows, cols = (1000, 1000)
grid = [[False for y in range(cols)] for x in range(rows)]

with open('input.txt', 'r') as f:
	for line in f:
		for i in instructions:
			if line.startswith(i):
				coords = line.removeprefix(i).strip().split('through')
				start = coords[0].split(',')
				start_x, start_y = (int(start[0]), int(start[1]))
				end = coords[1].split(',')
				end_x, end_y = (int(end[0]), int(end[1]))
				for x in range(start_x, end_x + 1):
					for y in range(start_y, end_y + 1):
						match i:
							case 'turn on':
								grid[x][y] = True
							case 'turn off':
								grid[x][y] = False
							case 'toggle':
								grid[x][y] = not grid[x][y]
							case _:
								print('Prefix does not fined')


print(sum(x.count(True) for x in grid))
