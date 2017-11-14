# coding:utf-8

# 定义一个最简单的闭包
def out():
    i = 1
    def f():
        print(i)
    return f
f1 = out()
# 打印闭包的值
#__closure__里包含了一个元组(tuple)。这个元组中的每个元素是cell类型的对象
print(f1.__closure__[0].cell_contents)
# 输出1
f1()

def out_err():
    i = 1
    def f():
        i = i+1
        print(i)
    return f
try:
    out_err()()
except Exception as e:
    print('python 的函数内，可以直接引用外部变量，但不能改写外部变量')
    print(e)


# 如果想改写外部变量，需要使用nonlocal关键字（python3引进）
def out_nonlocal():
    i = 1
    def f():
        nonlocal i
        i += 1
        print(i)
    return f
out_nonlocal()()


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1(), f2() ,f3()

print f1.__closure__[0].cell_contents # 打印闭包值 即i的值 =3

def count():
    fs = []
    for i in range(1, 4):
        def f(j=i):
             return j*j
        fs.append(f)
    return fs



f1, f2, f3 = count()
print f1(), f2() ,f3()

print f1.__closure__  # 没有闭包，因为外部变量i已经传值给默认参数j了