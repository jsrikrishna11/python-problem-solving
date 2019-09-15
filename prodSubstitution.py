'''
    Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?
'''
import math

EPS = 1e-9
def array_product(a):
    prod =1 
    for i in a:
        prod*= i
    return prod
#simple solution using division
def simple(a):
    prod = array_product(a)
    result = []
    for i in a:
        result.append(int(prod/i))
    print(result)

#solution without division operator
'''
    we will create two 
'''
def complicated(a):
    return

input = [4,2,1,5]
simple(input)
complicated(input)