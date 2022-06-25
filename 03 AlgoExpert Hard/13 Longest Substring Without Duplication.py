import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(longestSubstringWithoutDuplication("clementisacap"), "mentisac")
        print("Test Case: Passed")

def longestSubstringWithoutDuplication(string):
    # base case
    if len(string) == 0:
        return ''

    # base case
    if len(string) == 1:
        return string[0]
        
    start_index = 0
    visited_at  = {}
    max_len     = 0
    result      = []
    for idx, char in enumerate(string):
        # this condition only runs when we find a new duplicate element which belong to the current sub string
        # what if we don't find a duplicate in the current sub string? we will not be able to add this sub string in the result
        # we will call this condition EC-1
        if char in visited_at and visited_at[char] >= start_index:
            # remove the left-most duplicate to make this substring valid again
            cur_len = idx - start_index
            if cur_len > max_len:
                max_len = cur_len
                result.append((start_index, idx))

            # update the new sub string's start index
            start_index = visited_at[char] + 1

            # update the duplicate char's new index
            visited_at[char] = idx
            
        else:
            # mark the current character as visited
            visited_at[char] = idx

    # to handle the EC-1 condition
    if idx - start_index + 1> max_len:
        return string[start_index:idx+1]

    if len(result) > 0:
        start, end = result.pop()
        return string[start:end]
    else:
        # this might be possible that we never found a duplicate element, and hence our result stack is empty
        # in that case we return the string itself
        return string
    
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa