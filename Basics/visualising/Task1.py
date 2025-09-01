'''
Техническое задание.
Используя библиотеки seaborn и myplotlib,
укажите способы нарисовать график зависимости зарплаты от даты.
(Файл - income.csv)
'''

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../docs/income.csv')
df.plot()
# Возможные варианты:
# df.income.plot()
# sns.lineplot(data=df)
# sns.lineplot(x=df.index, y=df.income)
# plt.plot(df.index, df.income)
