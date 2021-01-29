# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-14 15:44:10
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-15 13:52:04
'''
Question 5
'''
class StringClass():

    def __init__(self, x='default'):
        self.string_val = x

    def get_string(self):
        self.string_val = input('Give me a string! ')
        return self.string_val

    def print_string(self): 
        return self.string_val.upper()

# string_stuff = StringClass()
# string_stuff.get_string()
# print(string_stuff.print_string())

import unittest

class TestMain(unittest.TestCase):

    def testing_print(self):
        test_param = 'hello' 
        instantiated = StringClass(test_param)
        result = instantiated.print_string()
        self.assertEqual(result, 'HELLO')
        
unittest.main()
