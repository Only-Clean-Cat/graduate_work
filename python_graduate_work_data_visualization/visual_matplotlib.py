'''
Визуализация данных с помощью библиотеки Matplotlib
'''
import matplotlib.pyplot as plt
import numpy as np
import csv

# Подготовка данных из файла csv для построения графиков
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


# Построение графика выручки магазинов по дням недели
# # Оформление графика
# # Размещение нескольких графиков на листе (размер, разрешение, цвет фона)
plt.figure(figsize=(20, 10), dpi=100, facecolor='#808080')
# Расположение графика на листе (строка, столбец, номер ячейки)
# plt.subplot(1,1,1)
plt.subplot(2,2,1)
# Название графика
plt.title('Выручка магазинов по дням недели', color='white')
# Подпись оси Х
plt.xlabel('день недели', color='white')
# Подпись оси Y
plt.ylabel('рублей', color='white')
# Установление лимита значений сетки оси
plt.ylim(0, 2000)
plt.xticks(color='white')
plt.yticks(color='white')
# Создание графика на плоскости с помощью метода plot() для каждого магазина с маркировкой
plt.plot(day_list, r_list, label='Елисеевский', color='r', marker='o')
plt.plot(day_list, g_list, label='На прудах',color='g', linestyle='--', marker='*')
plt.plot(day_list, b_list, label='Торгсин', color='b', marker='^', linewidth=5, alpha=0.5)
plt.plot(day_list, y_list, label='Манежный', color='y', linestyle=':', marker='+', linewidth=5, alpha=0.5)
plt.plot(day_list, m_list, label='Урбан', color='m', linestyle='-.', marker='+', linewidth=5, alpha=0.5)

# Рисуем сетку
plt.grid(color='gray', linewidth=0.5, linestyle='--')
# Создание легенды для объявления маркировки
plt.legend()

# Отображение графика в столбиках с помощью метода bar() со сдвигом стобцов и их ширины
# Расположение графика на листе (строка, столбец, место в строке)
# plt.subplot(1,1,1)
plt.subplot(2,2,2)
# Название графика
plt.title('Выручка магазинов по дням недели', color='white')
# Подпись оси Х
plt.xlabel('день недели', color='white')
# Подпись оси Y
plt.ylabel('рублей', color='white')
# Установление лимита значений сетки оси
plt.ylim(0, 2000)
# Ширина столбца
width = 0.18
x_indexes = np.arange(len(day_list))
plt.xticks(x_indexes, day_list)
plt.bar(x_indexes - width*2, r_list, color='r', label='Елисеевский', width=width)
plt.bar(x_indexes - width, g_list, color='g', label='На прудах', width=width)
plt.bar(x_indexes, b_list, color='b', label='Торгсин', width=width)
plt.bar(x_indexes + width, y_list, color='y', label='Манежный', width=width)
plt.bar(x_indexes + width*2, m_list, color='m', label='Урбан', width=width)
plt.xticks(color='white')
plt.yticks(color='white')
# Рисуем сетку
plt.grid(color='gray', linewidth=0.5, linestyle='--')
# Создание легенды для объявления маркировки
plt.legend(loc='upper left')

# Создание  графика рассеивания
# Расположение графика на листе (строка, столбец, номер ячейки)
# plt.subplot(1,1,1)
plt.subplot(2,2,3)
# Название графика
plt.title('Выручка магазинов по дням недели', color='white')
# Подпись оси Х
plt.xlabel('день недели', color='white')
# Подпись оси Y
plt.ylabel('рублей', color='white')
# Установление лимита значений сетки оси
plt.ylim(0, 2000)
# Создание графика на плоскости с помощью метода scatter() для каждого магазина с маркировкой
plt.scatter(day_list, r_list, c='r', linewidths=5,  label='Елисеевский')
plt.scatter(day_list, g_list, label='На прудах', c='g', linewidths=10)
plt.scatter(day_list, b_list, label='Торгсин', c='b', linewidths=5)
plt.scatter(day_list, y_list, label='Манежный', c='y', linewidths=5)
plt.scatter(day_list, m_list, label='Урбан', c='m', linewidths=5)
plt.xticks(color='white')
plt.yticks(color='white')
# Рисуем сетку
plt.grid(color='gray', linewidth=0.5, linestyle='--')
# Создание легенды для объявления маркировки
plt.legend()

# Создание круговой диаграммы
# Подготовка данных
c = ['r', 'g', 'b', 'y', 'm']
# Расположение графика на листе (строка, столбец, номер ячейки)
# plt.subplot(1,1,1)
plt.subplot(2,2,4)
# Название графика
plt.title('Доля магазина в выручке компании за неделю', color='white')
# Создание графика на плоскости с помощью метода plot() для каждого сотрудника с маркировкой
plt.pie(value_list, labels=name_list, explode=(0.07, 0.07, 0.07, 0.07, 0.07), colors=c,  autopct='%1.1f%%',
        radius=1.1, shadow=True)


