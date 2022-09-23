f = open('input.txt', 'r')
input = f.readline()
f.close()

visited_houses = [[0, 0]]

current_point_Santa = [0, 0]
current_point_RoboSanta = [0, 0]


for i in range(0, len(input)):
	point = current_point_RoboSanta if i % 2 else current_point_Santa
	match input[i]:
		case '<':
			point = [point[0] - 1, point[1]]
		case '>':
			point = [point[0] + 1, point[1]]
		case '^':
			point = [point[0], point[1] - 1]
		case 'v':
			point = [point[0], point[1] + 1]
		case _:
			break
	if point not in visited_houses:
		visited_houses.append(point)
	if i % 2:
		current_point_RoboSanta = point
	else:
		current_point_Santa = point

print(len(visited_houses))
