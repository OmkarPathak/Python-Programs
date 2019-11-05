# Author: OMKAR PATHAK

# PANGRAM: A sentence containing every letter of the alphabet.

from collections import Counter

def pangram(sentence):
	sentence = sentence.lower()
	check = 'abcdefghijklmnopqrstuvwxyz'
	alphabets = []
	for letter in sentence:
		if letter.isalpha():
			if letter in alphabets:
				pass
			else:
				alphabets.append(letter)

	alphabets = ''.join(alphabets)
	if Counter(check) == Counter(alphabets):
		return True
	else:
		return False

# A short version of above function:
def pangram2(sentence):
    alphabet = list(map(chr, range(97, 123)))
    formattedString = ''.join(c for c in sentence if c.isalpha()).lower()
    return set(alphabet) == set(formattedString)

if __name__ == '__main__':
    print(pangram('the quick brown fox jumps over the lazy dog'))       # True
    print(pangram('the_quick_brown_fox_jumps_over_the_lazy_dog'))       # True
    print(pangram('the 1 quick brown fish jumps over the 2 lazy dogs')) # False
    print(pangram('Five quacking Zephyrs jolt my wax bed.'))            # True
    print(pangram('the quick brown fox jumped over the lazy FOX'))      # False
    print(pangram(' '))                                                 # False
