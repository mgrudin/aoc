import math

places = {}
route = math.inf

def add_place(a, b, val):
	if a not in places:
		places[a] = {}

	places[a][b] = int(distance)

def add_places(nodes, distance):
	node_a, node_b = [node.strip() for node in nodes.split("to")]
	add_place(node_a, node_b, distance)
	add_place(node_b, node_a, distance)

def find_route(start, places, visited = None):
	if visited is None:
		visited  = set()
	visited.add(start)
	edges = places[start]
	min_route = math.inf
	end_point = ""

	for edge in edges:
		if edge in visited: continue
		if edges[edge] < min_route:
			end_point = edge
			min_route = edges[edge]
	if end_point == "": return 0
	return min_route + find_route(end_point, places, visited)


with open('input.txt', 'r') as f:
	for l in f:
		nodes, distance = [node.strip() for node in l.strip().split("=")]
		add_places(nodes, distance)

for place in places:
	new_route = find_route(place, places)
	if new_route < route:
		route = new_route

print(route)
