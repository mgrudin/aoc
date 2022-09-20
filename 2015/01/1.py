f = open('input.txt', 'r')
input = f.readline()
f.close()

up = input.count('(')
down = input.count(')')

floor = 0 + up - down

print(floor)
