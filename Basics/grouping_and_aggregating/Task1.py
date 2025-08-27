'''
Техническое задание:
Сгруппируйте героев из датасэта по числу их ног и выведите число героев с 0, 2, 4, 6, 8 ногами.
'''

import pandas as pd

dota_dataset = pd.read_csv("../docs/dota_hero_stats.csv")
legs_count = dota_dataset.groupby('legs').count().id.sort_index(ascending=True).values
print('0 legs - ', legs_count[0])
print('2 legs - ', legs_count[1])
print('4 legs - ', legs_count[2])
print('6 legs - ', legs_count[3])
print('8 legs - ', legs_count[4])
#print(dota_dataset)
