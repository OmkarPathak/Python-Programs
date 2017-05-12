# Author: OMKAR PATHAK

# ISOGRAM: An isogram (also known as a "nonpattern word") is a logological term for a word
# or phrase without a repeating letter

def is_isogram(word):
    # Convert the word or sentence in lower case letters.
    clean_word = word.lower()
    # Make ann empty list to append unique letters
    letter_list = []
    for letter in clean_word:
        # If letter is an alphabet then only check
        if letter.isalpha():
            if letter in letter_list:
                return False
            letter_list.append(letter)

    return True

if __name__ == '__main__':
    print(is_isogram(""))
    print(is_isogram("isogram"))
    print(is_isogram("eleven"))
    print(is_isogram("subdermatoglyphic"))
    print(is_isogram("Alphabet"))
    print(is_isogram("thumbscrew-japingly"))
    print(is_isogram("Hjelmqvist-Gryb-Zock-Pfund-Wax"))
    print(is_isogram("Emily Jung Schwartzkopf"))
    print(is_isogram("accentor"))
