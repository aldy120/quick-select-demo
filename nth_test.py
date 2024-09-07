import unittest
import nth

class NthTest(unittest.TestCase):
    def test_find_half_from(self):
        result = nth.find_half_from(3)
        self.assertEqual(result, (1,1))
        result = nth.find_half_from(4)
        self.assertEqual(result, (1,2))
    def test_slow_select(self):
        result = nth.slow_select(2, [1,4,2,5,3])
        self.assertEqual(result, 3)
        result = nth.slow_select(0, [1,4,2,5,3])
        self.assertEqual(result, 1)
        result = nth.slow_select(4, [1,4,2,5,3])
        self.assertEqual(result, 5)
    def test_quick_select(self):
        result = nth.quick_select(2, [1,4,2,5,3])
        self.assertEqual(result, 3)
        result = nth.quick_select(0, [1,4,2,5,3])
        self.assertEqual(result, 1)
        result = nth.quick_select(4, [1,4,2,5,3])
        self.assertEqual(result, 5)
        result = nth.quick_select(4, [1,4,2,5,3], nth.median_of_medians)
        self.assertEqual(result, 5)
        
    def test_slow_find_medium(self):
        result = nth.slow_find_median([1,4,2,5,3])
        self.assertEqual(result, 3)
        result = nth.slow_find_median([5,4,3,2,1])
        self.assertEqual(result, 3)
        result = nth.slow_find_median([1,2,3,4,5])
        self.assertEqual(result, 3)
    def test_trivial_pick_pivot(self):
        result = nth.trivial_pick_pivot([1,2,3])
        self.assertEqual(result, 1)
    def test_median_of_medians(self):
        result = nth.median_of_medians([1,2,3])
        self.assertEqual(result, 2)
        result = nth.median_of_medians([3,1,2,5,4])
        self.assertEqual(result, 3)
        result = nth.median_of_medians([1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(result, 5.5)
        result = nth.median_of_medians([1,2,3,4,5,6,7,8,9,10,1,2])
        self.assertEqual(result, 5.5)
        result = nth.median_of_medians([3,1,2,4,5,7,8,9,10,6,1,2])
        self.assertEqual(result, 5.5)
    def test_chunked(self):
        result = nth.chunked([1,2,3,4,5,6,7,8,9,10], 5)
        self.assertEqual(result, [[1,2,3,4,5],[6,7,8,9,10]])
    def test_quick_find_median(self):
        result = nth.quick_find_median([1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(result, 5.5)
        result = nth.quick_find_median([1,4,5,7,8,9,10,2,11,3,6])
        self.assertEqual(result, 6)
        arr = [35,5,14,49,49,90,60,22,47,86,34,94,14,96,20,17,48,20,62,33,20,55,70,29,49,84,43,97,25,2,28,14,38,81,16,27,10,15,17,49,49,71,39,71,62,84,58,9,21,69]
        result = nth.quick_find_median(arr)
        self.assertEqual(result, 41)
        result = nth.quick_find_median(arr[1:])
        self.assertEqual(result, 43)
        result = nth.quick_find_median(arr[2:])
        self.assertEqual(result, 45)
        result = nth.quick_find_median(arr[3:])
        self.assertEqual(result, 47)
if __name__ == '__main__':
    unittest.main()