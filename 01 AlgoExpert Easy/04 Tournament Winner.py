'''
O(n) Time | O(k) Space: where n is the number of competitions and k is the number of teams
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

# Kunal Wadhwa
