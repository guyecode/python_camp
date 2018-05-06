
同时定义多个变量


```python
a, b = 1, 2
print(a, b)
```

    1 2


交换两个变量的值


```python
a, b = b, a
print(a, b)
```

    2 1



```python
a,b,c = 1,2,3
a,b,c = b,c,a
print(a,b,c)
```

    2 3 1


嵌套赋值


```python
name, city, birth = 'Agu', 'Beijing', (2017, 9, 21)
print('%s born at %s on %s' % (name, city, birth))
name, city, (year, month, day) = '阿古', '北京', (2017, 9, 21)
print('%s%s年%s月%s日出生在%s' % (name, year, month, day, city))
```

    Agu born at Beijing on (2017, 9, 21)
    阿古2017年9月21日出生在北京


同样规则也适用于tuple或者list


```python
lst = [1, 2]
a, b = lst
print(a, b)
a, b = tuple(lst)
print(a, b)
```

    1 2
    1 2


适用于任何可迭代的对象，比如迭代器、字符串、文件对象


```python
s = 'Agu'
a, b, c = s
print(a, b, c)
```

    A g u



```python
a, b, c = range(3)
print(a, b, c)
```

    0 1 2


如果可迭代对象的个数超过变量的个数，则会抛出ValueError


```python
name, city, birth = 'Agu', 'Beijing', 2017, 9, 21
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-50-d36585cede7c> in <module>()
    ----> 1 name, city, birth = 'Agu', 'Beijing', 2017, 9, 21
    

    ValueError: too many values to unpack (expected 3)


这个时候可以用*号来解决这种问题


```python
name, city, *birth = 'Agu', 'Beijing', 2017, 9, 21
print(name, city, birth)
```

    Agu Beijing [2017, 9, 21]


注意第3个带*号的参数，它永远都是List,即使没有值的情况下，省去了类型检查。


```python
name, city, *birth = 'Agu', 'Beijing'
print(name, city, birth)
```

    Agu Beijing []



```python
people = ['李白', '李清照']
for p in people:
    family_name, *name = p
    print('姓：%s  名：%s' % (family_name, ''.join(name)))
```

    姓：李  名：白
    姓：李  名：清照



```python
*head, tail = range(10)
print(head)
print(tail)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    9


这种写法在在迭代一些长度不固定的序列时，非常的方便，比如：现在有一场跳水比赛的决赛，共有10名裁判，10名选手，评分规则是这10名裁判依次给选手打分，如果裁判弃权则没有分，最后，去掉一个最高分，一个最低分，剩下的成绩的平均分就是选手的最终成绩。


```python
import random
import faker
f = faker.Faker('zh_CN')
# 生成10名运动员
players = [f.name() for i in range(10)]
# print(players)
def collect_scores(player, judge_num=10):
    """收集裁判的评分"""
    scores = []
    for i in range(judge_num):
        # 裁判有1/4的机率会弃权
        if i % 4 == 0:
            continue
        scores.append(random.randint(6,10))
    return player, scores

all_scores = [collect_scores(player) for player in players]
for player, scores in all_scores:
    scores.sort()
    min_score, *fine_scores, max_score = scores
    print(player, sum(fine_scores)/len(fine_scores))
```

    宗洁 6.8
    查林 9.0
    苏娜 7.6
    古强 7.8
    亓海燕 8.2
    叶金凤 7.0
    鄂瑜 8.2
    邬桂香 8.0
    权凤兰 9.0
    厍春梅 8.6


这种*号解压的写法也可以用在分割字符串的时候


```python
a,*b, c = '1,2,3,4,5'.split(',')
print(a, b, c)
```

    1 ['2', '3', '4'] 5

