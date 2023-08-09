import unittest
from area import *

class MyTestClass(unittest.TestCase):
    def test_circle(self):             
        # String Input
        self.assertRaises(ValueError, circle, 'd')
        # self.assertRaises(ValueError, f, 'd', 'd')
        # self.assertRaises(ValueError, f, 'd', 5)
        # self.assertRaises(ValueError, f, 5, 'd')


        # Negative Input
        self.assertRaises(TypeError, circle, -1)
        # self.assertRaises(TypeError, f, -1, -1)
        # self.assertRaises(TypeError, f, -1, +1)
        # self.assertRaises(TypeError, f, +1, -1)

        # Zero Input
        self.assertRaises(TypeError, circle, 0)
        # self.assertRaises(TypeError, f, 0, 0)
        # self.assertRaises(TypeError, f, 0, 5)
        # self.assertRaises(TypeError, f, 5, 0)

        # Positive Input
        self.assertAlmostEqual(circle(5), math.pi * 5**2)
        self.assertAlmostEqual(circle(5.5), math.pi * 5.5**2)
        # self.assertAlmostEqual(f(5.5, 5.5), math.pi * 5**2)
        # self.assertAlmostEqual(f(5.5, 5), math.pi * 5**2)
        # self.assertAlmostEqual(f(5, 5.5), math.pi * 5**2)
        # self.assertAlmostEqual(f(5, 5), math.pi * 5**2)

    def test_rectangle(self):        
        # String Input
        # self.assertRaises(ValueError, f, 'd')
        self.assertRaises(ValueError, rectangle, 'd', 'd')
        self.assertRaises(ValueError, rectangle, 'd', 5)
        self.assertRaises(ValueError, rectangle, 5, 'd')


        # Negative Input
        # self.assertRaises(TypeError, f, -1)
        self.assertRaises(TypeError, rectangle, -1, -1)
        self.assertRaises(TypeError, rectangle, -1, +1)
        self.assertRaises(TypeError, rectangle, +1, -1)

        # Zero Input
        # self.assertRaises(TypeError, f, 0)
        self.assertRaises(TypeError, rectangle, 0, 0)
        self.assertRaises(TypeError, rectangle, 0, 5)
        self.assertRaises(TypeError, rectangle, 5, 0)

        # Positive Input
        # self.assertAlmostEqual(f(5), math.pi * 5**2)
        # self.assertAlmostEqual(f(5.5), math.pi * 5.5**2)
        self.assertAlmostEqual(rectangle(5.5, 5.5), 5.5*5.5)
        self.assertAlmostEqual(rectangle(5.5, 5), 5.5*5)
        self.assertAlmostEqual(rectangle(5, 5.5), 5*5.5)
        self.assertAlmostEqual(rectangle(5, 5), 5*5)

    def test_triangle(self):
        # String Input
        # self.assertRaises(ValueError, f, 'd')
        self.assertRaises(ValueError, triangle, 'd', 'd')
        self.assertRaises(ValueError, triangle, 'd', 5)
        self.assertRaises(ValueError, triangle, 5, 'd')


        # Negative Input
        # self.assertRaises(TypeError, f, -1)
        self.assertRaises(TypeError, triangle, -1, -1)
        self.assertRaises(TypeError, triangle, -1, +1)
        self.assertRaises(TypeError, triangle, +1, -1)

        # Zero Input
        # self.assertRaises(TypeError, f, 0)
        self.assertRaises(TypeError, triangle, 0, 0)
        self.assertRaises(TypeError, triangle, 0, 5)
        self.assertRaises(TypeError, triangle, 5, 0)

        # Positive Input
        # self.assertAlmostEqual(f(5), math.pi * 5**2)
        # self.assertAlmostEqual(f(5.5), math.pi * 5.5**2)
        self.assertAlmostEqual(triangle(5.5, 5.5), 5.5*5.5/2)
        self.assertAlmostEqual(triangle(5.5, 5), 5.5*5/2)
        self.assertAlmostEqual(triangle(5, 5.5), 5*5.5/2)
        self.assertAlmostEqual(triangle(5, 5), 5*5/2)

    def test_square(self):      
        # String Input
        self.assertRaises(ValueError, square, 'd')
        # self.assertRaises(ValueError, f, 'd', 'd')
        # self.assertRaises(ValueError, f, 'd', 5)
        # self.assertRaises(ValueError, f, 5, 'd')


        # Negative Input
        self.assertRaises(TypeError, square, -1)
        # self.assertRaises(TypeError, f, -1, -1)
        # self.assertRaises(TypeError, f, -1, +1)
        # self.assertRaises(TypeError, f, +1, -1)

        # Zero Input
        self.assertRaises(TypeError, square, 0)
        # self.assertRaises(TypeError, f, 0, 0)
        # self.assertRaises(TypeError, f, 0, 5)
        # self.assertRaises(TypeError, f, 5, 0)

        # Positive Input
        self.assertAlmostEqual(square(5), 5*5)
        self.assertAlmostEqual(square(5.5), 5.5**2)
        # self.assertAlmostEqual(f(5.5, 5.5), math.pi * 5**2)
        # self.assertAlmostEqual(f(5.5, 5), math.pi * 5**2)
        # self.assertAlmostEqual(f(5, 5.5), math.pi * 5**2)
        # self.assertAlmostEqual(f(5, 5), math.pi * 5**2)

if __name__ == "__main__":

    MyTestClass().test_circle()
    MyTestClass().test_rectangle()
    MyTestClass().test_square()
    MyTestClass().test_triangle()