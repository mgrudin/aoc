f = open('input.txt', 'r')
input = f.readlines()
f.close()

def trim(str):
	return str.rstrip()

input = list(map(trim, input))

total_ribbon = 0

for d in input:
	sizes = d.split('x')
	sizes = list(map(int, sizes))
	sizes.sort()
	req_ribbon = (2 * sizes[0]) + (2 * sizes[1]) + (sizes[0] * sizes[1] * sizes[2])
	total_ribbon += req_ribbon

print(total_ribbon)
