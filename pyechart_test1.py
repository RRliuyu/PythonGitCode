
from pyecharts import options as opts
from pyecharts.charts import Line,Scatter
from pyecharts.charts.composite_charts.page import Page

scatter1 = Scatter()
scatter1.set_global_opts(
                         yaxis_opts=opts.AxisOpts(type_='value'),
                         xaxis_opts=opts.AxisOpts(type_='value'),
                         datazoom_opts=[opts.DataZoomOpts()])
scatter1.extend_axis(yaxis=opts.AxisOpts(type_='value',position='right'))
scatter1.extend_axis(yaxis=opts.AxisOpts(type_='value',position='right',offset=40))

line1 = Line()
line1.set_global_opts(
                         yaxis_opts=opts.AxisOpts(type_='value'),
                         xaxis_opts=opts.AxisOpts(type_='value'),
                         datazoom_opts=[opts.DataZoomOpts()])

line2 = Line()
line2.set_global_opts(
                         yaxis_opts=opts.AxisOpts(type_='value'),
                         xaxis_opts=opts.AxisOpts(type_='value'),
                         datazoom_opts=[opts.DataZoomOpts()])


x1=[11,12,13,14,15,16]
y1=[12,24,3,7,31,4]

x2=[11,12,13,14,15,16]
y2=[333,444,555,666,777,333]

x3=[11,12,13,14,15,16]
y3=[1211,1222,2444,2332,1441,1525]

scatter1.add_xaxis(x1)
scatter1.add_yaxis("scatter1", y1)

line1.add_xaxis(x2)
line1.add_yaxis("line1",y2,yaxis_index=1)

line2.add_xaxis(x3)
line2.add_yaxis("line2",y3,yaxis_index=2)

scatter1.overlap(line1)
scatter1.overlap(line2)

scatter1.render(path='E:\\Stock/html_png_Total/test1.html')