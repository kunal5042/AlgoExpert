def phoneNumberMnemonics(phoneNumber):
    return phone_no_mnemonics(phoneNumber)

def phone_no_mnemonics(phone_number):
	result = []
	hash = {
		'1': '1',    '2': 'abc',   '3': 'def', 
		'4': 'ghi',  '5': 'jkl',   '6': 'mno',
		'7': 'pqrs', '8': 'tuv',   '9': 'wxyz',
					 '0': '0'
	}
	
	def helper(current, mnemonic):
		if len(current) == 0:
			result.append(mnemonic)
			return
		
		number = current[0]
		current = current[1:]
		
		combinations = hash[number]
		for next_num in combinations:
			helper(current, mnemonic + next_num)
	
	helper(phone_number, "")
	return result
		
# Kunal Wadhwa
			