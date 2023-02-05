
#5. Uchta sondan kattasini qaytaradigan funksiya yarating.


s1 = int(input('enter 1 number:'))
s2 = int(input('enter 2 number:'))
s3 = int(input('enter 3 number:'))

def m(s1, s2, s3):
    Maxx = max(s1, max(s2, s3))
    print(Maxx)

m(s1, s2, s3)

