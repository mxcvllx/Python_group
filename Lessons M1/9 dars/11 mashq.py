""""""
"""11. Berilgan listda tub sonlar yig’indisini qaytaring.
"""
from math import sqrt



def checkPrime(numberToCheck):
    if numberToCheck == 1:
        return False

    for i in range(2, int(sqrt(numberToCheck)) + 1):

        if numberToCheck % i == 0:
            return False

    return True



def primeSum(l, r):
    sum = 0

    for i in range(r, (l - 1), -1):


        isPrime = checkPrime(i)

        if (isPrime):
            sum += i

    return sum



if __name__ == "__main__":
    l, r = 4, 13

    print(primeSum(l, r))


