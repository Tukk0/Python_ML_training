'''
Техническое задание:
Используя данные (docs/genome_matrix.csv), представляющие геномные расстояния между видами постройте тепловую карту, чтобы различия было видно наглядно.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('../docs/genome_matrix.csv', index_col=0)
graph = sns.heatmap(data=dataset, cmap='viridis')

plt.savefig('task3_plot')
