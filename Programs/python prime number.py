x=int(input('Enter the input number - '))
for i in range(2,(x//2)+1):
    s=0
    if x%i==0:
        s=s+1
if s>=1:
    print ('The given number is not a prime number(Composite number)')
else:
    print('The given number is a prime number')
        
