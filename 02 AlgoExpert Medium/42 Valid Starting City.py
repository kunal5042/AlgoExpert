# https://www.algoexpert.io/questions/valid-starting-city
# Greedy Algorithms

def validStartingCity(distances, fuel, mpg):
	cities = len(distances)
	miles = 0
	result = {"Valid City": 0, "Miles Remaining": 0}
	current = {"Distance from previous city": 0, "Fuel refilled at previous city": 0}
	
	for city in range(1, cities):
		current["Distance from previous city"] = distances[city - 1]
		current["Fuel refilled at previous city"] = fuel[city - 1]
		miles += current["Fuel refilled at previous city"] * mpg - current["Distance from previous city"]

        # Logic: The city that we reach with the least amount of gas is our valid city
        # Why this works?
        # We know that there exist one city from which we can go to all the cities without running out of fuel
        # So, the idea is that, the city at which we come with least amount of fuel is the hardest to reach from other cities
        # or we should start with this city so that we don't have to come to this city from other cities
        # And with minimum gas, we can travel minimum number of miles
        # hence this condition
		if miles < result["Miles Remaining"]:
			result["Valid City"], result["Miles Remaining"] = city, miles
	
	return result["Valid City"]




import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        distances = [5, 25, 15, 10, 15]
        fuel = [1, 2, 1, 0, 3]
        mpg = 10
        expected = 4
        actual = validStartingCity(distances, fuel, mpg)
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