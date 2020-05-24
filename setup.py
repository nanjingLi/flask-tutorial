'''
@author: Administrator
@Wechat Contact:第一行Python代码 
@project: flask-tutorial
@file: setup.py
@time: 2020/5/21 23:50
@desc:
'''
from setuptools import find_packages,setup
setup(
    name='flask',
    version = '1.0.0',
    packages = find_packages(),
    include_package_data = True,
    zip_safe =False,
    install_requires = [
        'flask',
    ],
)