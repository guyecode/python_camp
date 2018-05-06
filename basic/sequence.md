
## 序列： 列表、元组、range

### range:

python3中range函数返回一个range对象，python2则返回一个list对象


```python
r = range(10)
type(r)
```




    range




```python
1 in r
```




    True




```python
r[5:]
```




    range(5, 10)




```python
r[5:] == range(5, 10)
```




    True




```python
list(range(0, 10, 2))
```




    [0, 2, 4, 6, 8]




```python
list(range(0, -10, -1))
```




    [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]



range对象可以转为list对象


```python
lst = list(r)
print(lst)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


###  list

list/tuple支持以下操作


```python
1 in lst
```




    True




```python
0 not in lst
```




    False




```python
letters = ['a', 'b', 'c', 'd', 'e']
lst + letters
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']




```python
[[]] * 3
```




    [[], [], []]




```python
letters[0:2]
```




    ['a', 'b']




```python
lst[::2]
```




    [0, 2, 4, 6, 8]




```python
lst[::-1]
```




    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]




```python
lst[-1] = 99
lst[0:5] = letters
print(lst)
lst[0:3] = [] # 相当于del lst[0:3]
print(lst)
```

    ['a', 'b', 'c', 'd', 'e', 5, 6, 7, 8, 99]
    ['d', 'e', 5, 6, 7, 8, 99]



```python
lst = list(range(10))
lst[::2] = ['a', 'b', 'c', 'd', 'e']
print(lst)
```

    ['a', 1, 'b', 3, 'c', 5, 'd', 7, 'e', 9]



```python
del lst[::2]
print(lst)
```

    [1, 3, 5, 7, 9]



```python
letters * 2
```




    ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']




```python
letters *= 2
print(letters)
```

    ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']



```python
print(len(lst), min(lst), max(lst))
```

    5 1 9


index方法可以检测对象在list中出现的位置


```python
letters.index('a')
```




    0




```python
letters2 = letters * 2
(letters * 2).index('a', 3, -1)
```




    5



count方法对象在列表中出现的次数


```python
letters2.count('a')
```




    4



复制list的几种方法


```python
lst1 = lst.copy()
lst2 = lst[:]
lst3 = list(lst)
print(lst1, lst2, lst3)
print(id(lst1), id(lst2), id(lst3))
```

    [1, 3, 5, 7, 9] [1, 3, 5, 7, 9] [1, 3, 5, 7, 9]
    4342743752 4339182024 4342746888



```python
letters = ['a', 'b', 'c', 'd', 'e']
letters.append('h')
print(letters)
```

    ['a', 'b', 'c', 'd', 'e', 'h']



```python
last = letters.pop()
print(last)
print(letters)
```

    h
    ['a', 'b', 'c', 'd', 'e']



```python
letters.insert(1, 'b')
print(letters)
```

    ['a', 'b', 'b', 'c', 'd', 'e']



```python
letters[1:1] = ['b']
print(letters)
```

    ['a', 'b', 'b', 'b', 'c', 'd', 'e']



```python
letters.remove('b')
print(letters)
```

    ['a', 'b', 'b', 'c', 'd', 'e']



```python
letters.reverse()
print(letters)
```

    ['e', 'd', 'c', 'b', 'b', 'a']


list的排序


```python
letters.sort()
print(letters)
```

    ['a', 'b', 'b', 'c', 'd', 'e']


倒序排序


```python
letters.sort(reverse=True)
print(letters)
```

    ['e', 'd', 'c', 'b', 'b', 'a']


按指定的键排序


```python
lst = [('a', 1), ('b', 3), ('c', 2)]
lst.sort(key=lambda x:x[1], reverse=True)
print(lst)
```

    [('b', 3), ('c', 2), ('a', 1)]

清空list的办法


```python
letters.clear()
del lst[:]
print(letters, lst)
```

    [] []

