# https://www.algoexpert.io/questions/min-max-stack-construction
# Stack

class MinMaxStack:
  def __init__(self):
    self.min_max = []
    self.s = []

  def peek(self):
    if not self.is_empty():
      return self.s[len(self.s)-1]

  def is_empty(self):
    return len(self.s) == 0

  def pop(self):
    if not self.is_empty():
      self.min_max.pop()
      return self.s.pop()

  def push(self, data):
    c_min_max = {"min": data, "max": data}
    if len(self.min_max):
      p_min_max = self.min_max[len(self.min_max)-1]
      c_min_max["min"] = min(p_min_max["min"], data)
      c_min_max["max"] = max(p_min_max["max"], data)
    self.min_max.append(c_min_max)
    self.s.append(data)

  def getMin(self):
    return self.min_max[len(self.min_max)-1]["min"]

  def getMax(self):
    return self.min_max[len(self.min_max)-1]["max"]


import unittest
def testMinMaxPeek(self, min, max, peek, stack):
    self.assertEqual(stack.getMin(), min)
    self.assertEqual(stack.getMax(), max)
    self.assertEqual(stack.peek(), peek)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stack = MinMaxStack()
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(7)
        testMinMaxPeek(self, 5, 7, 7, stack)
        stack.push(2)
        testMinMaxPeek(self, 2, 7, 2, stack)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 7)
        testMinMaxPeek(self, 5, 5, 5, stack)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''