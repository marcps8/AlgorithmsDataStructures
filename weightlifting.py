#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Assignment 1, Problem 1: Weightlifting

Team Number: 40
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
    '''
    Sig:  Set[int], int -> bool
    Pre: P is a Set of integers representing plates with different weights,
        weight is an integer representing the weight we want to get using our plates
    Post: True if we can get exactly weight using a subset of the set of the plates
    Ex:   P = {2, 32, 234, 35, 12332, 1, 7, 56}
          weightlifting(P, 299) = True
          weightlifting(P, 11) = False
    '''
    plate_list = list(P)
    # Initialise the dynamic programming matrix
    dp_matrix = [
        [None for i in range(weight + 1)] for j in range(len(plate_list) + 1)
    ]

    for i in range(len(plate_list) + 1):
        # Invariant:
        # Variant:
        dp_matrix[i][0] = True

    for i in range(1, len(plate_list) + 1):
        # Invariant:
        # Variant:
        for j in range(1, weight + 1):
            # Invariant:
            # Variant:
            if plate_list[i - 1] > j:
                dp_matrix[i][j] = dp_matrix[i - 1][j]
            else:
                dp_matrix[i][j] = dp_matrix[i - 1][j] or dp_matrix[i - 1][j - plate_list[i - 1]]
    if dp_matrix[-1][-1] is None:
        return False
    return True

def weightlifting_subset(P: Set[int], weight: int) -> Set[int]:
    '''
    Sig:  Set[int], int -> Set[int]
    Pre:P is a Set of integers representing plates with different weights,
        weight is an integer representing the weight we want to get using our plates
    Post: return the subset of plates with which we get exactly the weight, if we can't
        obtain it we return the empty set
    Ex:   P = {2, 32, 234, 35, 12332, 1, 7, 56}
          weightlifting_subset(P, 299) = {56, 7, 234, 2}
          weightlifting_subset(P, 11) = {}
    '''
    plate_list = list(P)
    # Initialise the dynamic programming matrix
    dp_matrix = [
        [(None,set()) for i in range(weight + 1)] for j in range(len(plate_list) + 1)
    ]
    for i in range(len(plate_list) + 1):
        # Invariant:
        # Variant:
        dp_matrix[i][0] = (True,{})

    for i in range(1, len(plate_list) + 1):
        # Invariant:
        # Variant:
        for j in range(1, weight + 1):
            # Invariant:
            # Variant:
            if plate_list[i - 1] > j:
                dp_matrix[i][j] = dp_matrix[i - 1][j]
            else:
                tempbol = dp_matrix[i - 1][j][0] or dp_matrix[i - 1][j - plate_list[i - 1]][0]
                if dp_matrix[i - 1][j][0]:
                    tempset = dp_matrix[i - 1][j][1]
                if dp_matrix[i - 1][j - plate_list[i - 1]][0]:
                    tempset = {plate_list[i - 1]}.union(dp_matrix[i - 1][j - plate_list[i - 1]][1])
                dp_matrix[i][j] = (tempbol,tempset)
    if dp_matrix[-1][-1][0] is None:
        return set({})
    return set(dp_matrix[-1][-1][1])



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