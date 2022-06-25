from collections import Counter
def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []

    new_pattern = get_new_pattern(pattern)
    did_switch  = new_pattern[0] != pattern[0]
    count, first_y_pos = get_count_and_first_y_position(new_pattern)

    if count['y'] > 0:
        for lenx in range(1, len(string)):
            leny = (len(string) - lenx * count['x']) / count['y']
            if leny <= 0 or leny % 1 != 0:
                continue

            leny = int(leny)
            yidx = first_y_pos * lenx
            x    = string[:lenx]
            y    = string[yidx: yidx+leny]
            potential_match = list(map(lambda char:x if char == 'x' else y, new_pattern))
            print("".join(potential_match))
            if string == "".join(potential_match):
                return [x, y] if not did_switch else [y, x]
    else:
        lenx = len(string) / count['x']
        if lenx % 1 == 0:
            lenx = int(lenx)
            x = string[:lenx]
            potential_match = list(map(lambda char:x, new_pattern))
            print("".join(potential_match))
            if string == "".join(potential_match):
                return [x, ''] if not did_switch else ['', x]

    return []

def get_new_pattern(pattern):
    pattern_letters = list(pattern)
    if pattern[0] == 'x':
        return pattern_letters
    else:
        return list(map(lambda char: 'x' if char == 'y' else 'y', pattern_letters))

def get_count_and_first_y_position(pattern):
    count = Counter(pattern)
    first_y_pos = None
    for idx, char in enumerate(pattern):
        if char == 'y':
            first_y_pos = idx
            break
    return count, first_y_pos

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"), ["go", "powerranger"])
        print("Test Case: Passed")

if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()

# Kunal Wadhwa
