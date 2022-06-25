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

# Kunal Wadhwa
