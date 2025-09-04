'''
Техническое задание:
Для датасета ирисов (docs/iris.csv) постройте pairplot и посмотрите на scatter плоты для каждой из пар фичей.
Какая из пар навскидку имеет наибольшую корреляцию?
'''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dataset = pd.read_csv('../docs/iris.csv', index_col=0)
sns.pairplot(dataset, hue = 'species')
plt.savefig('task7_plot')

# Навскидку - petal length и petal width.
# У petal length и sepal length тоже, вероятно, хорошая корреляция
