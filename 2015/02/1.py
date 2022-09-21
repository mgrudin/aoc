f = open('input.txt', 'r')
input = f.readlines()
f.close()

def trim(str):
	return str.rstrip()

input = list(map(trim, input))

total_paper = 0

for d in input:
	sizes = d.split('x')
	sizes = list(map(int, sizes))
	sizes.sort()
	req_paper = (2 * sizes[0] * sizes[1]) + (2 * sizes[1] * sizes[2]) + (2 * sizes[0] * sizes[2]) + sizes[0] * sizes[1]
	total_paper += req_paper

print(total_paper)
