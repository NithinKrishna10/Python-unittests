import myfuction
import unittest

class TestMultiply(unittest.TestCase):

    def test_with_two_positive(self):

        self.assertEqual(myfuction.multiply_with_loop_imperfect(17,19),17*19)
        self.assertEqual(myfuction.multiply_with_loop_imperfect(20,29),20*29)
        self.assertEqual(myfuction.multiply_with_loop_imperfect(1000,299),1000*299)


    def test_with_one_zero(self):

        self.assertEqual(myfuction.multiply_with_loop_imperfect(17,0),17*0)
        self.assertEqual(myfuction.multiply_with_loop_imperfect(0,29),0*19)
        self.assertEqual(myfuction.multiply_with_loop_imperfect(0,9),0*9)

    def test_with_two_zero(self):

        self.assertEqual(myfuction.multiply_with_loop_imperfect(0,0),0)
     
    def test_with_one_negative(self):

        self.assertEqual(myfuction.multiply_with_loop_imperfect(17,(-12)),17*(-12))
        self.assertEqual(myfuction.multiply_with_loop_imperfect(42,(-200)),42*(-200))
        self.assertEqual(myfuction.multiply_with_loop_imperfect(50,(-675)),50*(-675))


class TestMultiplyBetter(unittest.TestCase):

    def test_with_two_positive(self):
        self.assertEqual(myfuction.multiply_with_loop_better(17, 19), 17 * 19)
        self.assertEqual(myfuction.multiply_with_loop_better(20, 29), 20 * 29)
        self.assertEqual(myfuction.multiply_with_loop_better(1000, 299), 1000 * 299)
    def test_with_one_zero(self):
        self.assertEqual(myfuction.multiply_with_loop_better(17, 0), 17 * 0)
        self.assertEqual(myfuction.multiply_with_loop_better(0, 29), 0 * 19)
        self.assertEqual(myfuction.multiply_with_loop_better(0, 9), 0 * 9)

    def test_with_two_zero(self):
        self.assertEqual(myfuction.multiply_with_loop_better(0, 0), 0)

    def test_with_one_negative(self):
        self.assertEqual(myfuction.multiply_with_loop_better(17, (-12)), 17 * (-12))
        self.assertEqual(myfuction.multiply_with_loop_better(42, (-200)), 42 * (-200))
        self.assertEqual(myfuction.multiply_with_loop_better(50, (-675)), 50 * (-675))
