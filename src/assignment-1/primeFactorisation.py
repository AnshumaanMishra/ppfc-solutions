from math import ceil

isPrime = {0: False, 1: False, 2: True}

def checkPrime(n):
    for i in range(2, ceil(n ** 0.5) + 1):
        if(n % i == 0):
            isPrime[n] = False
            return False
    isPrime[n] = True
    return True

def smallestPrimeFactor(n):
    for i in range(2, n + 1):
        # print(isPrime)
        if(i in isPrime.keys()):
            if(isPrime[i] == True and n % i == 0):
                return i
            else:
                continue
        else:
            if checkPrime(i) and n % i == 0:
               return i

def primeFactorisarion(n):
    if(n == 1 or n == 0):
        return []
    if(n in isPrime.keys() and isPrime[n] == True):
        return [n]
    spf = smallestPrimeFactor(n)
    return [spf] + primeFactorisarion(n // spf)

a = int(input("Enter the number to find the prime factorisation: "))

print(a, "= ", end = '')
print(*primeFactorisarion(a), sep=" * ")
