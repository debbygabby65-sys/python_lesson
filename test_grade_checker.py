import unittest

from grade_checker import get_grade

class TestGradeChecker(unittest.TestCase):
    def test_negative_score(self):
        with self.assertRaises(ValueError):
            get_grade(-5)
        
    def test_score_above_100(self):
        with self.assertRaises(ValueError):
            get_grade(120)

    def test_score_of_101_raises_error(self):
        with self.assertRaises(ValueError):
            get_grade(101)

    def test_score_of_minus_1_raises_error(self):
        with self.assertRaises(ValueError):
            get_grade(-1)

    def test_f_grade_scores(self):
        for score in [0, 20, 44,]:
            with self.subTest(score=score):
                self.assertEqual(get_grade(score), "F")

    def test_score_of_69_returns_b(self):
        self.assertEqual(get_grade(69), "B")

    def test_score_of_70_returns_a(self):
        self.assertEqual(get_grade(70), "A")

    def test_score_of_71_returns_a(self):
        self.assertEqual(get_grade(71), "A")

    def test_score_of_59_returns_c(self):
        self.assertEqual(get_grade(59), "C") 

    def test_score_of_49_returns_d(self):
        self.assertEqual(get_grade(49), "D")

    def test_score_of_0_returns_f(self):
        self.assertEqual(get_grade(0), "F")   

    def test_score_of_100_returns_a(self):
        self.assertEqual(get_grade(100), "A")

    def test_score_of_44_returns_f(self):
        self.assertEqual(get_grade(44), "F")

    def test_score_of_45_returns_d(self):
        self.assertEqual(get_grade(45), "D")

    def test_grade_a(self):
        self.assertEqual(get_grade(85), "A")
    
    def test_grade_b(self):
        self.assertEqual(get_grade(65), "B")

    def test_grade_c(self):
        self.assertEqual(get_grade(55), "C")

    def test_grade_d(self):
        self.assertEqual(get_grade(47), "D")

    def test_grade_f(self):
        self.assertEqual(get_grade(30), "F")

if __name__ == "__main__":
    unittest.main()