#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Assignment 1, Problem 1: Weightlifting

Team Number:
Student Names:
Marc Pérez Sabater
Roberto Pérez Rico
'''

'''
Copyright: justin.pearson@it.uu.se and his teaching assistants, 2020.

This file is part of course 1DL231 at Uppsala University, Sweden.

Permission is hereby granted only to the registered students of that
course to use this file, for a homework assignment.

The copyright notice and permission notice above shall be included in
all copies and extensions of this file, and those are not allowed to
appear publicly on the internet, both during a course instance and
forever after.
'''
from typing import *  # noqa
import unittest  # noqa
import math  # noqa
from src.weightlifting_data import data  # noqa
# If your solution needs a queue, then you can use this one:
from collections import deque  # noqa
# If you need to log information during tests, execution, or both,
# then you can use this library:
# Basic example:
#   logger = logging.getLogger("put name here")
#   a = 5
#   logger.debug(f"a = {a}")
import logging  # noqa

__all__ = ['weightlifting', 'weightlifting_subset']


def weightlifting(P: Set[int], weight: int) -> bool:
    print(P)
    print(f'weight: {weight}')
    '''
    Sig:  Set[int], int -> bool
    Pre:
    Post:
    Ex:   P = {2, 32, 234, 35, 12332, 1, 7, 56}
          weightlifting(P, 299) = True
          weightlifting(P, 11) = False
    '''
    plate_list = list(P)
    plate_list.sort()
    if weight == 0: return True

    # Initialise the dynamic programming matrix
    dp_matrix = [
        [None for i in range(weight + 1)] for j in range(len(plate_list) + 1)]
    dp_matrix[0][0]= True;

    for p in range(1,len(plate_list) + 1):
        #print(f'p : {p}')
        for i in range (weight+1):
            #print(f'{i}: {dp_matrix[p-1][i]}')
            if dp_matrix[p-1][i] is not None:
                dp_matrix[p][i] = True
            if dp_matrix[p-1][i] is None:
                #print(f'lista: {plate_list[0:p]}')
                dp_matrix[p][i] = aux_sum(i,plate_list,p-1)
                #print(f'new {i}: {dp_matrix[p][i]}')
    print(dp_matrix[-1][-1])
    if dp_matrix[-1][-1] is None:
        return False
    return True
def aux_sum(weight: int, plates , n  : int):
    if weight == 0:
        return True
    if n < 0:
        return None
    #print(f'plates[n]: {plates[n]} and weight : {weight}')
    if plates[n] > weight:
        return aux_sum(weight,plates, n-1)
    return aux_sum(weight,plates, n-1) or aux_sum(weight - plates[n],plates, n-1 )

def weightlifting_subset(P: Set[int], weight: int) -> Set[int]:
    '''
    Sig:  Set[int], int -> Set[int]
    Pre:
    Post:
    Ex:   P = {2, 32, 234, 35, 12332, 1, 7, 56}
          weightlifting_subset(P, 299) = {56, 7, 234, 2}
          weightlifting_subset(P, 11) = {}
    '''

'''    
def weightlifting(P: Set[int], weight: int) -> bool:
    
    Sig:  Set[int], int -> bool
    Pre:
    Post:
    Ex:   P = {2, 32, 234, 35, 12332, 1, 7, 56}
          weightlifting(P, 299) = True
          weightlifting(P, 11) = False
    
    n = len(list(P))
    return subset_aux_sum(P=list(P), n=n, weight=weight)


def subset_aux_sum(P, n, weight):
    if weight == 0:
        return True
    if n == 0:
        return False
    if P[n - 1] > weight:
        return subset_aux_sum(P, n - 1, weight)
    return subset_aux_sum(P,n-1, weight) or subset_aux_sum(P, n-1, weight - P[n-1])


def weightlifting_subset(P: Set[int], weight: int) -> Set[int]:
    
    Sig:  Set[int], int -> Set[int]
    Pre:
    Post:
    Ex:   P = {2, 32, 234, 35, 12332, 1, 7, 56}
          weightlifting_subset(P, 299) = {56, 7, 234, 2}
          weightlifting_subset(P, 11) = {}
    

    n = len(list(P))
    return subset_aux_sum_set(P=list(P), n=n, weight=weight, wset = [])


def subset_aux_sum_set(P, n, weight, wset):
    if weight == 0:
        print(wset)
        return set(wset)
    if n == 0:
        return []
    if P[n - 1] > weight:
        return subset_aux_sum(P, n - 1, weight,wset)
    return subset_aux_sum(P, n - 1, weight,wset) + subset_aux_sum(P, n - 1, weight - P[n - 1],wset+[P[n-1]])
'''
#print(weightlifting({2, 32, 234, 35, 12332, 1, 7, 56},299))
class WeightliftingTest(unittest.TestCase):
    """
    Test Suite for weightlifting problem

    Any method named "test_something" will be run when this file is executed.
    Use the sanity check as a template for adding your own test cases if you
    wish. (You may delete this class from your submitted solution.)
    """
    logger = logging.getLogger('WeightLiftingTest')
    data = data
    weightlifting = weightlifting
    weightlifting_subset = weightlifting_subset

    def test_satisfy_sanity(self):
        """
        Sanity Test for weightlifting()

        passing is not a guarantee of correctness.
        """
        plates = {2, 32, 234, 35, 12332, 1, 7, 56}
        self.assertTrue(
            WeightliftingTest.weightlifting(plates, 299)
        )
        self.assertFalse(
            WeightliftingTest.weightlifting(plates, 11)
        )

    def test_subset_sanity(self):
        """
        Sanity Test for weightlifting_subset()

        passing is not a guarantee of correctness.
        """
        plates = {2, 32, 234, 35, 12332, 1, 7, 56}
        weight = 299
        sub = WeightliftingTest.weightlifting_subset(plates, weight)
        for p in sub:
            self.assertIn(p, plates)
        self.assertEqual(sum(sub), weight)

        weight = 11
        sub = WeightliftingTest.weightlifting_subset(plates, weight)
        self.assertSetEqual(sub, set())

    def test_satisfy(self):
        for instance in self.data:
            self.assertEqual(
                WeightliftingTest.weightlifting(instance["plates"],
                                                instance["weight"]),
                instance["expected"]
            )

    def test_subset(self):
        """
        Sanity Test for weightlifting_subset()

        passing is not a guarantee of correctness.
        """
        for instance in self.data:
            plates = WeightliftingTest.weightlifting_subset(
                instance["plates"].copy(),
                instance["weight"]
            )
            self.assertEqual(type(plates), set)

            for plate in plates:
                self.assertIn(plate, instance["plates"])

            if instance["expected"]:
                self.assertEqual(
                    sum(plates),
                    instance["weight"]
                )
            else:
                self.assertSetEqual(
                    plates,
                    set()
                )


if __name__ == '__main__':
    # Set logging config to show debug messages.
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()