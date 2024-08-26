'''
Визуализация данных с помощью библиотеки Plotly
'''
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
# Обязательные зависимости
import pandas as pd
import csv

df = pd.read_csv('revenue.csv', encoding='utf-8')

data_file = pd.read_csv('data_sea.csv', encoding='utf-8')

# Гистограмма выручки по видам товара
fig = px.bar(data_file, 'вид товара', y='сумма',facet_col='магазин', color='вид товара')

# Гистограмма по проданному количеству товара в разбивке по виду и дню недели
fig = px.bar(data_file, 'магазин', y='количество', facet_col='день недели',  color='вид товара')

# Гистограмма с анимацией
fig = px.bar(data_file, 'магазин', y='количество', animation_frame="день недели",  animation_group="магазин",
             color='вид товара')

# Построение информационной панели
# Подготовка данных
with open('revenue.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    list_rows = list(csv_reader)
day_list = list_rows[0][1:]
r_list = list(map(int, list_rows[1][1:]))
g_list = list(map(int, list_rows[2][1:]))
b_list = list(map(int, list_rows[3][1:]))
y_list = list(map(int, list_rows[4][1:]))
m_list = list(map(int, list_rows[5][1:]))
name_list = list_rows[1][0],  list_rows[2][0],  list_rows[3][0],  list_rows[4][0],  list_rows[5][0]
value_list = sum(r_list), sum(g_list), sum(b_list), sum(y_list), sum(m_list)
# # Создаем таблицу данных
table_data = [list_rows[0][0:],
              list_rows[1][0:],
              list_rows[2][0:],
              list_rows[3][0:],
              list_rows[4][0:],
                list_rows[5][0:]]


# # Инициализируем график по таблице
fig = ff.create_table(table_data, height_constant=50)

# # Добовляем графические данные
trace1 = go.Bar(x=day_list, y=r_list, xaxis='x2', yaxis='y2',
                marker=dict(color='red'),
                name='Елисеевский')
trace2 = go.Bar(x=day_list, y=g_list, xaxis='x2', yaxis='y2',
                marker=dict(color='green'),
                name='На прудах')
trace3 = go.Bar(x=day_list, y=b_list, xaxis='x2', yaxis='y2',
                marker=dict(color='blue'),
                name='Торгсин')
trace4 = go.Bar(x=day_list, y=y_list, xaxis='x2', yaxis='y2',
                marker=dict(color='yellow'),
                name='Манежный')
trace5 = go.Bar(x=day_list, y=m_list, xaxis='x2', yaxis='y2',
                marker=dict(color='magenta'),
                name='Урбан')
# # Передача данных в график
fig.add_traces([trace1, trace2, trace3, trace4, trace5])
fig['layout']['xaxis2'] = {}
fig['layout']['yaxis2'] = {}

# # Масштабирование на листе
fig.layout.yaxis.update({'domain': [0, .45]})
fig.layout.yaxis2.update({'domain': [0.5, 1]})
fig.layout.yaxis2.update({'anchor': 'x2'})
fig.layout.xaxis2.update({'anchor': 'y2'})
fig.layout.yaxis2.update({'title': 'Рублей'})
# # Определение название графика и места
fig.layout.margin.update({'t':75, 'l':50})
fig.layout.update({'title': 'Выручка магазинов за неделю'})
# # Высота проекции таблиц
fig.layout.update({'height':1200})


# Построение графика рассеивания
fig = px.scatter(data_file, x='сумма', y='количество', size_max=10000, facet_col='вид товара', color='магазин')

# Анимированный график рассеивания
fig = px.scatter(data_file, x='количество', y='сумма', animation_frame='день недели', animation_group='вид товара',
           size='количество', color='магазин', hover_name='вид товара',
           log_x=True, size_max=120, range_x=[40,200], range_y=[140, 800])


# Построение круговой диаграммы
fig = px.pie(data_file, values='сумма', names='магазин', title='Доля магазина в выручке компании')
# Бублик
fig = px.pie(data_file, values='сумма', names='вид товара', title='Доля товара в выручке компании',
             color_discrete_sequence=px.colors.sequential.RdBu,
             hover_data=['вид товара'], labels={'вид товара':'life expectancy'}, hole=.3)
fig.update_traces(textposition='inside', textinfo='percent+label')

fig = go.Figure(data = [go.Pie(labels=name_list, values=value_list, pull=[0, 0, 0.2, 0, 0])])

# Построение финансового графика свечей

# Создание данных
open_data = [r_list[0], g_list[0], b_list[0], y_list[0], m_list[0]]
high_data = [max(r_list), max(g_list), max(b_list), max(y_list), max(m_list)]
low_data = [min(r_list), min(g_list), min(b_list), min(y_list), min(m_list)]
close_data = [r_list[-1], g_list[-1], b_list[-1], y_list[-1], m_list[-1]]
dates = name_list
fig = go.Figure(data=[go.Candlestick(x=dates,
                       open=open_data, high=high_data,
                       low=low_data, close=close_data)])

# Построение линейного графика

fig = go.Figure()

fig.add_trace(go.Box(x=r_list, name=name_list[0]))
fig.add_trace(go.Box(x=g_list, name=name_list[1]))
fig.add_trace(go.Box(x=b_list, name=name_list[2]))
fig.add_trace(go.Box(x=y_list, name=name_list[3]))
fig.add_trace(go.Box(x=m_list, name=name_list[4]))


# Построение 3D диаграмм

# Рассеивания
fig = px.scatter_3d(data_file, x='количество', y='сумма', z='день недели',
              color='вид товара')

fig = px.scatter_3d(data_file, x='количество', y='сумма', z='день недели',
                    color='магазин', symbol='вид товара')

# График поверхностей
fig = go.Figure(go.Surface(
    contours = {
        "x": {"show": True, "start": 1.5, "end": 2, "size": 0.04, "color":"white"},
        "z": {"show": True, "start": 0.5, "end": 0.8, "size": 0.05}
    },
    x = name_list,
    y = name_list,
    z = [
        r_list,
        g_list,
        b_list,
        y_list,
        m_list
    ]))
fig.update_layout(
        scene = {
            "xaxis": {"nticks": 100},
            "zaxis": {"nticks": 20},
            'camera_eye': {"x": 0, "y": -1, "z": 0.5},
            "aspectratio": {"x": 1, "y": 1, "z": 0.2}
        })




fig.show()