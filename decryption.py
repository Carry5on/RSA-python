# RSA decryption

chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', "Z"]


# function determines the greatest common divisor of two given numbers
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


C = int(input("enter your encrypted message"))

# private key
print("p and q should be prime")
p = int(input("enter private key p="))
q = int(input("enter private key q="))

# public key
r = p * q
s = int(input("enter public key s="))
'''
while gcd(s,p-1) != 1 and gcd(s,q-1) != 1:
    s = int(input("enter public key s="))
'''

print("Your public key (r,s)=(" + str(r) + "," + str(s) + ")")


# looking for a and c from s*a+(p-1)*b=1 and s*c+(q-1)*d=1, using extended Euclidean algorithm
def ext_Eucl(a, b):
    aa = a
    bb = b
    x_a, y_a, x_b, y_b = 1, 0, 0, 1
    while a * b != 0:
        if a >= b:
            x_a -= x_b * (a // b)
            y_a -= y_b * (a // b)
            a %= b
        else:
            x_b -= x_a * (b // a)
            y_b -= y_a * (b // a)
            b %= a

    if a > 0:
        x = x_a
        y = y_a
    elif b > 0:
        x = x_b
        y = y_b
    while x < bb:
        x += bb
    while x >= bb:
        x -= bb
    return [x, y]


A = ext_Eucl(s, p - 1)[0]
B = ext_Eucl(s, q - 1)[0]

m_1 = p
m_2 = q
M = m_1 * m_2
a_1 = C ** A % (m_1)
a_2 = C ** B % (m_2)
X = ext_Eucl(M / m_1, m_1)[0]
Y = ext_Eucl(M / m_2, m_2)[0]

# L=(M/m_!*a_1*X+M/m_2*a_2*Y)(mod M)
# extend it to multiple variables Chinese remainder theorem
L = int(((M / m_1 * a_1 * X) + (M / m_2 * a_2 * Y)) % (M))
answer = "Info: "

'''
#test values

print("a=",A)
print("a'=",B)
print("a_1=",a_1)
print("a_2=",a_2)
print("x_1=",X)
print("x_2=",Y)
print("L=",L)
'''

L = str(L)
# adding 0 at the beginning if needed
if len(L) % 2 != 0:
    L = "0" + L

print(L)
'''   
n = 0
while n < len(L):    
    k = int(L[n:n+2])-1
    answer += chars[k]
    n += 2     

print(answer)  
'''