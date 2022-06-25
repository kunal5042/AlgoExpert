import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        try:
            print("Test Case : Passed")
            self.assertEqual(minRewards_E([8, 4, 2, 1, 3, 6, 7, 9, 5]), 25)
        except:
            print("Test Case : Failed")
        
        
# O(n^2) Solution
def minRewards(scores):
    output = [1 for _ in range(len(scores))]
    output[0] = 1

    for idx in range(1, len(scores)):
        if scores[idx-1] < scores[idx]:
            output[idx] = output[idx-1] + 1

        if scores[idx-1] > scores[idx]:
            start = idx - 1

            while start >= 0:
                if start != 0:
                    if output[start-1] < output[start]:
                        output[start] = max(output[start], output[start+1]+1)
                        break
                output[start] = max(output[start], output[start+1]+1)
                start -= 1

    return sum(output)


# O(n) Solution
def minRewards_E(scores):
    output = [1 for _ in range(len(scores))]

    for idx in range(1, len(scores)):
        if scores[idx] > scores[idx-1]:
            output[idx] = output[idx-1] + 1

    for idx in reversed(range(len(scores)-1)):
        if scores[idx] > scores[idx+1]:
            output[idx] = max(output[idx], output[idx+1]+1)


    return sum(output)


if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa
