'''
O(n) Time and O(n) Space: where n is the length of the input array
'''
def nextGreaterElement(array):
    result = [-1 for x in array]
    stack = []

    for idx in range(2 * len(array)):
        circular_idx = idx % len(array)

        while len(stack):
            top = array[stack[len(stack)-1]]
            ele = array[circular_idx]

            if ele > top:
                result[stack.pop()] = ele

            else:
                break

        stack.append(circular_idx)

    return result

# Kunal Wadhwa
