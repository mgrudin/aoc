import hashlib

input = 'ckczppom'

i = 0

while not str(hashlib.md5((input + str(i)).encode()).hexdigest()).startswith('00000'):
	i += 1

print(i)
