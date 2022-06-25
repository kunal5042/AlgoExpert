'''
O(n^2) Time | O(1) Space: Where n is the length of the input string
'''
def is_palindrome(left, right, string):
	while left >= 0 and right < len(string):
		if string[left] != string[right]:
			break
		left -= 1
		right += 1
	# when the above loop will end
	# the left and right indices will correspond to one left and one right of the palindrome
	# And, as string splicing excludes the upperbound index element, we don't change the right
	# But increment the left, as it's the start of the palindrome and we want to include it in our result
	return [left+1, right]
		
def longestPalindromicSubstring(string):
	# Algorithm
	# Treat every index as the centre of a potential palindrome
	# It could be an even or an odd plaindrome 
	# Move left and right accordingly and keep moving as long as the substring inside stays a palindrome
	longest_palindrome = [0, 1]
	
	for idx in range(1, len(string)):
		even = is_palindrome(idx-1, idx, string)
		odd = is_palindrome(idx-1, idx+1, string)
		# find the longest palindrome of the two
		current = max(even, odd, key = lambda indices: indices[1] - indices[0])
		
		# check if the current longest palindrome's length is greater than the longest plaindrome's length
		# update the longest_palindrome accordingly 
		longest_palindrome = max(longest_palindrome, current, key = lambda length: length[1] - length[0])
	
	# return the result
	return string[longest_palindrome[0]:longest_palindrome[1]]

# Kunal Wadhwa
