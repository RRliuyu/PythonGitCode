
import tushare as ts
import datetime
api = ts.pro_api('5f37df276dab4fff9a3783499fd18174ec34caf4a84dc1e953c7d987')
df = api.cashflow(ts_code='000938.SZ', start_date='20180101', end_date='20180730')
print(df)
