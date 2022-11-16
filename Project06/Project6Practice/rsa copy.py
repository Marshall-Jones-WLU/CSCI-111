import random
import math

def rsa_encrypt(msg,e,n): # encrypts an integer
    enc = pow(msg, e, n)
    return enc

def rsa_decrypt(enc,d,n): # decrypts an integer
    msg = pow(enc, d, n)
    return msg

def string_to_val(s = "hello"): # converts a string of characters to integers
    return int("".join(["{:07b}".format(ord(x)) for x in s]),2)
    
def val_to_string_natural(val = 28130883183): # converts integers to a string of characters
    s = []
    v = val
    while v > 0:
        s.append(v & 0b1111111)
        v = v >> 7
    s.reverse()
    g = [chr(x) for x in s]
    return "".join(g)

def rsa_encrypt_string(s,e,n):
    val = string_to_val(s)
    enc = rsa_encrypt(val,e,n)
    print("Your private key is the following:\n" + enc)

def rsa_decrypt_string(v,d,n):
    msg = rsa_decrypt(v,d,n)
    message = val_to_string_natural(msg)
    print(message)


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

def main():

    #_not_prime(a,d,n,r)
    
    n = int(input("What is the public key 'n'? "))
    e = int(input("What is the public key 'e'? "))
    choice = input("Are you trying to 'encrypt' a message or 'decrypt' a string? ")

    #_get_bases(n)

    if choice == "encrypt":
        s = input("What is your message? ")
        
        rsa_encrypt_string(s,e,n)
        
    elif choice == "decrypt":
        v = int(input("What is your private key? "))
        #v = 
        rsa_decrypt_string(v,e,n)

    else:
        print("I do not understand! Please enter either 'encrypt' or 'decrypt'.")
        print("The program will now restart.")
        main()

if __name__ == "__main__":
    main()
