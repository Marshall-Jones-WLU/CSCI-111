prime = []
z = 75
def primeNumbers(z):
    for p in range(1,z+1):
        if p > 1:
            for n in range(2,p):
                if (p % n) == 0:
                    break
            else:
                prime.append(p)
    print(prime)
primeNumbers(z)
