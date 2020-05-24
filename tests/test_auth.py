'''
@author: Administrator
@Wechat Contact:第一行Python代码 
@project: flask-tutorial
@file: test_auth.py
@time: 2020/5/21 23:50
@desc:
'''
import pytest
from flask import g,session
from flaskr.db import get_db
import logging


def test_register(client,app):
    assert client.get('/auth/login').status_code == 200
    response = client.post(
        '/auth/login',data={'username':'a','password':'a'}
    )
    logging.info('这是调试内容')
    assert 'http://localhost/auth/login' == response.headers['Location']

    with app.app_context():
        assert get_db().execute(
            'select * from user where username = "a"',
        ).fetchone() is not None

@pytest.mark.paramtrize(('username','password','message'),(
        ('','',b'Username is required'),
        ('a','',b'Password is required'),
        ('test','test',b'already registered'),
))
def test_register_validate_input(client,username,password,message):
    response = client.post(
        '/auth/register',
        data = {'username':username,'passwrod':password}
    )
    assert message in response.data

def test_logout(client,auth):
    auth.login()
    with client:
        auth.logout()
        assert 'user_id' not in session


