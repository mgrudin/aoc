f = open('input.txt', 'r')
input = f.readline()
f.close()

floor = 0

for pos in range(0, len(input)):
	if input[pos] == '(':
		floor += 1
	if input[pos] == ')':
		floor -= 1
	if floor == -1:
		print(pos + 1)
		break
