import requests

class testClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print1(self):
        print("我的名字是%s,我的年龄是%d"%(self.name,self.age))
    def testDownload(self):
        headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'}
        url='https://img.ivsky.com/img/tupian/t/201008/05/bianxingjingang-001.jpg'

        re=requests.get(url,headers=headers)
        print(re.status_code)#查看请求状态，返回200说明正常

        path='./test.jpg'#文件储存地址
        with open(path, 'wb') as f:#把图片数据写入本地，wb表示二进制储存
            for chunk in re.iter_content(chunk_size=256):
                f.write(chunk)
