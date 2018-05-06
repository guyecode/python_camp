
collections模块是Python内置模块，包含了几种扩展数据类型

### namedtuple
有时候我们需要定义一些简单的数据结构，只有几个属性，那我们可以不用定义一个类，直接用namedtuple就行了。


```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
print(p.x, p.y)
```




    2



上面的p对象虽然看起来像是一个类的实例，但它实际上也是个元组，支持所有的元组操作


```python
len(p)
```




    2




```python
x, y = p
print(x, y)
```

    1 2


namedtuple可以tuple、list等类型相互转换


```python
isinstance(p, tuple)
```




    True




```python
tuple(p)
```




    (1, 2)




```python
list(p)
```




    [1, 2]



namedtuple的优点在于比起直接写元组下标的写法更优雅，同时兼俱元组的可迭代特点


```python
iphones = (
    ('iPhone8', '32G', 60000 ),
    ('iPhone8', '128G', 7000),
    ('iPhoneX', '64G', 8000),
    ('iPhoneX', '256G', 10000),
    )
for phone in iphones:
    print(phone[0], phone[1], phone[2])
```

    iPhone8 32G 60000
    iPhone8 128G 7000
    iPhoneX 64G 8000
    iPhoneX 256G 10000


比较一下这种写法


```python
Phone = namedtuple('Phone', ['model', 'storage', 'price'])
iphones = (
    Phone('iPhone8', '32G', 60000 ),
    Phone('iPhone8', '128G', 7000),
    Phone('iPhoneX', '64G', 8000),
    Phone('iPhoneX', '256G', 10000),
    )
for phone in iphones:
    print(phone.model, phone.storage, phone.price)
```

    iPhone8 32G 60000
    iPhone8 128G 7000
    iPhoneX 64G 8000
    iPhoneX 256G 10000


namedtuple也可以作为字典的替代，它比字典更节省内存，但它不能像字典那可以修改


```python
iphone8 = Phone('iPhone8', '32G', 60000 )
iphone8.price = 1000
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-25-07a110896d9f> in <module>()
          1 iphone8 = Phone('iPhone8', '32G', 60000 )
    ----> 2 iphone8.price = 1000
    

    AttributeError: can't set attribute


如果实在想修改的话，可以用_replace方法。不过并不鼓励这样做，最好还是用字典来实现。


```python
iphone8._replace(price=1000)
```




    Phone(model='iPhone8', storage='32G', price=1000)



### deque

