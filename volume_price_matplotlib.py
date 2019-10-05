import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib import ticker
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
fig=plt.figure()
ax1=fig.add_subplot(111)

#设置x轴的刻度
ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.plot(df1.Date,df1.Volume)
ax2=ax1.twinx()
ax2.plot(df1.Date,df1.Close,'r')
plt.show()