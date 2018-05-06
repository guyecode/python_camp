

```python
import sys, threading

def log_exception(*args):
#     print('got exception %s' % (args,))
    print('haha')
sys.excepthook = log_exception

def foo():
    a = 1 / 0
threading.Thread(target=foo).start()
```

    Exception in thread Thread-5:
    Traceback (most recent call last):
      File "/Users/guye/anaconda/envs/py3/lib/python3.6/threading.py", line 916, in _bootstrap_inner
        self.run()
      File "/Users/guye/anaconda/envs/py3/lib/python3.6/threading.py", line 864, in run
        self._target(*self._args, **self._kwargs)
      File "<ipython-input-26-3d907fcc11a8>", line 9, in foo
        a = 1 / 0
    ZeroDivisionError: division by zero
    

