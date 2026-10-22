def add(a, b):
    return a + b
assert add(10, 5) == 15

def multiply(a, b):
    return a * b
assert multiply(2, 10) == 20

def subtract(a, b):
    return a - b
assert subtract(10 , 5) == 5

def divide(a, b):
    return a / b
assert divide(20, 2) == 10
print("All test passed!")

import unittest 

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b 

def divide(a, b):
    return a / b

def subtract(a, b):
    return a - b

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
    
    def test_multiply(self):
        self.assertEqual(multiply(10, 2), 20)
    
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
    
    def test_subtract(self):
        self.assertEqual(subtract(30, 10), 20)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)  

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(5, 10), -5)
        
if __name__ == "__main__": 
    unittest.main()
