

```python
nums = set(range(2,20))
comps = {j for i in nums for j in range(i*i, 20, i)}
print(comps)
primes = nums - comps
print(primes)


def f(val, lst=[]):
    lst.append(val)
    return lst

print(f(1))
print(f(2, []))
print(f(3))
```

    {4, 6, 8, 9, 10, 12, 14, 15, 16, 18}
    {2, 3, 5, 7, 11, 13, 17, 19}
    [1]
    [2]
    [1, 3]



```python
def f(val, lst=[]):
    lst.append(val)
    return lst

print(f(1))
print(f(2, []))
print(f(3))
```

    [1]
    [2]
    [1, 3]

