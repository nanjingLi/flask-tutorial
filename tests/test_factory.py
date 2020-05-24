'''
@author: Administrator
@Wechat Contact:第一行Python代码 
@project: flask-tutorial
@file: test_factory.py
@time: 2020/5/21 23:50
@desc:
'''
from flaskr import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING':True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'hello ,world!'