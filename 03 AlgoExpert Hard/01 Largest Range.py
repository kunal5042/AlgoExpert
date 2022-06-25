def largest_range(a):
	result = [-1, -1]
	hash   = {}
	largest = float('-inf')
	
	for ele in a:
		hash[ele] = True
	
	for ele in a:
		current = 1
		start   = ele
		end     = ele
		ele    += 1
		match   = True
		
		while match is True:
			if ele in hash:
				current += 1
				end      = ele
				ele     += 1
			else:
				match = False
		
		if current > largest:
			largest = current
			result  = [start, end]
	return result