'''
@author: Administrator
@Wechat Contact:第一行Python代码 
@project: flask-tutorial
@file: a1.py
@time: 2020/5/22 12:35
@desc:
'''
def test1():
    'test1...'
    print('test1')

def test2():
    'test2...'

    print('test2')

print (test1.__name__)
print (test1.__doc__)

print (test2.__name__)
print (test2.__doc__)
print('-------------------')
#加装饰器未加wraps代码
from functools import wraps
def login_required(view_func):
    def wrapper(*args,**kwargs):
        pass
    return wrapper

@login_required
def test1():
    'test1...'
    print('test1')

@login_required
def test2():
    'test2...'
    print('test2')
print (test1.__name__)
print (test1.__doc__)

print (test2.__name__)
print (test2.__doc__)

#加装饰器加wraps代码：
from functools import wraps
def login_required(view_func):
    @wraps(view_func)
    def wrapper(*args,**kwargs):
        pass
    return wrapper

@login_required
def test1():
    'test1...'
    print('test1')
@login_required
def test2():
    'test2...'
    print('test2')
print (test1.__name__)
print (test1.__doc__)

print (test2.__name__)
print (test2.__doc__)