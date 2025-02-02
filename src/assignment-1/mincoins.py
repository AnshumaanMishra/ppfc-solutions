# -*- coding: utf-8 -*-
"""

@author: AnshumaanMishra24CS10082

"""

'''
The code has been modified a little to incorporate the optional exercise in the same file.
'''


def min_coins(coins, value):
    """
    Finds the minimum number of coins required to make the given value using the given denominations.
    :param coins: List of coin denominations sorted in non-decreasing order.
    :param value: The target value to be made with the coins.
    :return: Minimum number of coins needed or -1 if not possible, list containing corresponding denominations
    """
    if(value == 0):
        return 0, []
    elif(value < 0):
        return -1, []
    maxList = []
    denoList = []
    retval = 0
    for i in coins:
        if(value >= i):
            retval, retlist = min_coins(coins, value - i)
            if(retval >= 0):
                maxList.append(1 + retval)
                denoList.append(retlist + [i])
    final = min(maxList) if len(maxList) > 0 else -1
    finList = []
    if(final != -1):
        for j in range(0, len(maxList)):
            if(maxList[j] == final):
                finList = denoList[j]
    return final, finList

'''
# Example usage
if __name__ == "__main__":
    coins = [1, 2, 4, 10, 11]
    value = 14
    retval, retlist = min_coins([1, 2, 4, 10, 11], 14)
    print(f"Minimum coins needed: {retval}")
    print(f"Coins needed: {retlist}")
'''
    # Tests using assert statements
if __name__ == "__main__":
    # Test 1: Basic case
    assert min_coins([1, 2, 5], 8)[0] == 3  # (1 + 2 + 5)
    assert min_coins([1, 2, 5], 6)[0] == 2  # (1 + 5)
    assert min_coins([1, 2, 5], 2)[0] == 1  # (2)
    assert min_coins([2], 3)[0] == -1  # Cannot form 3 with only 2-denomination coins
    assert min_coins([2, 3, 4], 6)[0] == 2  # (3 + 3 or 2+4)
    assert min_coins([1, 2, 5], 0)[0] == 0  # No coins needed for 0 value
    assert min_coins([2, 4, 6], 7)[0] == -1  # Cannot form 7 with even denominations
    assert min_coins([1, 2, 4, 10, 11], 14)[0] == 2  # (4+10) is a better solution than 1+2+11
    assert min_coins([3, 6, 8, 11, 14, 20], 14)[0] == 1
    assert min_coins([1, 3, 6, 8, 12, 14, 16], 20)[0] == 2

    print("All test cases passed!")
