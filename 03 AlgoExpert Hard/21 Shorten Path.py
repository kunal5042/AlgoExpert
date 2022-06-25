class Stack:
    def __init__(self):
        self.stack = list()

    def pop(self):
        if self.empty() is False:
            return self.stack.pop()

    def push(self, val):
        self.stack.append(val)

    def empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def __str__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)

    def top(self):
        if self.empty() is False:
            return self.stack[-1]

    def return_as_list(self):
        return self.stack
    
def shortenPath(path):
    stack = Stack()
    absolute = False
    
    if path[0] == '/': absolute = True
    
    directories = path.split('/')

    for dir in directories:
        if dir == '.' or dir == '':
            continue
            
        elif dir == '..':
            if stack.empty() and not absolute:
                stack.push(dir)
            elif absolute or stack.top() != '..':
                stack.pop()
            else:
                stack.push(dir)

        else:
            stack.push(dir)

    result = '/'.join(stack.return_as_list())

    if absolute is True: return '/' + result
    return result


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        expected = "/foo/bar/baz"
        output = shortenPath("/foo/../test/../test/../foo//bar/./baz")
        self.assertEqual(output, expected)
        print("Test Case: Passed")
        
        
if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa