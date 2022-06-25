def longestPeak(array):
	return longest_peak(array)

def longest_peak(array):
	result = 0
	if len(array) < 3:
		return result
	
	idx = 1
	while idx < len(array) - 1:
		# conditions for peak
		previous_is_smaller = array[idx-1] < array[idx]
		next_is_smaller = array[idx] > array[idx+1]
		
		# if both conditions are true, find peak's length
		if previous_is_smaller and next_is_smaller:
			# if both conditions hold true, min peak = 3
			peak = 3
			
			# count the number of elements following the peak criteria to the left
			idx_left = idx - 2
			while idx_left >= 0 and array[idx_left] < array[idx_left + 1]:
				peak += 1; idx_left -= 1
			
			# count the number of elements following the peak criteria to the right and update the peak length accordingly
			idx_right = idx + 2
			while idx_right < len(array) and array[idx_right] < array[idx_right - 1]:
				peak += 1; idx_right += 1
			
			# upate the result, that is maximum of previous largest peak and current peak
			result = max(result, peak)
			
			# we can check for the next max peak from the right of the current peak so
			idx = idx_right
		
		# if peak conditions are not satisfied, increment the index and check for next element
		else:
			idx += 1
	
	return result

# Kunal Wadhwa
