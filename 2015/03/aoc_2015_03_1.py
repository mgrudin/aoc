f = open('input.txt', 'r')
input = f.readline()
f.close()

visited_houses = [[0, 0]]

current_point = [0, 0]

for i in range(0, len(input)):
	match input[i]:
		case '<':
			current_point = [current_point[0] - 1, current_point[1]]
		case '>':
			current_point = [current_point[0] + 1, current_point[1]]
		case '^':
			current_point = [current_point[0], current_point[1] - 1]
		case 'v':
			current_point = [current_point[0], current_point[1] + 1]
		case _:
			break
	if current_point not in visited_houses:
		visited_houses.append(current_point)

print(len(visited_houses))
