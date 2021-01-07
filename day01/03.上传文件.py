'''
上传文件：
    本地文件上传到服务器上，比如上传头像，上传附件等
'''

import requests
#上传文件的接口
url = "http://www.httpbin.org/post"
#上传的文件是本地磁盘的文件
#'name':file-tule

filePath = "d:/test.txt"
filePath2 = "d:/test.png"
with open (filePath,'rb') as f:
    with open(filePath2, 'rb') as f2:
        file = {
            "file1":(filePath,f),#2-tuple('filename',fileobj)
            "file2":(filePath2,f2,"image/png") #3-tuple ('filename',fileobj,'conten_type')

        }
        r = requests.post(url,files=file)
        print(r.text)