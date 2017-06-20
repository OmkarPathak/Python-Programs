# Chandan is an extremely biased person, and he dislikes people who fail to solve all the problems in the interview he
# takes for hiring people. There are n people on a day who came to be interviewed by Chandan.
#
# Chandan rates every candidate from 0 to 10. He has to output the total ratings of all the people who came in a day.
# But, here's the problem: Chandan gets extremely frustrated when someone ends up scoring a 0 in the interview. So in
# frustration he ends up removing the candidate who scored that 0, and also removes the candidate who came before him.
# If there is no candidate before the one who scores a 0, he does nothing.
#
# You've to find the summation of all the ratings in a day for Chandan.
#
# Input constraints:
# The first line of input will contain an integer — n. The next n lines will contain an integer, where the ith integer
# represents the rating of the ith person.
#
# Output constraints:
# Print the required sum.
#
# Constraints:
# 1 ≤ n ≤5 * 103
# 0 ≤ Value of ratings ≤10
#
# SAMPLE INPUT
# 5
# 2
# 3
# 0
# 7
# 0

# using for loop
myArray = []
sumAll = 0
countZero = 0

for i in range(int(input())):
    myInput = int(input())
    if myInput == 0:
      if countZero > 0:
        if countZero == 1:
          continue
        else:
          sumAll -= myArray[countZero - 1]
          del myArray[countZero - 1]
          countZero -= 1
    else:
      myArray.append(myInput)
      sumAll += myInput
      countZero += 1

print(sum(myArray))

# using while loop
n=int(input())
i=0
a=[]
while i<n:
      k=int(input())
      if k==0:
          if a!=[]:
              a.pop()
      else:
         a.append(k)
      i=i+1
print(sum(a))
