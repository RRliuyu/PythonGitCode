
import tushare as ts
import datetime
api = ts.pro_api('5f37df276dab4fff9a3783499fd18174ec34caf4a84dc1e953c7d987')
code='000938'
start='20180101'
end='20181231'
adj='qhf'
freq='D'
ds = ts.pro_bar(pro_api=api,ts_code='000938.SZ', start_date=start, end_date=end, adj=adj, freq=freq)
print(ds)
