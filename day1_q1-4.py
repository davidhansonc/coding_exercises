# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-14 15:44:10
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-15 12:46:05
''' 
Question 1
'''
def find_nums(low_num, high_num):
    num_list = []
    for num in range(low_num, high_num+1):
        if num % 7 == 0 and num % 5 != 0:
            num_list.append(str(num))
    return ', '.join(num_list)

# print(find_nums(2000, 3200))

''' 
Question 2
'''
from functools import reduce

def factorial_calc(*number):
    results = []
    for num in number:
        results.append(str(reduce(lambda x,y: x*y, range(1, num+1))))
    return ', '.join(results)

# print(factorial_calc(8, 4, 5))

''' 
Question 3
'''
def number_dict(number):
    results = {}
    for num in range(1, number+1):
        results.update({num: num**2})
    return results

# print(number_dict(8))

''' 
Question 4
'''
def list_format_conv():
    num_list = input('Supply sequence of comma-separated numbers: ')
    nlist = num_list.split(',')
    ntuple = tuple(nlist)
    print(nlist)
    print(tuple(nlist))

# list_format_conv(number_list)