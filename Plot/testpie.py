import random
import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

# provinces = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
#              '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']
# num = [1, 1, 1, 17, 9, 22, 23, 42, 35, 7, 20, 21, 16,
#        24, 16, 21, 37, 12, 13, 14, 13, 7, 22, 8, 16, 13, 13]
# color_series = ['#FAE927', '#E9E416', '#C9DA36', '#9ECB3C', '#6DBC49',
#                 '#37B44E', '#3DBA78', '#14ADCF', '#209AC9', '#1E91CA',
#                 '#2C6BA0', '#2B55A1', '#2D3D8E', '#44388E', '#6A368B'
#                 '#7D3990', '#A63F98', '#C31C88', '#D52178', '#D5225B',
#                 '#D02C2A', '#D44C2D', '#F57A34', '#FA8F2F', '#D99D21',
#                 '#CF7B25', '#CF7B25', '#CF7B25']

temp_color_series = ['#FAE927', '#E9E416', '#C9DA36', '#9ECB3C', '#6DBC49',
                     '#37B44E', '#3DBA78', '#14ADCF', '#209AC9', '#1E91CA',
                     '#2C6BA0', '#2B55A1', '#2D3D8E', '#44388E', '#6A368B'
                     '#7D3990', '#A63F98', '#C31C88', '#D52178', '#D5225B',
                     '#D02C2A', '#D44C2D', '#F57A34', '#FA8F2F', '#D99D21',
                     '#CF7B25', '#CF7B25', '#CF7B25']

color_len = len(temp_color_series)

provinces = []
num = []
color_series = []

file = open('F:/PythonProject/Plot/result2.txt', 'r')
my_list = file.readlines()
for item in my_list:
    temp1, temp2 = item.split(',')
    # print(temp1)

    # print(temp2)
    if float(temp2) > 1000 and float(temp2) < 60000:
        provinces.append(temp1)
        num.append(temp2)
        color_series.append(
            temp_color_series[random.randint(0, color_len-1)])


# provinces = []
# num = []
# color_series = []

# for i in range(100):
#     provinces.append(random.randint(1, 100))
#     num.append(random.randint(1, 100))
#     color_series.append(
#         temp_color_series[random.randint(0, color_len-1)])

df = pd.DataFrame({'provinces': provinces, 'num': num})
df.sort_values(by='num', ascending=False, inplace=True)

v = df['provinces'].values.tolist()
d = df['num'].values.tolist()

pie1 = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))
pie1.set_colors(color_series)
pie1.add("", [list(z) for z in zip(v, d)],
         radius=["30%", "135%"],
         center=["50%", "65%"],
         rosetype="area"
         )
pie1.set_global_opts(title_opts=opts.TitleOpts(title='example'),
                     legend_opts=opts.LegendOpts(is_show=False),
                     toolbox_opts=opts.ToolboxOpts())
pie1.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="inside", font_size=12,
                                               formatter="{b}:{c}day", font_style="italic",
                                               font_weight="bold", font_family="Microsoft YaHei"
                                               ),
                     )
pie1.render('myplot.html')
