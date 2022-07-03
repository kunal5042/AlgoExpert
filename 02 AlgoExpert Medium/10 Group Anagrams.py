# https://www.algoexpert.io/questions/group-anagrams
# Strings

'''O(w * n * log(n)) time | O(wn) space - where w is the number of words and n is the length of the longest word'''
def groupAnagrams(words):
	# words will be stored after arranging them in alphabetical order
	arranged = {}
	for word in words:
		key = "".join(sorted(word))
		if key in arranged:
			# This means this word belongs to sorted(word) group of anagram
			# So, we will add it to that group
			arranged[key].append(word)
		else:
			# This word is the founder of it's group of anagram
			arranged[key] = [word]
	
	return list(arranged.values())



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
        expected = [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
        output = list(map(lambda x: sorted(x), groupAnagrams(words)))

        self.compare(expected, output)

    def compare(self, expected, output):
        if len(expected) == 0:
            self.assertEqual(output, expected)
            return
        self.assertEqual(len(expected), len(output))
        for group in expected:
            self.assertTrue(sorted(group) in output)
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