import random
import math

def _get_bases(n):
    a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,41]
    k = int(math.log(n))
    if   n < 1373653:
        return a[:2]
    elif n < 25326001:
        return a[:3]
    elif n < 25000000000:
        return a[:4]
    elif n < 2152302898747:
        return a[:5]
    elif n < 3474748660383:
        return a[:6]
    elif n < 341550071728321:
        return a[:7]
    elif n < 3825123056546413051:
        return a[:8]
    elif n < 318665857834031151167461:
        return a[:-1]
    elif n < 3317044064679887385961981:
        return a
    else:
        return [random.randint(2,n-2) for x in range(k)]
        
def _not_prime(a,d,n,r):
    x = pow(a,d,n)
    if x==1 or x==n-1:
        return False
    else:
        for j in range(r):
            if x == n-1:
                return False
            x = pow(x,2,n)
    return True

def is_prime(n):
    '''
    Miller-Rabin primality test implemented by KLu
    n is number to test

    False means number is definitely not prime
    True means number is very likely a prime. (Certainly prime up to 2**64,
    might report false positives afterwards with low probability).
    '''
    
    #Implementation of the Miller-Rabin algorithm to test for prime numbers!
    #First check some small numbers
    if n < 3:
        return n==2
    if n < 10:
        if n==3 or n==5 or n==7:
            return True
        else:
            return False
            
    #If not an odd number, it's not prime!
    if not n%2:
        return False
        
    #Compute r and d such that 2**r * d + 1 == n
    d = n - 1
    r = 0
    while d%2 == 0:
        d = d // 2
        r += 1
        
    #Main tester, call helper
    for a in _get_bases(n):
        if _not_prime(a%n,d,n,r):
            return False
    return True

def rsa_keys(size = 16):
    size = int(input("What would you like for the size of your keys to be? "))
    e = 65537
    p = random.randint(2**(size/2-3), 2**(size/2))
    while True:
        if is_prime(p) == False or (p-1)%e == 0:
            p += 1
        else:
            break
    
    q = random.randint(2**size//p, 2**(size + 1)//p)
    while True:
        if is_prime(q) == False or (q-1)%e == 0:
            q += 1
        else:
            break
    n = p * q
    
    phi = (p-1)*(q-1)
    k = 1
    while True:
        if (k * phi + 1) % e != 0:
            k += 1
        else:
            break
    d = (k * phi + 1)//e

    keyList = [n,e,d]
    print("Your keys in the order of n, e, then d are in the following list:\n",keyList)
    print("\nThe public key n is:\n", n)
    print("\n\nThe public key e is:\n", e)
    print("\n\nYour private key d is:\n", d)
rsa_keys()
