import datetime
import pandas as pd

def parse_date(date):
    # This custom parsing works faster than:
    # datetime.datetime.strptime(date, "%Y-%m-%d")
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])
    d = datetime.date(year, month, day)
    ret = d
    return ret

# 读出数据，DataFrame格式
df = pd.read_csv('E:/PythonData/Tushare/000938.csv')
# 从df中选取数据段，改变段名；新段'Adj Close'使用原有段'close'的数据
df2 = pd.DataFrame({'Date' : df['trade_date'], 'Open' : df['open'],
                    'High' : df['high'],'Close' : df['close'],
                    'Low' : df['low'],'Volume' : df['vol'],
                    'Adj Close':df['close']})
df2['Date']=df2['Date'].apply(str)
#方法一：
# for i in range(len(df2.Date)):
#     df2.Date[i]=parse_date(df2.Date[i])

#方法二：
df2['Date']=df2['Date'].map(lambda x :'%s-%s-%s'%(x[0:4],x[4:6],x[6:8]))
print(df2)
df2.to_csv("E:/PythonData/CSV/000938.csv", index=False)