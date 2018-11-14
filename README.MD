## Fibonacci All The Ways

Because this is imporant. 

### classic recursive solution
```python
# just the plain old recursive fibonacci. should not take you 20 minutes
# in a coding interview
def fib_classic(n, _):
    if n in [1, 2]:
        return 1
    return fib_classic(n - 1) + fib_classic(n - 2)
```

### recursive with memoization
```python
# spice it up using memoization
# memo: dict of n->fib(n)
def fib_recursive_with_memo(n, memo):
    if memo[n]:
        return memo[n]
    if n in [1, 2]:
        result = 1
    else:
        result = fib_recursive_with_memo(n - 1, memo) + fib_recursive_with_memo(n - 2, memo)
    memo[n] = result
    return result
```


### bottom up approach
```python
# and now for the dynamic programming junkies, build the fib sequence
# from the botton up 
def fib_bottom_up(n, memo):
    for i in range(1, n + 1):
        if i in [1, 2]:
            memo[i] = 1
        else:
            memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]
```

