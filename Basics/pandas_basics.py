'''
Техническое задание:
Загрузить датасет о пассажирах "Титаника",
вывести число колонок и строк.
Ответить, сколько колонок имеют типы float, int, object
'''

import pandas as pd

titanic_dataset = pd.read_csv('docs/titanic.csv')
print('Число колонок - ', titanic_dataset.shape[1])
print('Число строк - ', titanic_dataset.shape[0])
print('Число колонок типа float - ', titanic_dataset.select_dtypes(include='float').shape[1])
print('Число колонок типа int - ', titanic_dataset.select_dtypes(include='int').shape[1])
print('Число колонок типа object - ', titanic_dataset.select_dtypes(include='object').shape[1])
# Информация также есть в titanic_dataset.info()
