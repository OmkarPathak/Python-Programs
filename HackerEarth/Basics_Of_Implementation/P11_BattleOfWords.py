# Alice and Bob are fighting over who is a superior debater. However they wish to decide this in a dignified manner. So 
# they decide to fight in the Battle of Words.
#
# In each game both get to speak a sentence. Because this is a dignified battle, they do not fight physically, the
# alphabets in their words do so for them. Whenever an alphabet spoken by one finds a match (same alphabet) spoken by the
# other, they kill each other. These alphabets fight till the last man standing.
#
# A person wins if he has some alphabets alive while the other does not have any alphabet left.
#
# Alice is worried about the outcome of this fight. She wants your help to evaluate the result. So kindly tell her if she
# wins, loses or draws.
#
# Input:
#
# First line contains an integer T denoting the number of games played.
# Each test case consists of two lines. First line of each test case contains a string spoken by Alice.
# Second line of each test case contains a string spoken by Bob.
#
# Note:
#
# Each sentence can have multiple words but the size of sentence shall not exceed 105.
#
# Output:
#
# For each game, output consists of one line each containing "You win some." if she wins ,"You lose some." if she loses or
# "You draw some." otherwise.
#
# Constraints:
#
# 1 ≤ T ≤ 10
# 1≤ |A|,| B| ≤ 105
# 'a' ≤ alphabet ≤ 'z'
# Each string contains atleast one alphabet.


T = int(input())
if(T>=1 and T<=10):

    for i in range(0,T):
        flag1=0
        flag2=0
        as1 = input()
        bs = input()

        #a = list(as1.split())
        #b = bs.split()

        for i in range(97,97+26):
            if(as1.count(chr(i))>bs.count(chr(i))):
                flag1=1
            elif(as1.count(chr(i))<bs.count(chr(i))):
                flag2=1
            if (flag1==1 and flag2==1):
                break
        #a = "".join(a)
        #b = "".join(b)

        if(flag1==1 and flag2==0):
            print("You win some.")
        elif(flag1==0 and flag2==1):
            print("You lose some.")
        else:
            print("You draw some.")
