import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line,Kline


# 显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
# 读出数据，DataFrame格式
df = pd.read_csv('E:/PythonData/CSV_min/600036.csv')
# 从df中选取数据段，改变段名；新段'Adj Close'使用原有段'close'的数据
df1 = pd.DataFrame({'Date Time' : df['Date Time'], 'Open' : df['Open'],
                    'High' : df['High'],'Close' : df['Close'],
                    'Low' : df['Low'],'Volume' : df['Volume']})
#调整时间格式
df1['Date Time']=df1['Date Time'].apply(str)
df1['Date Time']=df1['Date Time'].map(lambda x :'%s-%s-%s %s:%s:%s'%(x[0:4],x[5:7],x[8:10],x[11:13],x[14:16],x[17:19]))


#倒序排列
df1=df1.sort_index(ascending=False)
# print(df1)
# line1 =Line('折线图',background_color = 'white',title_text_size = 25)
# line2 =Line('折线图',background_color = 'white',title_text_size = 25)
# line1.add('收盘价',df1.Date,df1.Close, is_datazoom_show=True)
# line2.add('成交量',df1.Date,df1.Volume, is_datazoom_show=True)
# overlap = Overlap()
# overlap.add(line1)
# overlap.add(line2,is_add_yaxis=True,yaxis_index=1)
# overlap.render()
# overlap.render(path = 'D:\\折线图.html')

# kline=Kline()
# kline.add_xaxis(df1.Date)
# kline.add_yaxis("kline",df1.Open,df1.High,df1.Close,df1.Low)
# print(df1.Date)
# print(df1[df1.Date.isin(['2019/07/16 10:30:00'])])

# print(df1[~df1['Date'].str.contains("09:30:00")])

df2=df1[~df1['Date Time'].str.contains("09:30:00")]
df2.to_csv("E:/Stock/Data_Min/60min_4_600036.csv", index=False)
df2=df2.reset_index()

print(df2)
#
#
# # line1 =Line()
# # # line1.set_global_opts(xaxis_opts=opts.AxisOpts(type_="time",name="aaavvvv"),datazoom_opts=[opts.DataZoomOpts()])
# # # line1.add_xaxis(df1.Date)
# # # line1.add_yaxis("aaa",df1.Close)
# # # line1.render(path = 'D:\\折线图.html')
#
# date=df2.['Open'].tolist()
date=df2.xs('Date Time', axis=1).tolist()
data=[]
for idx in df2.index :
     row=[df2.iloc[idx]['Open'],df2.iloc[idx]['Close'],df2.iloc[idx]['Low'],df2.iloc[idx]['High']]
     data.append(row)

# data=data.reverse()
print(data)

kline1=Kline()
kline1.set_global_opts(yaxis_opts=opts.AxisOpts(is_scale=True),
            xaxis_opts=opts.AxisOpts(is_scale=True),
            datazoom_opts=[opts.DataZoomOpts()])
kline1.add_xaxis(date)
kline1.add_yaxis("aaa",data)
kline1.render(path = 'D:\\600036.html')

line1=Line()
line1.set_global_opts(yaxis_opts=opts.AxisOpts(is_scale=True),
            xaxis_opts=opts.AxisOpts(is_scale=True),
            datazoom_opts=[opts.DataZoomOpts()])
line1.add_xaxis(date)
line1.add_yaxis("vvv",df2.Close)
kline1.overlap(line1)
kline1.render(path = 'D:\\600036.html')
