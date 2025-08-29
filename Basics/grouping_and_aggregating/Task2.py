'''
Техническое задание:
К нам поступили данные из бухгалтерии о заработках Лупы и Пупы за разные задачи!
Посмотрите у кого из них больше средний заработок в различных категориях (колонка Type) и
укажите исполнителя с большим заработком в каждой из категорий.
'''

import pandas as pd
import numpy as np

acc_data = pd.read_csv('../docs/accountancy.csv')
mean_salaries = acc_data.groupby(['Type', 'Executor'], as_index=False).aggregate({'Salary': 'mean'})
max_mean_salaries = mean_salaries.sort_values(['Type', 'Salary'], ascending = [True, False]).groupby('Type').head(1)
print(max_mean_salaries) # С указанием средних зарплат
print()
print(max_mean_salaries[['Type', 'Executor']]) # Только исполнители в каждой группе
