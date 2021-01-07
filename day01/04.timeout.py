'''
timeout超时
1.上传文件，上传2M耗时比较短，2G文件耗时比较久。可以设置timeout设置时间比较久的文件
2.接口测试时，测试接口性能，返回结果是否在某个时间段内
    比如获取用户列表的接口，是否在100ms以内
'''

import requests

url = "http://192.168.150.222:8081/futureloan/mvc/api/member/list"
#Read timed out.
r = requests.get(url,timeout=0.1)#100ms
print(r.text)

'''
代理 proxies
1.用界面操作某个功能，结果正常。但是使用自动化操作同样的功能，结果报错
    界面操作时，抓包
    自动化脚本执行时，抓包
    对比抓到的包，检查异常点
2.频繁的像服务器发起请求，服务器当做攻击处理，将IP禁用掉，使用代理IP发送请求
'''
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/list"
proxy = {
    "http":"http://127.0.0.1:8888", #HTTP协议，使用http://127.0.0.1:8888代理
    "https":"http://127.0.0.1:8888"
}
r = requests.get(url,proxies=proxy)#设置代理后要把对应工具打开
print(r.text)
#https的请求，使用代理时，需要设置忽略证书
r = requests.get("https://www.baidu.com",proxies=proxy,verify=False)
print(r.text)