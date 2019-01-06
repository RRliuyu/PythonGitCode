import tushare as ts
import pandas as pd
import datetime
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#获取数据
pro = ts.pro_api('5f37df276dab4fff9a3783499fd18174ec34caf4a84dc1e953c7d987')
df = pro.daily(ts_code='000938.SZ', start_date='20180101', end_date='20180718')
# 数据存盘
df.to_csv('E:/PythonData/Tushare/000938.csv')
# 读出数据，DataFrame格式
df = pd.read_csv('E:/PythonData/Tushare/000938.csv')
# 从df中选取数据段，改变段名；新段'Adj Close'使用原有段'close'的数据
df2 = pd.DataFrame({'Date' : df['trade_date'], 'Open' : df['open'],
                    'High' : df['high'],'Close' : df['close'],
                    'Low' : df['low'],'Volume' : df['vol'],
                    'Adj Close':df['close']})
#调整时间格式
df2['Date']=df2['Date'].apply(str)
df2['Date']=df2['Date'].map(lambda x :'%s-%s-%s'%(x[0:4],x[4:6],x[6:8]))

df2.to_csv("E:/PythonData/CSV/000938.csv", index=False)