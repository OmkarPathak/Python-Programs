
def sumOfAp(firstTerm, difference, terms):
    '''This function calculates the sum of first n terms of the AP'''
    sum = terms*(2*firstTerm + (terms-1)*difference)/2
    return sum

if __name__ == '__main__':
    firstTerm = float(input('Enter first term of AP : '))
    difference = float(input('Enter common difference : '))
    terms = int(input('Enter number of terms : '))
    sum = sumOfAp(firstTerm, difference, terms)
    print('Sum of AP : ', sum)
