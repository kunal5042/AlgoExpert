def array_of_products(array):
    # Algorithm
    # Array of products for an element at index i
    # is equal to the product of
    # product of all the elements to it's left
    # and product of all the elements to it's right

    left, right, result = [ele for ele in array], [ele for ele in array], [1] * len(array)
    N = len(array)

    # Fill the left product array
    for idx in range(1, N):
        left[idx] = left[idx - 1] * array[idx]

    # Fill the right product array
    for idx in reversed(range(0, N - 1)):
        right[idx] = right[idx + 1] * array[idx]

    # Fill the resultant array as result[i] = left[i-1] * right[i+1]
    for idx in range(N):
        if idx + 1 < N: result[idx] *= right[idx + 1]
        if idx - 1 >= 0: result[idx] *= left[idx - 1]

    # Return result
    return result

# Kunal Wadhwa
