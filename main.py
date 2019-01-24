# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 21:48:26 2019

@author: dheeraj_kumar
"""

def CompareValues(varOne,varTwo,varThree):
    '''
        CompareValues function that accepts 3 parameters and 
        checks for equality between any two of them.
        It return True if 2 or more of the parameters are equal, 
        and false is none of them are equal to any of the others.
    '''
    if int(varOne) == int(varTwo) or int(varOne) == int(varThree) or int(varTwo) == int(varThree):
        return True
    return False