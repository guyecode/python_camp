
## 字符串操作

### 定义字符串


```python
s1 = 'hello world'
print(s1)
```


```python
s2 = 'hello ' 'world'
print(s2)
```


```python
s3 = ('hello ' 'world')
print(s3)
```


```python
s1 == s2 and s2 == s3
```


```python
s = 'hello '
'world'
print(s)
```

### 格式化字符串


```python
a = 'hello '
b = 'world'
a + b
```


```python
''.join((a, b))
```


```python
'%s%s' % (a, b)
```


```python
'%s%s'.format(a, b)
```


```python
'{}{}'.format(a, b)
```




    'hello world'




```python
'{0}{1}'.format(a, b)
```




    'hello world'




```python
'%(a)s%(b)s' % ({'a': a, 'b': b})
```




    'hello world'




```python
'{a}{b}'.format_map({'a': a, 'b': b})
```




    'hello world'




```python
'{a}{b}'.format(a=a, b=b)
```




    'hello world'




```python
f'{a}{b}'
```




    'hello world'




```python
'a' * 10
```




    'aaaaaaaaaa'



### 字符串对象方法


```python
'aBc'.lower()
```




    'abc'




```python
'aBc'.upper()
```




    'ABC'




```python
'aBc'.swapcase()
```




    'AbC'




```python
'abc'.capitalize()
```




    'Abc'




```python
'china america japan'.title()
```




    'China America Japan'




```python
'abc'.center(7, '*')
```




    '**abc**'




```python
'abc'.ljust(7, '*')
```




    'abc****'




```python
'abc'.rjust(7, '*')
```




    '****abc'




```python
' abc '.strip()
```




    'abc'




```python
'**abc**'.lstrip('*')
```




    'abc**'




```python
'**abc**'.rstrip('*')
```




    '**abc'




```python
'1'.zfill(2)
```




    '01'




```python
'abc'.startswith('a')
```




    True




```python
'abc'.endswith('c')
```




    True




```python
'abc'.islower()
```




    True




```python
'abc'.isupper()
```




    False




```python
'abc'.isalpha()
```




    True




```python
'123'.isdigit()
```




    True




```python
'一二三'.isdigit()
```




    False




```python
'一二三'.isnumeric()
```




    True




```python
'一二三123'.isnumeric()
```




    True




```python
'abc123'.isalnum()
```




    True




```python
'abc一二三123'.isalnum()
```




    True




```python
'1,2,3'.split(',')
```




    ['1', '2', '3']




```python
'1,2,3'.split(',', maxsplit=1)
```




    ['1', '2,3']




```python
'logo.png'.partition('.')
```




    ('logo', '.', 'png')




```python
love_letter = ll = 'i am missing you'
ll.replace('i', 'I')
```




    'I am mIssIng you'




```python
ll.replace('i', 'I', 1)
```




    'I am missing you'




```python
ll.find('i')
```




    0




```python
ll.rfind('i')
```




    9




```python
ll.index('i')
# 如果不存在则会报错
```




    0



### 字符串序列化操作


```python
for i in 'abc':
    print(i, end='')
```

    abc


```python
'abcd'[::2]
```




    'ac'



字符串是只读的，不支持修改


```python
s = 'abc'
#s[2] = 2
```

#### 反转字符串


```python
s = 'abc'
s[::-1]
```




    'cba'




```python
def rev1(s):
    l = list(s)
    l.reverse()
    return ''.join(l)
rev1(s)
```




    'cba'




```python
def rev2(s):
    l = list(s)
    for i in range(len(l) // 2):
        l[i], l[-(i+1)] = l[-(i+1)], l[i]
    return ''.join(l)
rev2(s)
```




    'cba'




```python
def rev3(s):
    return ''.join(s[i-1] for i in range(len(s), 0, -1))
rev3(s)
```




    'cba'




```python
def rev4(s):
    l = list(s)
    rs = ''
    while l:
        rs += l.pop()
    return rs
rev4(s)
```




    'cba'




```python
def rev5(s):
    if len(s) == 1:
        return s
    head, *tail = s
    return ''.join(rev5(tail)) + head
rev5(s)
```




    'cba'