# Библиотека автоматически подбирает масштаб и деление по осям графика,
# А также в нижнем меню графика есть возможность сохрания граика в формате png для использования



# Отображение графиков в формате 3D
# Демонстрирует создание 3D-графика, который содержит 2D-гистограммы, спроецированные на плоскости y=0, y=1 и т.д.



fig = plt.figure(figsize=(20, 20), dpi=80, facecolor='#808080')

ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y', 'm']
y_ticks = [1, 2, 3, 4, 5]
revenue = [r_list, g_list, b_list, y_list, m_list]
j = 0
for c, k in zip(colors, y_ticks):
    xs = np.array(day_list)
    ys = revenue[j]
    cs = [c] * len(xs)
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.6)
    j += 1
ax.set_xlabel('день недели')
ax.set_ylabel('название магазина')
ax.set_zlabel('рублей')
ax.set_yticks(y_ticks)
ax.set(yticklabels=name_list)
plt.title('Выручка магазинов по дням недели', color='white')

# Демонстрирует создание 3D-гистограмм

fig = plt.figure(figsize=(20, 20), dpi=80, facecolor='#808080')

ax2 = fig.add_subplot(111, projection='3d')
# Создание массива
x = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
y = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
c = ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'b', 'b', 'b', 'b', 'b', 'b', 'b', 'y', 'y', 'y', 'y', 'y', 'y', 'y',
     'm', 'm', 'm', 'm', 'm', 'm', 'm']

dx = np.ones_like(x)*0.25
dy = np.ones_like(x)*0.5
dz = r_list + g_list + b_list + y_list + m_list


ax2.bar3d(x, y, z, dx, dy, dz, color=c, alpha=0.6)
# Создание меток на оси
ax2.set_yticks([1, 2, 3, 4, 5, 6, 7])
ax2.set_xticks([1, 2, 3, 4, 5])
ax2.set_zticks([0, 200, 400, 600, 800, 1000, 1200, 1400, 1600])
# Подписи меток на оси
ax2.yaxis.set_ticklabels(day_list)
ax2.xaxis.set_ticklabels(name_list)


ax2.set_xlabel('название магазина')
ax2.set_ylabel('день недели')
ax2.set_zlabel('рублей')
plt.title('Выручка магазинов по дням недели', color='white')


# Демонстрирует создание 3D-графика рассеивания

fig = plt.figure(figsize=(20, 20), dpi=80, facecolor='#808080')

ax3 = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y', 'm']
y_ticks = [1, 2, 3, 4, 5]

revenue = [r_list, g_list, b_list, y_list, m_list]
j = 0
for c, k in zip(colors, y_ticks):
    xs = [1, 2, 3, 4, 5, 6, 7]
    y = revenue[j]
    cs = [c] * len(xs)
    ax3.scatter(xs, ys=k, zs=y, zdir='z', s=1500, c=cs, alpha=1)
    j += 1
ax3.set_xlabel('день недели')
ax3.set_ylabel('название магазина')
ax3.set_zlabel('рублей')

ax3.set_xticks([1, 2, 3, 4, 5, 6, 7])
ax3.set(xticklabels=day_list)
ax3.set_yticks([1, 2, 3, 4, 5])
ax3.set_zticks([0, 200, 400, 600, 800, 1000, 1200, 1400, 1600])
ax3.set(yticklabels=name_list)
plt.title('Выручка магазинов по дням недели', color='white')
plt.legend(name_list)

# Гистограмма безубыточеости

fig1 = plt.figure(figsize=(20, 20), dpi=100, facecolor='#808080')
#fig, ax4 = plt.subplots(subplot_kw={"projection": "3d"})
ax4 = fig1.add_subplot(111, projection='3d')
revenue1 = r_list + g_list + b_list + y_list + m_list
# Точка безубыточности
revenue2 = 900

x = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
y = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]

z = revenue1



ax4.stem(x, y, z, linefmt='g:', markerfmt='go', bottom=revenue2)

ax4.set_xlabel('название магазина')
ax4.set_ylabel('день недели')
ax4.set_zlabel('рублей')

ax4.set_yticks([1, 2, 3, 4, 5, 6, 7])
ax4.set(yticklabels=day_list)
ax4.set_xticks([1, 2, 3, 4, 5])
ax4.set_zticks([0, 200, 400, 600, 800, 1000, 1200, 1400, 1600])
ax4.set(xticklabels=name_list)
plt.title('Выручка магазинов по дням недели', color='white')



plt.show()