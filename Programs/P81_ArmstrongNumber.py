#A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if 
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

number = input('Enter a positive integer : ') #number to be checked
exponent = len(number) #number of digits
number = int(number) #convert string to int
copy = number #creating a copy of the original number to operate upon
sum = 0 #sum of cube of digits

#adding up the cube of each digit
while(copy>0):
    temp = copy%10
    sum+=temp**exponent
    copy = int(copy/10)

if(sum==number):
    print('Armstrong number')
else:
    print('Not an Armstrong number')
    
