
from codecs import decode

len_literals = 0
len_strings = 0

with open('input.txt', 'r') as f:
	for l in f:
		line = l.strip()
		len_literals += len(line)

		len_strings += len(decode(line[1:-1], 'unicode_escape'))


print(len_literals - len_strings)
