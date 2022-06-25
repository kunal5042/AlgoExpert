'''
O(n) Time | O(n) Space: where n is the length of the input string
'''
def reverseWordsInString(string):
    # Write your code here.
	stack = []
	result = ''
	
	idx = 0
	while idx < len(string):
		# find a blankspace and push it to the stack
		if string[idx] == ' ':
			start = idx
			while idx < len(string) and string[idx] == ' ':
				idx += 1
			stack.append(string[start:idx])
			
		# find a word and push it to the stack
		else:
			start = idx
			while idx < len(string) and string[idx] != ' ':
				idx += 1
			stack.append(string[start: idx])
			

	while len(stack) != 0:
		# pop the string from the stack and concatenate it to the result
		# thereby reversing the words and the blankspaces
		result += stack.pop()
		
	return result

# Kunal Wadhwa
