import os
import random

players=[]
score=[]

print("\n\tRandom Number Game\n\nHello Everyone ! it is just a game of chance in which you have to guess a number"
      " from 0 to 100 and computer will tell whether your guess is smaller or bigger than the acctual number chossen by the computer . "
      "the person with less attempts in guessing the number will be winner .")
print("\n if you have understood the rools of game you may press enter and if not just call shivansh :)")
x=input()
os.system('cls')

n=int(input("Enter number of players : "))
print()

for i in range(0,n):
    name=input("Enter name of player : ")
    players.append(name)

os.system('cls')

for i in range(0,n):
    orignum=random.randint(1,100)
    print(players[i],"your turn :",end="\n\n")
    count=0
    while True :
        ch=int(input("Please enter your guess : "))
        if ch>orignum:
            print("no! number is smaller...")
            count+=1
        elif ch==orignum:
            print("\n\n\tcongrats you won")
            break
        else :
            print("nope ! number is large dude...")
            count+=1
    print("    you have taken", count+1,"attempts")
    x=input()
    score.append(count+1)
    os.system('cls')
print("players :\n")
for i in range(0,n):
    print(players[i],"-",score[i])

print("\n\nwinner is :\n")
for i in range(0,n):
    if score[i]==min(score):
        print(players[i])
x=input()
