import pandas as pd
from pyecharts import Line,Overlap
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
# 读出数据，DataFrame格式
df = pd.read_csv('E:/PythonData/Tushare/000938.csv')
# 从df中选取数据段，改变段名；新段'Adj Close'使用原有段'close'的数据
df1 = pd.DataFrame({'Date' : df['trade_date'], 'Open' : df['open'],
                    'High' : df['high'],'Close' : df['close'],
                    'Low' : df['low'],'Volume' : df['vol'],
                    'Adj Close':df['close']})
#调整时间格式
df1['Date']=df1['Date'].apply(str)
df1['Date']=df1['Date'].map(lambda x :'%s/%s/%s'%(x[0:4],x[4:6],x[6:8]))

#倒序排列
df1=df1.sort_index(ascending=False)

print(df1)
line1 =Line('折线图',background_color = 'white',title_text_size = 25)
line2 =Line('折线图',background_color = 'white',title_text_size = 25)
line1.add('收盘价',df1.Date,df1.Close, is_datazoom_show=True)
line2.add('成交量',df1.Date,df1.Volume, is_datazoom_show=True)
overlap = Overlap()
overlap.add(line1)
overlap.add(line2,is_add_yaxis=True,yaxis_index=1)
overlap.render()
overlap.render(path = 'D:\\折线图.html')