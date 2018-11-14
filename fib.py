from unittest import TestCase


# classic recursive solution
def fib_classic(n, _):
    if n in [1, 2]:
        return 1
    return fib_classic(n - 1) + fib_classic(n - 2)


# recursive with memoization
def fib_recursive_with_memo(n, memo):
    if memo[n]:
        return memo[n]
    if n in [1, 2]:
        result = 1
    else:
        result = fib_recursive_with_memo(n - 1, memo) + fib_recursive_with_memo(n - 2, memo)
    memo[n] = result
    return result


# bottom up approach
def fib_bottom_up(n, memo):
    for i in range(1, n + 1):
        if i in [1, 2]:
            memo[i] = 1
        else:
            memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]


def fib(n):
    memo = [None] * (n + 1)
    return fib_bottom_up(n, memo)


class FibTest(TestCase):

    def test_should_do_something(self):
        # self.assertEqual(2, fib(3))
        # self.assertEqual(5, fib(5))
        # self.assertEqual(8, fib(6))
        self.assertEqual(280571172992510140037611932413038677189525, fib(200))
