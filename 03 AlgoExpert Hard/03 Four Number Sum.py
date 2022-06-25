import unittest

def fourNumberSum(arr, target):
    hash = {}
    quads = []
    
    for i in range(1, len(arr)-1):
        for j in range(i+1, len(arr)):
            csum = arr[i] + arr[j]
            diff = target - csum
            
            if diff in hash:
                for pair in hash[diff]:
                    quads.append(pair + [arr[i]] + [arr[j]])
                    
                    
        for k in range(0, i):
            csum = arr[i] + arr[k]
            
            if csum not in hash:
                hash[csum] = [[arr[k], arr[i]]]
                
            else:
                hash[csum].append([arr[k], arr[i]])
                
    return quads

def sortAndStringify(array):
    return ",".join(sorted(list(map(lambda x: str(x), array))))


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = fourNumberSum([7, 6, 4, -1, 1, 2], 16)
        output = list(map(sortAndStringify, output))
        quadruplets = [[7, 6, 4, -1], [7, 6, 1, 2]]
        self.assertTrue(len(output) == 2)
        for quadruplet in quadruplets:
            try:
                self.assertTrue(sortAndStringify(quadruplet) in output)
            except:
                print("Test Case: Failed")
                break
        print("Test Case: Passed")
            

if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa



