from selenium import webdriver
import time
from lxml import etree
import random
from urllib import request
import os


def pic_url_get(num):
    for i in range(num):
        time.sleep(random.uniform(0, 2))
        content = driver.page_source
        html = etree.HTML(content)
        pic_url = html.xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img/@src')[0]
        pic_urls.append(pic_url)
        print('第{}张图片获取成功'.format(i + 1))
        next_page_button = driver.find_element_by_xpath(
            '//div[@id="Sva75c"]/div/div/div[3]/div[2]//div/div[1]/div[1]/div[1]/a[3]')
        next_page_button.click()


def pics_download():
    a = 1
    for pic_url in pic_urls:
        opener = request.build_opener()
        opener.addheaders = [('User-agent',
                              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'),
                             ('accept',
                              'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')]
        request.install_opener(opener)
        name = os.path.split(pic_url)[-1]
        if '.' not in name:
            name = name + '.jpg'
        try:
            request.urlretrieve(pic_url, r'C:\Users\msi\Desktop\google\{0}'.format(name))
            print(name + '下载完成！！！')
        except:
            request.urlretrieve(pic_url, r'C:\Users\msi\Desktop\google\{0}.jpg'.format(a))
            print(str(a) + '下载完成！！！')
            a += 1


if __name__ == '__main__':
    if os.path.isdir(r'D:\yolov5-6.2\collectPicData\pic'):  # 修改成你想要存储到的地方
        pass
    else:
        os.mkdir(r'D:\yolov5-6.2\collectPicData\pic')  # 修改成你想要存储到的地方
    num = int(input('请输入你想要下载的图片数量(整数)：'))
    pic_urls = []
    url = input('请输入你想要下载的谷歌图片网址：')
    driver_path = r'D:\yolov5-6.2'  # 修改成你的chromedriver的路径10
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(url)
    first_pic_button = driver.find_element_by_xpath('//div[@id="islrg"]/div[1]/div[1]/a[1]')
    first_pic_button.click()
    pic_url_get(num)
    print(pic_urls)
    pics_download()
    print('-----------------------------------爬取完成------------------------------------------')