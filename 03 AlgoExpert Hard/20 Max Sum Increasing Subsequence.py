'''
O(n^2) Time and O(n) Space: where n is the length of the input array
'''
def maxSumIncreasingSubsequence(array):
    # At every cell/index/position in this dp array
    # it will store the maximum sum of increasing subsequence that ends at this index
    # where index lies in range(0, len(array))
    dp = [array[idx] for idx in range(len(array))]

    # Every index position of this array will store index of the previous element which was used to build this maximum sum increasing subsequence
    indices = [None for _ in range(len(array))]

    # initialize max sum = 0 and ending index of this sequence = 0
    result_sum = array[0]
    # result sum stores the ending index of our maximum sum increasing subsequence
    result_idx = 0


    for idx in range(1, len(array)):
        # every element in itself is a subsequence
        current_max_sum = array[idx]

        # used to keep track of which previous element are we using to build this increasing subsequence
        previous_subsequence_ending_index = idx
        
        for jdx in range(0, idx):
            # if we find a previous element which is smaller than current element
            # we can use this element to increase the length/ build further our increasing subsequence
            if array[jdx] < array[idx]:

                # if the sum of previous increasing subsequence + our current element i.e total sum of this potential increasing subsequence
                # is greater than maximum sum of increasing subsequence that we can build with current element
                if dp[jdx] + array[idx] >= current_max_sum:
                    # update maximum sum we can build with an increasing subsequence that ends with element
                    current_max_sum = dp[jdx] + array[idx]
                    # index of the previous element that we used
                    previous_subsequence_ending_index = jdx

        # update the result
        dp[idx] = current_max_sum

        # keep track of result, so that we dont' have to do another traversal at the end
        if current_max_sum > result_sum:
            result_sum = current_max_sum
            result_idx = idx

        # if we didn't use any previous element in building this increasing subsequence
        # then we have to leave previous index as None, coz this will be our base case in building the resultant subsequence
        if previous_subsequence_ending_index != idx:
            indices[idx] = previous_subsequence_ending_index

    # initialize the resultant subsequence
    resultant_subsequence = list()

    # build it
    max_seq_idx = result_idx
    while max_seq_idx is not None:
        resultant_subsequence.append(array[max_seq_idx])
        max_seq_idx = indices[max_seq_idx]

    # because we built it from last, we have to reverse it
    resultant_subsequence.reverse()

    return [result_sum, resultant_subsequence]


# Kunal Wadhwa