f = open('input.txt', 'r')
input = f.read().splitlines()
f.close()

vowels = 'aeiou'
unacceptable_strings = ['ab', 'cd', 'pq', 'xy']

def check_vowels(s):
	num_vowels = 0
	for i in range(len(s)):
		if s[i] in vowels:
			num_vowels += 1
		if num_vowels >= 3:
			return True
	return False

def check_twice_in_a_row(s):
	for i in range(len(s)):
		if i < len(s) - 1 and s[i] == s[i + 1]:
			return True
	return False

def check_unacceptable_strings(s):
	for unst in unacceptable_strings:
		if unst in s:
			return False
	return True

def is_nice(s):
	if check_vowels(s) and check_twice_in_a_row(s) and check_unacceptable_strings(s):
		return True
	return False

num_nice_str = 0

for s in input:
	if is_nice(s):
		num_nice_str += 1


print(num_nice_str)
