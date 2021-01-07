'''
fixture作用域：
    函数级（默认）、模块级、类级、Session级别的（跨文件）
'''
import pytest
#scope = ‘function’  函数界别2/3/4之情前置和后置
#scope = 'module'  模块级别  首次顶用login的地方执行前置，整个文件执行完执行后置，2执行前置，4执行后置
@pytest.fixture(scope='module')
def login():
    print("前置：登录系统")
    yield
    print("后置：退出登录")

@pytest.fixture(scope='module')
def db():
    print("前置，连接数据库")
    yield
    print("后置：断开数据库")

def test_01():
    print("用例1")

def test_02(login):
    print("用例2")

def test_03(login):
    print("用例3")


def test_04(login):
    print("用例4")

