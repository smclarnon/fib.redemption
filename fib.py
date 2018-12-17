from unittest import TestCase


# a pythonic solution
def fib_py(n):
    x, y = 0, 1
    for i in range(n - 1):
        x, y = y, x + y
    return y


# classic recursive solution
def fib_classic(n):
    if n in [1, 2]:
        return 1
    return fib_classic(n - 1) + fib_classic(n - 2)


# recursive with memoization
def fib_recursive_with_memo(n):
    memo = [None] * (n + 1)

    def _fib(x):
        if memo[x]:
            return memo[x]
        elif x in [1, 2]:
            result = 1
        else:
            result = _fib(x - 1) + _fib(x - 2)
        memo[x] = result
        return result

    return _fib(n)


# bottom up approach
def fib_bottom_up(n):
    memo = [None] * (n + 1)
    for i in range(1, n + 1):
        if i in [1, 2]:
            memo[i] = 1
        else:
            memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]


class FibTest(TestCase):

    def test_fib_py(self):
        self.assertEqual(2, fib_py(3))
        self.assertEqual(5, fib_py(5))
        self.assertEqual(8, fib_py(6))
        self.assertEqual(280571172992510140037611932413038677189525, fib_py(200))

    def test_classic(self):
        self.assertEqual(2, fib_classic(3))
        self.assertEqual(5, fib_classic(5))
        self.assertEqual(8, fib_classic(6))
        # too slow
        # self.assertEqual(280571172992510140037611932413038677189525, fib_classic(200))

    def test_memo(self):
        self.assertEqual(2, fib_recursive_with_memo(3))
        self.assertEqual(5, fib_recursive_with_memo(5))
        self.assertEqual(8, fib_recursive_with_memo(6))
        self.assertEqual(280571172992510140037611932413038677189525, fib_recursive_with_memo(200))

    def test_should_do_something(self):
        self.assertEqual(2, fib_bottom_up(3))
        self.assertEqual(5, fib_bottom_up(5))
        self.assertEqual(8, fib_bottom_up(6))
        self.assertEqual(280571172992510140037611932413038677189525, fib_bottom_up(200))
