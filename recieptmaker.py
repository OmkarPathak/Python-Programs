sum = 0
recieptname=input("name your recipt")
try:
    f=open(f"{recieptname}.txt", "x")
    f.close()
except Exception as e:
    print(e)
reciept=[]
while(True):
    userinput=input("enter price")
    if userinput!="q":
        sum = sum+int(userinput)
        reciept.append(int(userinput))
        print(f"your total so far {sum}")
    else:
        print(f"thank for shooping with us")
        print(f"your total is {sum}")
        print(reciept)
        break
a=open(f"{recieptname}.txt", "a")
a.write(str(reciept))
a.close()

