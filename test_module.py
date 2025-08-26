import unittest
import mean_var_std as mvs

class TestMeanVarStd(unittest.TestCase):
    def test_calculate_correct(self):
        self.assertEqual(mvs.calculate([0,1,2,3,4,5,6,7,8]), {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.0],
            'standard deviation': [[2.449..., 2.449..., 2.449...], [0.816..., 0.816..., 0.816...], 2.449...],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        })

    def test_error(self):
        with self.assertRaises(ValueError):
            mvs.calculate([1,2,3])

if __name__ == "__main__":
    unittest.main()
