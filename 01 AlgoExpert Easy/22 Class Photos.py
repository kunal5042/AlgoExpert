import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        try:
            redShirtHeights = [5, 8, 1, 3, 4]
            blueShirtHeights = [6, 9, 2, 4, 5]
            expected = True
            actual = classPhotos(redShirtHeights, blueShirtHeights)
            self.assertEqual(actual, expected)
            print("Test Passed")
        except:
            print("Test Failed")
        
def classPhotos(redShirtHeights, blueShirtHeights):
    red = redShirtHeights
    blue = blueShirtHeights
    return class_photo_possible(red, blue)
        
def class_photo_possible(red, blue):
	red.sort()
	blue.sort()
	
	if sum(red) > sum(blue):
		for idx in range(len(red)):
			if red[idx] < blue[idx] or red[idx] == blue[idx]:
				return False
	else:
		for idx in range(len(blue)):
			if blue[idx] < red[idx] or blue[idx] == red[idx]:
				return False
	
	return True

if __name__ == "__main__":
    tester = TestProgram()
    tester.test_case_1()
    
# Kunal Wadhwa
