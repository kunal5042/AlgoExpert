# https://www.algoexpert.io/questions/valid-ip-addresses
# Strings

'''
O(1) Time | O(1) Space
'''
def validIPAddresses(string):
	result = []
	
	for idx in range(1, min(len(string), 4)):
		# parts for current ip address
		current = ['', '', '', '']
		
		current[0] = string[:idx]
		if not valid(current[0]):
			continue
			
		for jdx in range(idx + 1, idx + min(len(string) - idx, 4)):
			current[1] = string[idx:jdx]
			if not valid(current[1]):
				continue
			
			for kdx in range(jdx + 1, jdx + min(len(string) - jdx, 4)):
				current[2] = string[jdx:kdx]
				current[3] = string[kdx:]
				
				if valid(current[2]) and valid(current[3]):
					result.append('.'.join(current))
					
	return result

def valid(part):
	number = int(part)
	if number > 255 or len(str(number)) != len(part):
		return False
	
	return True



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "1921680"
        expected = [
            "1.9.216.80",
            "1.92.16.80",
            "1.92.168.0",
            "19.2.16.80",
            "19.2.168.0",
            "19.21.6.80",
            "19.21.68.0",
            "19.216.8.0",
            "192.1.6.80",
            "192.1.68.0",
            "192.16.8.0",
        ]
        actual = validIPAddresses(input)
        self.assertEqual(actual, expected)
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