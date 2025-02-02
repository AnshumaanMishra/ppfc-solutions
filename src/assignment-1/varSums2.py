# -*- coding: utf-8 -*-
"""
@author:
    Name: Anshumaan Mishra
    Rollno: 24CS10082
"""

'''
Please Note that the functions have been modified to return both the number of possible sums and the possible sums
Hence, the number of sums is represented by `function(argument)[0]`
'''

from math import ceil

def generaliser(value, pool, sumArr, listArr, checkFunction, additionalCondition, new, con2, retBase):
    if(value in sumArr.keys()):
        return sumArr[value], listArr[value]
    # pool = range(2, value + 1)
    if(value == 0):
        return 1, [[]]
    if(new and value == 1):
        return 0, [[]]
    if(value < 0):
        return retBase, [[]]
    denoList = list()
    for i in pool:
        if(value >= i):
            if(checkFunction(i)):
                retval, retlist = generaliser(value - i, pool, sumArr, listArr, checkFunction, additionalCondition, new, con2, retBase)
                if(retval > 0 or con2(retval)):
                    for j in retlist:
                        if(additionalCondition and i in j):
                            continue
                        currentList = sorted(j + [i])
                        if(currentList not in denoList):
                            denoList.append(currentList)
        else:
            break
    final = len(denoList) if len(denoList) > 0 else 0
    sumArr[value] = final
    listArr[value] = denoList
    return sumArr[value], (denoList)


def count_sum_of_positive_integers(value):
    posint = {0: 0, 1: 1, 2: 2}
    posarr = {0: [[]], 1:[[1]], 2:[[1, 1], [2]]}

    return generaliser(value, range(1, value + 1), posint, posarr, lambda x: value >= x, False, False, lambda x: 0 == x, 0)[0]

def count_sum_of_primes(value):
    isPrime = {0: False, 1: False, 2: True}
    def checkPrime(n):
        if(n in isPrime.keys()):
            return isPrime[n]
        for i in range(2, ceil(n ** 0.5) + 1):
            if(n % i == 0):
                isPrime[n] = False
                return False
        isPrime[n] = True
        return True
    primSum = {0: 1, 1: 0, 2: 1, 3: 1, 4: 1}
    primArr = {0: [[]], 1: [[]], 2: [[2]], 3: [[3]], 4: [[2, 2]]}

    return generaliser(value, range(2, value + 1), primSum, primArr, checkPrime, False, True, lambda x: False, 0)[0]

def count_sum_of_distinct_primes(value):
    isPrime = {0: False, 1: False, 2: True}
    def checkPrime(n):
        if(n in isPrime.keys()):
            return isPrime[n]
        for i in range(2, ceil(n ** 0.5) + 1):
            if(n % i == 0):
                isPrime[n] = False
                return False
        isPrime[n] = True
        return True
    primSum = {0: 1, 1: 0, 2: 1, 3: 1, 4: 1}
    primArr = {0: [[]], 1: [[]], 2: [[2]], 3: [[3]], 4: [[2, 2]]}
    
    return generaliser(value, range(2, value + 1), primSum, primArr, checkPrime, True, True, lambda x: False, 0)[0]


def count_sum_of_distinct_positive_integers(value):
    posDint = {0: 0, 1: 1, 2: 1}
    posDarr = {0: [[]], 1:[[1]], 2:[[2]]}

    return generaliser(value, range(1, value + 1), posDint, posDarr, lambda x: True, True, False, lambda x: x == 0, 0)[0]


def count_sum_of_distinct_coins(value, coins):
    coinVals = {0: 1}
    coinArrs = {0: [[]]}

    return generaliser(value, coins, coinVals, coinArrs, lambda x: True, True, False, lambda x: x == 0, -1)[0]

def count_sum_of_coins(value, coins):
    coinVals = {0: 1}
    coinArrs = {0: [[]]}

    return generaliser(value, coins, coinVals, coinArrs, lambda x: True, False, False, lambda x: x == 0, -1)[0]

    
