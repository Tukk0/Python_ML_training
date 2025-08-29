'''
Техническое задание:
Сгруппируйте по колонкам attack_type и primary_attr и выберите самый распространённый набор характеристик.
'''

import pandas as pd

dota_dataset = pd.read_csv("../docs/dota_hero_stats.csv")
leader = dota_dataset.groupby(['attack_type', 'primary_attr'], as_index=False).aggregate({'id': 'count'}).sort_values('id', ascending=False).head(1)

print(leader.iloc[0, 0], leader.iloc[0, 1])
