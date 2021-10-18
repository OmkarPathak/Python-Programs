"""
health management software
this program is a sample project for healthmangement system.
you can edit the filenames and people names here.
this helps you to monitor your diet and exercises you do.
log means to enter diet or exercise.
retrive means to see what you have written.
"""
print("dont get worried when you see the below warnings")
print("there just coming because the file already exists")
print("but if you see this all warnings coming for the first time then put a issue on it")
try:
    firstfile=open("person1diet.txt","x")
except Exception as e:
    print(e)
try:
    secondfile=open("person2diet.txt","x")
except Exception as f:
    print(f)
try:
    thirdfile=open("person3diet.txt","x")
except Exception as j:
    print(j)
try:
    fourthfile=open("person1execise.txt","x")
except Exception as g:
    print(g)
try:
    fifthfile=open("person2exercise.txt","x")
except Exception as k:
    print(k)
try:
    sixthfile=open("person3exrciser.txt","x")
except Exception as m:
    print(m)
logorretrieve=int(input("press 0 for logging and press 1 for retrieveing\n"))
dietorexercise=int(input("press 0 for diet and press 1 for exercise\n"))
whomm=int(input('press 0 for person1,press 1 for person2 and press 2 for person3\n'))
def gettime():
    import datetime
    return datetime.datetime.now()
if logorretrieve == 0 and dietorexercise == 0 and whomm == 0:
    Food=input("what food you want to store\n")
    a=open("person1diet.txt","a+")
    time=str(gettime())
    a.write(time)
    a.write(Food)
    a.write("\n")
elif logorretrieve==0 and dietorexercise==0 and whomm==1:
    Foodr=input("what food you want to store\n")
    a=open("person2diet.txt","a+")
    time=str(gettime())
    a.write(time)
    a.write(Foodr)
    a.write("\n")
elif logorretrieve==0 and dietorexercise==0 and whomm==2:
    Foodh=input("what food you want to store\n")
    a=open("person3diet.txt","a+")
    time=str(gettime())
    a.write(time)
    a.write(Foodh)
    a.write("\n")
elif logorretrieve==0 and dietorexercise==1 and whomm==0:
    exercise=str(input("what exercise you want to store\n"))
    a=open("person1execise.txt","a+")
    time=str(gettime())
    a.write(time)
    a.write(exercise)
    a.write("\n")
elif logorretrieve==0 and dietorexercise==1 and whomm==1:
    exerciser=input("what exercise you want to store\n")
    a=open("person2exercise.txt","a+")
    time=str(gettime())
    a.write(time)
    a.write(exerciser)
    a.write("\n")
elif logorretrieve==0 and dietorexercise==1 and whomm==2:
    exerciseh=input("what exercise you want to store\n")
    a=open("person3exrciser.txt","a+")
    time=str(gettime())
    a.write(time)
    a.write(exerciseh)
    a.write("\n")
elif logorretrieve == 1 and dietorexercise == 0 and whomm == 0:
    a=open("person1diet.txt","r")
    print(a.read())
    input()
elif logorretrieve==1 and dietorexercise==0 and whomm==1:
    a=open("person2diet.txt","r")
    print(a.read())
    input()
elif logorretrieve==1 and dietorexercise==0 and whomm==2:
    a=open("person3diet.txt","r")
    print(a.read())
    input()
elif logorretrieve==1 and dietorexercise==1 and whomm==0:
    a=open("person1execise.txt","r")
    print(a.read())
    input()
elif logorretrieve==1 and dietorexercise==1 and whomm==1:
    a=open("person2exercise.txt","r")
    print(a.read())
    input()
elif logorretrieve==1 and dietorexercise==1 and whomm==2:
    a=open("person3exrciser.txt","r")
    print(a.read())
    input()
a.close()
