import requests
import time
import csv
import re
from concurrent.futures import ThreadPoolExecutor


def parse_info(crawl_url):
    response = requests.get(crawl_url,headers=headers)
    contents=re.findall(r'page(.*?)top', response.text, re.S)
    #去除热门评论
    name = re.findall(r'member":{"mid":".*?","uname":"(.*?)","sex', contents[0], re.S)
    #时间戳返回时间格式
    ctime = re.findall(r'ctime":(.*?),', contents[0], re.S)
    comment_time = map(lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(x))), ctime)
    #性别 uid 等级 评论内容
    sex = re.findall(r'member":{"mid":".*?sex":"(.*?)"', contents[0], re.S)
    uid = re.findall(r'member":{"mid":"(.*?)"', contents[0], re.S)
    level = re.findall(r'member":{"mid.*?current_level":(.*?),', contents[0], re.S)
    comment = re.findall(r'message":"(.*?)"', contents[0], re.S)
    #打包成每个人发表的信息列表
    result = zip(name, uid, sex, level, comment_time, comment)
    save_to_csv(list(result))

def save_to_csv(result):
    # head = ['用户名', 'UID', '性别', '等级', '评论时间', '评论内容']
    with open('comment.csv', 'a+',encoding='utf-8',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(result)

if __name__ == '__main__':
    start_time=time.time()
    executor=ThreadPoolExecutor(max_workers=4)
    # oid=input("输入AV号：")# oid AV号
    # pn = input("输入爬取页数：")
    ts = int(time.time() * 1000)
    oid=44994209
    start_url = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn={}&type=1&oid={}&sort=0&_={}'
    headers = {
        'Host':'api.bilibili.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Content-Encoding':'gzip',
        'Content-Type':'application/json; charset=utf-8'
    }
    urls=[start_url.format(pn,oid,str(ts)) for pn in range(1,1210)]
    executor.map(parse_info,urls)

    end_time=time.time()-start_time
    print('爬虫结束,总耗时%.4fs'%end_time)