if __name__ == "__main__":
    #print(count_sum_of_positive_integers(5))
    #print(count_sum_of_positive_integers(1))
    #print(count_sum_of_positive_integers(15))

    # Task 1: Number of ways to write V as a sum of positive integers
    assert count_sum_of_positive_integers(5) == 7  # (5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1)
    assert count_sum_of_positive_integers(1) == 1  # (1)
    assert count_sum_of_positive_integers(15) == 176  #

    # Task 2: Number of ways to write V as a sum of prime numbers
    assert count_sum_of_primes(5) == 2  # (5, 2+3)
    assert count_sum_of_primes(2) == 1  # (2)
    assert count_sum_of_primes(15) == 12  #
    assert count_sum_of_primes(10) == 5  # (7+3, 5+5, 5+3+2, 3+2+2+2, 2+2+2+2+2)

    # Task 3: Number of ways to write V as a sum of distinct positive integers
    assert count_sum_of_distinct_positive_integers(5) == 3  # (5, 2+3, 1+4)
    assert count_sum_of_distinct_positive_integers(6) == 4  # (6, 1+5, 2+4, 1+2+3)
    assert count_sum_of_distinct_positive_integers(1) == 1  # (1)
    assert count_sum_of_distinct_positive_integers(15) == 27  #


    # Task 4: Number of ways to write V using distinct coins
    coins = [1, 4, 5, 7, 8, 10]
    assert count_sum_of_distinct_coins(5, coins) == 2  # (5, 4+1)
    assert count_sum_of_distinct_coins(3, coins) == 0  # cannot be done
    assert count_sum_of_distinct_coins(0, coins) == 1  # No coins needed for value 0
    assert count_sum_of_distinct_coins(15, coins) == 3  # (10+5, 10+4+1, 8+7)

    # Additional test cases

    # Task 4: Number of ways to write V using coins
    coins = [1, 2, 5]
    assert count_sum_of_coins(5, coins) == 4  # (5, 2+2+1, 2+1+1+1, 1+1+1+1+1)
    assert count_sum_of_coins(3, coins) == 2  # (2+1, 1+1+1)
    assert count_sum_of_coins(0, coins) == 1  # No coins needed for value 0
    assert count_sum_of_coins(7, coins) == 6  # (5+2, 5+1+1, 2+2+2+1, 2+2+1+1+1, 2+1+1+1+1+1, 1+1+1+1+1+1+1)

    # Additional test cases

    #'Task 2: Prime number task with no valid combinations')
    assert count_sum_of_primes(1) == 0  # No primes sum to 1


    # Task 4: Coins where no combination is possible
    assert count_sum_of_distinct_coins(3, [2, 4]) == 0  # Cannot sum to 3 with coins [2, 4]
    assert count_sum_of_distinct_coins(7, [10]) == 0  # Cannot sum to 7 with a single coin 10

    print("All test cases passed!")

    #New Examples to run
    V=20
    # Task 1: Number of ways to write V as a sum of positive integers
    print(f"Task 1: Number of ways to write {V} as a sum of positive integers:  {count_sum_of_positive_integers(V)}")

    # Task 2: Number of ways to write V as a sum of prime numbers
    print(f"Task 2: Number of ways to write {V} as a sum of prime numbers: {count_sum_of_primes(V)}")

    # Task 3: Number of ways to write V as a sum of distinct positive integers
    print(f"Task 3: Number of ways to write {V} as a sum of distinct positive integers {count_sum_of_distinct_positive_integers(V)}")

    # Additional Task 6: Number of ways to write V as a sum of distinct prime numbers
    print(f"Task 6: Number of ways to write {V} as a sum of distinct prime numbers: {count_sum_of_distinct_primes(V)}")
    # Task 4: Number of ways to write V using coins
    V=30
    coins = [1, 2, 5, 7, 8, 10, 12, 18, 20]

    print(f"Task 4: Number of ways to write {V} using distinct coins from {coins}: {count_sum_of_distinct_coins(V, coins)}")

    # Additional Task 5:
    print(f"Task 5: Number of ways to write {V} using coins from {coins} that can repeat: {count_sum_of_coins(V, coins)}")
