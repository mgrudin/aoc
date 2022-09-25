f = open('input.txt', 'r')
input = f.read().splitlines()
f.close()

def check_pair_letters(s):
	for i in range(len(s)):
		if i < len(s) - 2:
			subs = s[i] + s[i + 1]
			if subs in s[i + 2:len(s)]:
				return True
	return False

def check_letter_between(s):
	for i in range(len(s)):
		if i < len(s) - 2:
			if s[i] == s[i + 2]:
				return True
	return False

def is_nice(s):
	if check_pair_letters(s) and check_letter_between(s):
		return True
	return False

num_nice_str = 0

for s in input:
	if is_nice(s):
		num_nice_str += 1


print(num_nice_str)
