'''
SOLUTION-1
O(n+m) Time and O(n) Space
'''
def underscorifySubstring(string, substring):
    return get_modified(string, get_indices_of_target(string, substring))

'''
O(n) Time and O(n) Space
'''
def get_modified(string, indices):
    if len(indices) == 0: return string
    indices.reverse()
    result = ''
    start, end = indices.pop()
    for idx in range(len(string)):
        if idx == start and idx == end:
            result += '_' + string[idx] + '_'
            if len(indices) != 0:
                start, end = indices.pop()
            continue
        if idx == start:
            result += '_' + string[idx]
            continue
        if idx == end:
            result += string[idx] + '_'
            if len(indices) != 0:
                start, end = indices.pop()
            continue
        result += string[idx]
    return result

'''
O(n + m) Time and O(n) Space
'''
def get_indices_of_target(string, target):
    indices = list()
    for idx in range(len(string)):
        if string[idx] == target[0]:
            jdx = idx + 1
            matched = True
            for tidx in range(1, len(target)):
                if jdx >= len(string) or string[jdx] != target[tidx]:
                    matched = False
                    break
                jdx += 1
            if matched is True:
                indices.append(idx)
    return merge_overlapping(indices, target)
                
                
'''
O(n) Time and O(n) Space
'''
def merge_overlapping(indices, target):
    merged = list()
    idx = 0
    while idx < len(indices):
        if idx + 1 >= len(indices):
            merged.append((indices[idx], indices[idx]+len(target)-1))
            break
        
        if indices[idx+1] - indices[idx] <= len(target):
            start = indices[idx]
            while idx < len(indices)-1 and (indices[idx+1] - indices[idx] <= len(target)):
                end = indices[idx+1]
                idx += 1
            merged.append((start, end+len(target)-1))
            idx += 1
            continue
        
        else:
            merged.append((indices[idx], indices[idx]+len(target)-1))
            idx += 1
    return merged

'''
SOLUTION-2
O(n+m) Time and O(n) Space
'''
def underscorify_substring(string, substring):
    def get_locations():
        # store the locations of the substring in the given string
        locations = []
        start_idx = 0
        while start_idx < len(string):
            next_idx = string.find(substring, start_idx)
            if next_idx != -1:
                locations.append([next_idx, next_idx+len(substring)])
                start_idx = next_idx + 1
            else:
                break
        return locations

    def collapse(locations):
        if not len(locations):
            return locations
        new_locations = [locations[0]]
        previous      = new_locations[0]
        for idx in range(1, len(locations)):
            current = locations[idx]
            if current[0] <= previous[1]:
                previous[1] = current[1]
            else:
                new_locations.append(current)
                previous = current
        return new_locations

    def underscorify(locations):
        locations_idx = 0
        string_idx = 0
        in_between_underscores = False

        result = []
        i = 0
        while string_idx < len(string) and locations_idx < len(locations):
            if string_idx == locations[locations_idx][i]:
                result.append("_")
                in_between_underscores = not in_between_underscores

                if not in_between_underscores:
                    locations_idx += 1

                i = 0 if i == 1 else 1

            result.append(string[string_idx])
            string_idx += 1

        if locations_idx < len(locations):
            result.append("_")

        elif string_idx < len(string):
            result.append(string[string_idx:])

        return "".join(result)


            
            
    locations = collapse(get_locations())
    return underscorify(locations)

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            underscorifySubstring("testthis is a testtest to see if testestest it works", "test"),
            "_test_this is a _testtest_ to see if _testestest_ it works",
        )
        print("Test Case: Passed")


if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa
