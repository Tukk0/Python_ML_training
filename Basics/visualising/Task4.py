'''
Техническое задание:
Используя датасэт с данными о героях из игры dota 2 (docs/dota_hero_stats.csv) посмотрите на распределение их возможных ролей в игре (колонка roles).
Постройте гистограмму, отражающую скольким героям сколько ролей приписывается и напишите какое число ролей у большинства героев.
'''
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset = pd.read_csv('../docs/dota_hero_stats.csv')
dataset['roles_count'] = dataset['roles'].apply(lambda x: x.count(',') + 1)
sns.displot(dataset, x='roles_count', discrete=True)
plt.savefig('task4_plot')
