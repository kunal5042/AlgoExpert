'''
O(n(log(n))) Time and O(1) Extra Space: where n is the length of the input array 
'''
def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    
    merged = intervals[0]
    result = []
    
    for idx in range(1, len(intervals)):
        current = intervals[idx]
        
        if merged[1] < current[0]:
            # not overlapping
            result.append(merged)
            merged = current
            
        else:
            # overlapping
            merged[0] = min(merged[0], current[0])
            merged[1] = max(merged[1], current[1])
            
        # no need to merge further 
        if idx == len(intervals) - 1:
            result.append(merged)
            
    return result

# Kunal Wadhwa
			 