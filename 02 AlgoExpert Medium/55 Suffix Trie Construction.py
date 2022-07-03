# https://www.algoexpert.io/questions/suffix-trie-construction
# Tries

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for idx in range(len(string)):
            # insert all the substrings
            self.insert_substring_starting_at(idx, string)

    def insert_substring_starting_at(self, idx, string):
        current_node = self.root
        for jdx in range(idx, len(string)):
            # current letter to insert in the suffix tree
            character = string[jdx]
            # if the current character of the substring is present in the Hash Map of root
            # we point to it
            # else, we create a new Hash Map for this node and point to the newly created hash map
            if character not in current_node:
                current_node[character] = {}
                
            # Hash Map for current character exists now, so point to it
            current_node = current_node[character]

        # once the entire substring has been inserted
        # we add an end symbol to it
        current_node[self.endSymbol] = True
            

    def contains(self, string):
        # to check if a string is present in our suffix tree
        current_node = self.root
        for character in string:
            # if any of the characters is not present in our suffix tree, return False
            # otherwise, moving to the next node and checking
            if character not in current_node:
                return False
            current_node = current_node[character]

        # to check if the entire string is present in our suffix tree
        # we have to check if the current_node has endSymbol or not
        return self.endSymbol in current_node



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trie = SuffixTrie("babc")
        expected = {
            "c": {"*": True},
            "b": {"c": {"*": True}, "a": {"b": {"c": {"*": True}}}},
            "a": {"b": {"c": {"*": True}}},
        }
        self.assertEqual(trie.root, expected)
        self.assertTrue(trie.contains("abc"))
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