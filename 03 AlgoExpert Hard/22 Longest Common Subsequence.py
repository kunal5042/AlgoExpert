# O(nm * min(n, m)) Time and Space: where n and m are the length of the two strings
def longestCommonSubsequence(str1, str2):
    dp = [['' for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

    for idx in range(len(str2)):
        for jdx in range(len(str1)):
            if str2[idx] == str1[jdx]:
                dp[idx+1][jdx+1] = dp[idx][jdx] + str2[idx]
            else:
                dp[idx+1][jdx+1] = max(dp[idx][jdx+1], dp[idx+1][jdx], key=len)
                
    return list(dp[-1][-1])

# O(nm) Time and Space
class LCS:
    def __init__(self):
        # because in the beginning string is empty
        self.len = 0
        self.ending_with = None
        self.prev_lcs_row = None
        self.prev_lcs_col = None

    def __len__(self):
        return self.len
        
def longest_common_subsequence(str1, str2):
    dp = [[LCS() for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

    for idx in range(1, len(str2)+1):
        for jdx in range(1, len(str1)+1):
            if str2[idx-1] == str1[jdx-1]:
                this_lcs = dp[idx][jdx]
                
                this_lcs.ending_with  = str2[idx-1]
                this_lcs.len          = dp[idx-1][jdx-1].len + 1
                this_lcs.prev_lcs_row = idx-1
                this_lcs.prev_lcs_col = jdx-1
            else:
                if len(dp[idx-1][jdx]) >  len(dp[idx][jdx-1]):
                    dp[idx][jdx].len          = len(dp[idx-1][jdx])
                    dp[idx][jdx].prev_lcs_row = idx-1
                    dp[idx][jdx].prev_lcs_col = jdx
                else:
                    dp[idx][jdx].len          = len(dp[idx][jdx-1])
                    dp[idx][jdx].prev_lcs_row = idx
                    dp[idx][jdx].prev_lcs_col = jdx-1

    # build sequence
    sequence = []
    idx, jdx = len(dp)-1, len(dp[0])-1

    while idx != 0 and jdx !=0:
        this_lcs = dp[idx][jdx]
        if this_lcs.ending_with is not None:
            sequence.append(this_lcs.ending_with)
        idx = this_lcs.prev_lcs_row
        jdx = this_lcs.prev_lcs_col

    sequence.reverse()

    return sequence

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = longestCommonSubsequence("ZXVVYZW", "XKYKZPW")
        self.assertEqual(output, ["X", "Y", "Z", "W"])
        print("Test Case: Passed")

if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa