# John has recently learned about ASCII values. With his knowledge of ASCII values and character he has
# developed a special word and named it John's Magical word.
#
# A word which consists of alphabets whose ASCII values is a prime number is a John's Magical word. An
# alphabet is john's Magical alphabet if its ASCII value is prime.
#
# John's nature is to boast about the things he know or have learnt about. So just to defame his friends he
# gives few string to his friends and ask them to convert it to John's Magical word. None of his friends would
# like to get insulted. Help them to convert the given strings to John's Magical Word.
#
# Rules for converting:
#
# 1.Each character should be replaced by the nearest John's Magical alphabet.
#
# 2.If the character is equidistant with 2 Magical alphabets. The one with lower ASCII value will be considered as its replacement.
#
# Input format:
#
# First line of input contains an integer T number of test cases. Each test case contains an integer N (denoting the length of the string) and a string S.
#
# Output Format:
#
# For each test case, print John's Magical Word in a new line.
#
# Constraints:
#
# 1 <= T <= 100
#
# 1 <= |S| <= 500
#
# SAMPLE INPUT
# 1
# 8
# KINGKONG
#
# SAMPLE OUTPUT
# IIOGIOOG

numl = [97, 101, 103, 107, 109, 113]
numu = [67, 71, 73, 79, 83, 89]
num = [67, 89, 97, 113]

for _ in range(int(input())):
	length = input()
	string = input()
	result = ''

	for char in string:
		if char.islower() and char.isalpha():
			minimum = 200
			ascii_char = ord(char)
			temp = 0

			for j in numl:
				if minimum > abs(ascii_char - j):
					minimum = abs(ascii_char - j)
					temp = j

			result = result + chr(temp)

		elif char.isupper() and char.isalpha():
			minimum = 200
			ascii_char = ord(char)
			temp = 0

			for j in numu:
				if minimum > abs(ascii_char - j):
					minimum = abs(ascii_char - j)
					temp = j

			result = result + chr(temp)

		else:
			minimum = 200
			ascii_char = ord(char)
			temp = 0

			for j in num:
				if minimum > abs(ascii_char - j):
					minimum = abs(ascii_char - j)
					temp = j

			result = result + chr(temp)

	print(result)
