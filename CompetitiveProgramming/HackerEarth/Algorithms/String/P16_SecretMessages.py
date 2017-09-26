# X and Y are best friends and they love to chat with each other. But their recent concerns about the privacy
# of their messages has distant them. So they decided to encrypt their messages with a key, K, such that the
# character of their messages are now shifted K times towards right of their initial value. Their techniques
# only convert numbers and alphabets while leaving special characters as it is.
#
# Provided the value K you are required to encrypt the messages using their idea of encryption.
#
# INPUT FORMAT
#
# The first line of the input contains, T, the number of messages. The next line contains N, and K, no of
# characters in the message and key for encryption. The next line contains the message.
#
# OUTPUT FORMAT
#
# Output the encrypted messages on a new line for all the test cases.
#
# CONSTRAINS
#
# 1≤T≤100
# 1≤N≤106
# 0≤K≤106
#
# SAMPLE INPUT
# 2
# 12 4
# Hello-World!
# 16 50
# Aarambh@1800-hrs
#
# SAMPLE OUTPUT
# Lipps-Asvph!
# Yypykzf@1800-fpq

myString = 'abcdefghijklmnopqrstuvwxyz'
myStringU = myString.upper()
nums = '0123456789'

def access_char(string, i):
	return string[i % len(string)]

for _ in range(int(input())):
	n, k = map(int, input().split())
	string = input()
	result = []

	for char in string:
		if char.islower() and char.isalpha():
			result.append(access_char(myString, myString.find(char) + k))
		elif char.isupper() and char.isalpha():
			result.append(access_char(myStringU, myStringU.find(char) + k))
		elif char.isnumeric():
			result.append(access_char(nums, nums.find(str(char)) + k))
		else:
			result.append(char)

	print(''.join([str(i) for i in result]))
	
