import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(levenshteinDistance("abc", "yabd"), 2)
        print("Test Case: Passed")

def levenshteinDistance(str1, str2):
    # 2 matrix set up
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]

    # initializing first column (base requirements)
    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i-1][0] + 1


    for r in range(1, len(str2) + 1):
        for c in range(1, len(str1) + 1):
            if str2[r - 1] == str1[c - 1]:
                edits[r][c] = edits[r - 1][c - 1]
            else:
                edits[r][c] = 1 + min(edits[r - 1][c], edits[r][c - 1], edits[r - 1][c - 1])

    return edits[-1][-1]


if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa
