# bilibili_comment

以白蛇传为例 抓取时间 20190308 22:10
爬取b站评论（JS解析）：用户名，性别，评论时间，评论内容，等级，UID号
![Image text](https://github.com/fenghuoxiguozu/bilibili_comment/tree/master/img/example.png)

1. 解析网址: 变化参数 oid:AV号  ts:时间戳  pn:页数 
![Image text](https://github.com/fenghuoxiguozu/bilibili_comment/tree/master/img/url.png)

2.去除热门评论，使用线程池（4个）抓取，1000多页评论1s不到完成
![Image text](https://github.com/fenghuoxiguozu/bilibili_comment/tree/master/img/csv.png)

3.用pandas+pyecharts分析数据
  a.有大约一半B站用户没有填写身份认证，41%的男性发表评论，远高于10%的女性
  ![Image text](https://github.com/fenghuoxiguozu/bilibili_comment/tree/master/img/sex.png)
  b.只有3月份的图表，说明电影是3月才上架的
  ![Image text](https://github.com/fenghuoxiguozu/bilibili_comment/tree/master/img/day.png)
  c.晚上3~11点发表的人数最多，大致推出这个时间段观看电影的人最多
  ![Image text](https://github.com/fenghuoxiguozu/bilibili_comment/tree/master/img/time.png)
  d.从观众发表的评论可以看出 小白，许仙，白蛇，会员这几个字段最多。前3个词是电影里人物名，第四个说明需要会员才能观看
  ![Image text](https://github.com/fenghuoxiguozu/bilibili_comment/tree/master/img/woedcloud.png)
