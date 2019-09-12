'''

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''
input = [2,4,5,1,7,9,3]
sum= 5

def find_pairs(array, sum):
    for i in array:
        if sum-i in array:
            print (i,sum-i)

find_pairs(input, sum)
