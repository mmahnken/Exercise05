from sys import argv

script, filename = argv

f = open(filename)
filetext = f.read()
f.close()

report = []

for char in filetext:
	report.append(char)

print report

letter_dict = {}

letter_count = 0

for letter in report:
	letter_dict.setdefault(letter, letter_count)
	occurs = letter_dict[letter]
	letter_dict[letter] = occurs + 1

print letter_dict