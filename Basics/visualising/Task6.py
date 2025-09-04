'''
Техническое задание:
Нарисуйте распределение длины лепестков ирисов из предыдущего датасэта с помощью violin плота.
'''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dataset = pd.read_csv('../docs/iris.csv')

sns.violinplot(y = dataset['petal length'])
#print(dataset)
plt.savefig('task6_plot')
