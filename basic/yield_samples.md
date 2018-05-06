

```python
def f():
    i = 0
    while True:
        i += 1
        print(i)
        yield

c = f()
next(c)
next(c)
print(c.send(5))
```


```python
def f(num):
    print("function start")
    for i in range(num):
        n = yield i
        print('generate %s finished' % n)
    print("function end")
    

print('test...')
g = f(3)
print(type(g))
print(dir(g))
print('next: %s' % next(g))
g.send('a')
# for i in g:
#     print(i)
```

    test...
    <class 'generator'>
    ['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']
    function start
    next: 0
    generate a finished





    1




```python
def consumer():
    while True:
        print('yield')
        n = yield 100
        print(n)
        if not n:
            break
        print('[CONSUMER]Consuming %s...' % n)

def producer(c):
    next(c)
    for n in range(1, 5):
        print('[PRODUCER]Producing %s...' % n)
        c.send(n)
    c.close()

c = consumer()
producer(c)
```


```python
from functools import wraps
def coroutine(fun):
    @wraps(fun)
    def primer(*args, **kwargs):
        gen = fun(*args, **kwargs)
        next(gen)
        return gen
    return primer
```


```python
@coroutine
def consumer():
    sum_ = 0
    while True:
        n = yield
        if not n:
            break
        sum_ = sum_ + n#<-
        print('[CONSUMER]Consuming %s...' % n)
#     return sum_#<-
```


```python
def producer(c):
    for n in range(1, 5):
        print('[PRODUCER]Producing %s...' % n)
        c.send(n)
    try:
        c.send(None)#<-
    except StopIteration as exc:
        print(dir(exc))
#         print("[PRODUCER]Producing GET",exc.value)
```

producer(consumer())


```python





```
