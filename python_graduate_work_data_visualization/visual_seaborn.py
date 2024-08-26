'''
Визуализация данных с помощью библиотеки Seaborn
'''
import seaborn as sns
# Обязательные зависимости
import pandas as pd
import matplotlib.pyplot as plt

data_file = pd.read_csv('data_sea.csv', encoding='utf-8')

# Графики для числовых переменных

sns.scatterplot(data=data_file, x='количество', y='сумма')

sns.relplot(data=data_file, x='количество', y='сумма', kind='scatter')

fg = sns.relplot(data=data_file, x='количество', y='сумма', kind='scatter', col='вид товара', hue='магазин')

fg = sns.relplot(data=data_file, x='количество', y='сумма', kind='scatter', size='день недели')

sns.relplot(data=data_file, x='день недели', y='сумма', kind='line')
sns.relplot(data=data_file, x='вид товара', y='количество', kind='line')

sns.displot(data=data_file, x='количество',kind='hist', bins=20)
# #  y='сумма', bins=50 для максимального отображение = количеству строк dataset
sns.displot(data=data_file, x='количество', kind='hist', bins=105, hue='день недели', col='магазин', row='вид товара')

sns.displot(data=data_file, x='количество', kind='kde', hue='магазин', fill=True)

sns.displot(data=data_file, x='количество', y='сумма', cbar=True)


#  hue='магазин'
sns.jointplot(data=data_file, x='количество',  y='сумма',  hue='вид товара')

sns.pairplot(data=data_file, hue='вид товара')

sns.catplot(data=data_file, kind='boxen', x='вид товара', y='количество', hue='магазин', errorbar="sd", palette="dark", alpha=.6, height=6)

sns.catplot(data=data_file, kind='violin', x='вид товара', y='сумма', hue='магазин', errorbar="sd", palette="dark", alpha=.6, height=6)


#  Графики для категориальных переменных

sns.catplot(data=data_file, x='вид товара',  y='сумма',  hue='магазин')

sns.catplot(data=data_file, x='вид товара',  y='количество', kind='box',  hue='магазин')

sns.lmplot(data=data_file, x='количество', y='сумма', hue='вид товара')

# Настройка отображения из стандартных тем, "whitegrid", "darkgrid"

sns.set_style('darkgrid')
sns.lmplot(data=data_file, x='количество', y='сумма', hue='вид товара')



plt.show()

