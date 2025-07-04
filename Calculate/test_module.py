import unittest
from mean_var_std import calculate

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = calculate([0,1,2,3,4,5,6,7,8])
        expected = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666]*3, 6.666666666666667],
            'standard deviation': [[2.449489742783178]*3, [0.816496580927726]*3, 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
            }

        self.assertAlmostEqual(actual['mean'][0][0], expected['mean'][0][0], places=2)
        self.assertAlmostEqual(actual['variance'][2], expected['variance'][2], places=2)
        self.assertEqual(actual['max'][2], expected['max'][2])
        self.assertEqual(actual['min'][1], expected['min'][1])
        self.assertEqual(actual['sum'][0], expected['sum'][0])

    def test_calculate_raises_error(self):
        with self.assertRaises(ValueError):
            calculate([1, 2, 3])

if __name__ == "__main__":
    unittest.main()
