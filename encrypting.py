#RSA encryption

import math

chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#function determines the greatest common divisor of two given numbers
def gcd(x, y):
    while x > 0 and y > 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    if x == 0:
        return y
    elif y == 0:
        return x


#function checks if the number is prime
def isPrime(x):
    sqr = math.sqrt(x)
    n = 2
    if x > 2:
        while n-1 < sqr:
            if x % n == 0:
                return False
            else:
                return True
            n += 1
    elif x == 2:
        return True
    else:
        return False

#private key
print("p and q should be prime")
p = int(input("enter private key p="))
q = int(input("enter private key q="))

#public key
r = p*q
s = int(input("enter public key s="))
while gcd(s,p-1) != 1 and gcd(s,q-1) != 1:
    s = int(input("enter public key s="))


print("Your public key (r,s)=("+str(r)+","+str(s)+")")

#translating message into numbers
L = ""
message = input("enter your message ").upper()
for x in range(0, len(message)) :
    if chars.index(message[x])+1 < 10 and x != 0:
        L = L + "0" + str(chars.index(message[x])+1)
    else:
        L = L + str(chars.index(message[x])+1)

encrypted = (int(L)**s) % r

print("Encrypted message:",encrypted)