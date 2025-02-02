# -- coding: utf-8 --
"""
@author: 
    Name: Saksham Kumar
    Rollno: 24CS10029
"""

from math import sqrt

# functions

# common function for task 2 and task 6
def is_prime(n):
    k = int(sqrt(n))
    for i in range(2, k + 1):
        if n % i == 0:
            return False
    return True

def give_next_prime(n):
    
    while(1):
        if is_prime(n):
            return n
        n += 1


#function for task 1 
def count_sum_of_positive_integers(n):

    def helper(n, ptr, current_sum, count):
        if ptr > n:
            return count
        
        while(current_sum <= n):
            count = helper(n, ptr + 1, current_sum, count)
            current_sum += ptr
            if current_sum == n:
                count += 1

        return count


    if n == 0:
        return 0

    ans = helper(n, 1, 0, 0)
    return ans

# function for task 2
def count_sum_of_primes(n):

    
    def helper(n, ptr, current_sum, count):
        if ptr > n:
            return count

        next_prime = give_next_prime(ptr + 1)
        while(current_sum <= n):
            count = helper(n, next_prime, current_sum, count)
            current_sum += ptr
            if current_sum == n:
                count += 1

        return count


    if n == 0:
        return 0

    return helper(n, 2, 0, 0)


# function for task 3
def count_sum_of_distinct_positive_integers(n):
    
    def helper(n, current, count, k):

        if current == n:
            return count + 1

        if current > n or k > n:
            return count

        count = helper(n, current + k, count, k + 1)
        count = helper(n, current, count, k + 1)

        return count

    
    if (n == 0) :
        return 0
    ans =  helper(n, 0, 0, 1)
    return ans

# function for task 4
def count_sum_of_distinct_coins(n, coins):
    if n == 0:
        return 1 
    if len(coins) == 0:
        return 0

    def helper(n, coins, ptr, count, current):
        if current == n:
            return count + 1 

        if ptr >= len(coins) or current > n:
            return count

        count = helper(n, coins, ptr + 1, count, current + coins[ptr])
        count = helper(n, coins, ptr + 1, count, current)

        return count

    return helper(n, coins, 0, 0, 0)


# function for task 5
def count_sum_of_coins(n, coins):
    
    def helper(n, coins, ptr, count):
        if ptr >= len(coins) or n < 0:
            return count

        while(n > 0) :
            count = helper(n, coins, ptr + 1, count)
            n -= coins[ptr]
            if n == 0:
                count += 1

        return count

    if n == 0:
        return 1

    ans = helper(n, coins, 0, 0)
    return ans

# function for task 6
def count_sum_of_distinct_primes(n):
    
    def helper(n, ptr, current_sum, count):

        if current_sum == n:
            return count + 1
        if ptr > n or current_sum > n:
            return count

        next_prime = give_next_prime(ptr + 1)

        sum1 = current_sum
        sum2 = current_sum + ptr

        count = helper(n, next_prime, sum1, count)
        count = helper(n, next_prime, sum2, count)

        return count


    if n == 0:
        return 0
    return helper(n, 2, 0, 0)


# Test the program

    
if __name__ == "__main__":
    
    #Task 1: Number of ways to write V as a sum of positive integers
    assert count_sum_of_positive_integers(5) == 7  # (5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1)
    assert count_sum_of_positive_integers(1) == 1  # (1)
    assert count_sum_of_positive_integers(15) == 176  # 

    # Task 2: Number of ways to write V as a sum of prime numbers
    assert count_sum_of_primes(5) == 2  # (5, 2+3)
    assert count_sum_of_primes(2) == 1  # (2)
    assert count_sum_of_primes(15) == 12  # 
    assert count_sum_of_primes(10) == 5  # (7+3, 5+5, 5+3+2, 3+2+2+2, 2+2+2+2+2)
    #
    # # Task 3: Number of ways to write V as a sum of distinct positive integers
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

    # # Additional test cases
    #
    # # Task 4: Number of ways to write V using coins
    coins = [1, 2, 5]
    assert count_sum_of_coins(5, coins) == 4  # (5, 2+2+1, 2+1+1+1, 1+1+1+1+1)
    assert count_sum_of_coins(3, coins) == 2  # (2+1, 1+1+1)
    assert count_sum_of_coins(0, coins) == 1  # No coins needed for value 0
    assert count_sum_of_coins(7, coins) == 6  # (5+2, 5+1+1, 2+2+2+1, 2+2+1+1+1, 2+1+1+1+1+1, 1+1+1+1+1+1+1)

    # Additional test cases

    # 'Task 2: Prime number task with no valid combinations')
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