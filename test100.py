from pyecharts.charts import Bar,Scatter
from pyecharts import options as opts

# # V1 版本开始支持链式调用
# # 你所看到的格式其实是 `black` 格式化以后的效果
# # 可以执行 `pip install black` 下载使用
# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#     .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
#     # 或者直接使用字典参数
#     # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
# )
# bar.render()

scatter1 = Scatter()
scatter1.set_global_opts(xaxis_opts=opts.AxisOpts(type_='value',is_scale=True),
                         yaxis_opts=opts.AxisOpts(is_scale=True),
                         datazoom_opts=[opts.DataZoomOpts()])

for x in range(10):
        x1=[x]
        y1=[x]
        print(x1)
        scatter1.add_xaxis(x1)
        scatter1.add_yaxis("vvv", y1)
scatter1.render(path='E:\\aaa.html')