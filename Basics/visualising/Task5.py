'''
Техническое задание:
Используя датасэт со значениями параметров ирисов (docs/iris.csv), постройте их распределения и отметьте правильные утверждения, глядя на график.
1) Petal width и petal length имеют бимодальное распределение
2) Petal width и petal length имеют унимодальное распределение
3) Sepal width и sepal length имеют бимодальное распределение
4) Petal length имеет наибольший размах значений
5) Sepal width и sepal length имеют унимодальное распределение
'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dataset = pd.read_csv("../docs/iris.csv", index_col=0)
for column in dataset:
	sns.displot(dataset[column], discrete=True)
	plt.savefig('task5_plot_{}'.format(column))
# Верны 1, 4, 5
