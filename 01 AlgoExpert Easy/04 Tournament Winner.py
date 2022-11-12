# https://www.algoexpert.io/questions/tournament-winner
# Arrays

'''
	# Optimal = O(n) time | O(k) space
	# where n is the number of competitions and k is the number of teams
'''
def tournamentWinner(competitions, results):

	hash = {}
	best_team = ""
	best_score = 0
	
	for idx in range(len(results)):
		if results[idx] == 0:
			winner = competitions[idx][1]
			
			if winner in hash:
				hash[winner] = hash[winner] + 3
			else:
				hash[winner] = 3
			
			winner_score = hash[winner]
			if winner_score > best_score:
				best_score = winner_score
				best_team = winner
		
		elif results[idx] == 1:
			winner = competitions[idx][0]

			if winner in hash:
				hash[winner] = hash[winner] + 3
			else:
				hash[winner] = 3

			winner_score = hash[winner]
			if winner_score > best_score:
				best_score = winner_score
				best_team = winner
	
	return best_team



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = "Python"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(actual, expected)
        print("Test Case: Passed")

if __name__ == "__main__":
    test = TestProgram()
    test.test_case_1()
'''

# Kunal Wadhwa

'''