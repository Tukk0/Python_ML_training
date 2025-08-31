'''
Техническое задание:
Пользуясь предыдущими данными (docs/algae.csv), укажите через пробел (без запятых) чему равны минимальная,
средняя и максимальная концентрации аланина (alanin) среди видов рода Fucus.
Округлите до 2-ого знака, десятичным разделителем является точка.
'''

import pandas as pd

dataset = pd.read_csv('../docs/algae.csv')
grouped_data = dataset.groupby('genus')
min = grouped_data.aggregate('min', 'alanin')
mean = grouped_data.aggregate('mean', 'alanin')
max = grouped_data.aggregate('max', 'alanin')

print(round(min.loc['Fucus', 'alanin'], 2), round(mean.loc['Fucus', 'alanin'], 2), round(max.loc['Fucus', 'alanin'], 2))
