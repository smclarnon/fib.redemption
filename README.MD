## Fibonacci Many Ways

Because this is imporant. 

### classic recursive solution
```python
def fib_classic(n, _):
    if n in [1, 2]:
        return 1
    return fib_classic(n - 1) + fib_classic(n - 2)
```

### recursive with memoization
```python
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
def fib_bottom_up(n, memo):
    for i in range(1, n + 1):
        if i in [1, 2]:
            memo[i] = 1
        else:
            memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]
```

