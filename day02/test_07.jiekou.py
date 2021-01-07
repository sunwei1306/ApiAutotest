
import pytest
import requests






@pytest.fixture(params=[{"mobilephone":"15903591116","pwd":"123456"},
                        {"mobilephone":"18011132243","pwd":"123456","regname":"hah"},
                        {"mobilephone":"18012122224","pwd":"","regname":""},
                        {"mobilephone":"","pwd":"1234565","regname":""},
                        {"mobilephone":"","pwd":"","regname":""}])



def register_data(request):

    return request.para

def test_register(login_data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    print(f"注册功能，测试数据为：{register_data}")
    r = requests.post(url,data=register_data)
    assert r.json()['msg'] == register_data['msg']


@pytest.fixture(params=[{"data":{"mobilephone":"18012122224","pwd":"123456","regname":""},
                         "expect":{"status":0,"code":20110,"data":None,"msg":"手机号码已被注册"}},
                         {"data":{"mobilephone":"18012345678","pwd":"1234","regname":""},
                          "expect":{"status":0,"code":20108,"data":None,"msg":"密码长度必须为6~18位"}}])
def register_data1(request):
    return request.para


def test_register1(register_data1):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    print(f"注册功能，测试数据为：{register_data1['data']}")
    r = requests.post(url,data=register_data1['data'])
    assert r.json()['msg'] == register_data['msg']