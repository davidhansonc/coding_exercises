# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-15 13:53:01
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-22 09:50:28
'''
Question 9
'''
def capitalize():
    phrases = input()
    print(type(phrases))
    x = phrases.upper()
    return x

print(capitalize())


'''
Question 8
'''
def sort_words():
    csv_list = input("csv list of words: ").split(',')
    csv_list.sort()
    return ','.join(csv_list)

# print(sort_words())


'''
Question 7
'''
def array_gen(X, Y):
    array = [None] * X
    for index in range(len(array)):
        new_list = list(range(Y))
        array[index] = [element * index for element in new_list]
    return array


def receive_two_nums_csv():
    csv_list = input("csv list of integers: ")
    x, y = csv_list.split(',')
    return array_gen(int(x), int(y))

# print(array_gen(3, 5))
# print(receive_two_nums_csv())


'''
Question 6
'''
import numpy as np

def calculation(C=50, H=30):
    csv_list = input("csv list of integers: ")
    D_list = csv_list.split(',')
    Q_list = ''
    for D in D_list:
        Q = str(round(np.sqrt((2 * C * int(D)) / H))) + ','
        Q_list += Q
    return Q_list[:-1]

# print(calculation())