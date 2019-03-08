import pandas as pd


df=pd.read_csv('comment.csv')
df.columns=['用户名', 'UID', '性别', '等级', '评论时间', '评论内容']

from pyecharts import Pie

item=df["性别"].value_counts()
index=item.index
values=item.values
pie = Pie("B站评论性别分布表",title_pos='center')
pie.add("性别", index, values,                    #"haha":鼠标放上去额外显示的标签
        radius=[35, 75],                     #扇区圆心角展现数据的百分比，半径展现数据的大小
        label_text_color='Black',             #标签颜色
        is_label_show=True,                  #是否显示标签
        legend_orient='vertical',            #图例展开方向
        legend_pos='right')
pie.render('./html/sex.html')


from pyecharts import Line
day_time=df['评论时间'].str.split(' ',expand=True)
split_day=day_time[0].str.split('-',expand=True)[0]+'-'+day_time[0].str.split('-',expand=True)[1]
split_time=day_time[1].str.split(':',expand=True)[0]


item1=split_day.value_counts()
index1=item1.index
values1=item1.values

line = Line('B站评论月份折线面积示例图')
line.add('时间',index1,values1,
    mark_point = ['max'],  #标注点：平均值，最大值，最小值
    mark_point_symbol = 'arrow',         #标注day点：钻石形状
    mark_point_symbolsize=40)      #标注点：标注文本颜色
line.render('./html/comment_day.html')


item2=split_time.value_counts()
index2=item2.index
values2=item2.values

line = Line('B站评论时间折线面积示例图')
line.add('月份',index2,values2,
    mark_point = ['max'],  #标注点：平均值，最大值，最小值
    mark_point_symbol = 'diamond',         #标注点：钻石形状
    mark_point_symbolsize=40)      #标注点：标注文本颜色
line.render('./html/comment_time.html')






from wordcloud import WordCloud
from PIL  import Image
import jieba
import numpy as np

text=df['评论内容'].to_dict().values()
text=",".join(text)
result=jieba.cut(text.replace('回复',''))
result=" ".join(result)

mask=np.array(Image.open('./tool/bg.jpg'))
wordcloud=WordCloud(mask=mask,font_path='./tool/font.ttf').generate(result)
image_produce=wordcloud.to_image()
image_produce.show()
