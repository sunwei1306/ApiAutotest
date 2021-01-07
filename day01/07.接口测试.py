import requests



# 注册
url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"15903591116","pwd":"123456"}
r = requests.post(url,data=cs)
print(r.text)
assert  r.json()['code'] == "10001"


url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"18011132243","pwd":"123456","regname":"hah"}
r = requests.post(url,data=cs)
print(r.text)
assert  r.json()['code'] == "10001"

url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"18012122224","pwd":"","regname":""}
r = requests.post(url,data=cs)
print(r.text)
assert  r.json()['code'] == "20103"

url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"","pwd":"1234565","regname":""}
r = requests.post(url,data=cs)
print(r.text)
assert  r.json()['code'] == "20103"

url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"","pwd":"","regname":""}
r = requests.post(url,data=cs)
print(r.text)
assert  r.json()['code'] == "20103"

url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"","pwd":"","regname":"yy"}
r = requests.post(url,data=cs)
print(r.text)
assert  r.json()['code'] == "20103"


url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"18012312324","pwd":"asd12","regname":""}
r = requests.post(url,data=cs)
print(r.text)
assert  r.json()['code'] == "20108"


url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"18012312324","pwd":"123141421231432151451451451514523452345134","regname":""}
r = requests.post(url,data=cs)
print(r.text)
assert  r.json()['code'] == "20108"

url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"1111111","pwd":"123456","regname":""}
r = requests.post(url,data=cs)
print(r.text)
assert  r.json()['code'] == "20109"

url = "http://jy001:8081/futureloan/mvc/api/member/register"
cs = {"mobilephone":"15006007018","pwd":"123456","regname":""}
r = requests.post(url,data=cs)
print(r.text)
assert  r.json()['code'] == "10001"