""""""""


"""
4 Kiritilgan sondan keyingi tub sonni topuvchi funksiya yarting
"""

n = int(input())


def nextprime(n):
    prime = 0
    n += 1
    for i in range(2, int(n ** 0.5) + 2):
        if n % i == 0:
            prime = 0
            break
        else:
            prime = 1
    if prime == 1:
        print(n)
        return

    else:
        return


nextprime(n)