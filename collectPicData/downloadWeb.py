import re
import requests

#url="https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1668592541529_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=&ie=utf-8&sid=&word=%E5%8F%A3%E7%BD%A9+%E4%BA%BA"
url="https://google.com"
headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
html = requests.get(url,headers=headers)#得到一个Response对象

print(html)
html_bytes = html.content#属性.content用来显示bytes型网页的源代码
html_str = html_bytes.decode()#属性.decode()用来把bytes型的数据解码为字符串型的数据，默认编码格式UTF-8
# print(html_str)
dataouts=re.findall(r"[\"](middleURL)[\"\\:\"](.+?)\?",html_str)
print(dataouts)
data="";
for url in dataouts:
    # print(url)
    data=data.join(url)+"?"
# print(data)
dataout=re.findall("https(.+?)\?",str(data))
# print(dataout)
for picurl in dataout:
    print("https://"+picurl)
