import unittest
from answer import run

class TestAnswer(unittest.TestCase):
    def test_sample(self):
        output = ['Case #1: 1 0 0 0 0', 'Case #2: IMPOSSIBLE']
        self.assertEqual(run('inp/sample.inp'), output)

    def test_self_prepared_1(self):
        output = ['Case #1: IMPOSSIBLE']
        self.assertEqual(run('inp/case1.inp'), output)

    def test_self_prepared_2(self):
        output = ['Case #1: 0 0 1 1 0']
        self.assertEqual(run('inp/case2.inp'), output)

    def test_self_prepared_3(self):
        output = ['Case #1: 1 1 0', 'Case #2: 1 1 1 1']
        self.assertEqual(run('inp/case3.inp'), output)

    def test_self_prepared_4(self):
        output = ['Case #1: 0 1 0 1 0 0 1 0 0 0']
        self.assertEqual(run('inp/case4.inp'), output)

    def test_self_prepared_5(self):
        output = ['Case #1: IMPOSSIBLE']
        self.assertEqual(run('inp/case5.inp'), output)

if __name__ == '__main__':
    unittest.main()
