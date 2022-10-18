len_original_strings = 0
len_escaped_strings = 0

with open('input.txt', 'r') as f:
	for l in f:
		line = l.strip()
		len_original_strings += len(line)
		escaped = line.translate(str.maketrans({
                                          "\\": r"\\",
                                          "\"": r"\""}))

		len_escaped_strings += len('"' + escaped + '"')

print(len_escaped_strings - len_original_strings)
