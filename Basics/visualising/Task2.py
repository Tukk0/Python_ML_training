'''
Техническое задание:
Вам дан датасэт с 2-мя фичами (колонками).
Постройте график распределения точек (наблюдений) в пространстве этих 2-ух переменных (одна из них будет x, а другая - y)
и напишите число кластеров, формируемых наблюдениями.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('../docs/dataset.csv')

plt.scatter(data.iloc[:, 0], data.iloc[:, 1])
plt.savefig('task2_plot.png')

# Видим 3 кластера
