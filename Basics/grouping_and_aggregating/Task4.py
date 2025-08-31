'''
Техническое задание:
Аспирант Ростислав изучает метаболом водорослей и получил такую табличку. В ней он записал вид каждой водоросли,
её род (группа, объединяющая близкие виды), группа (ещё одно объединение водорослей в крупные фракции) и концентрации анализируемых веществ.
Помогите Ростиславу найти среднюю концентрацию каждого из веществ в каждом из родов (колонка genus).
'''

import pandas as pd

dataset = pd.read_csv('../docs/algae.csv')
# mean_concentrations = dataset.groupby('genus').aggregate({'sucrose': 'mean', 'alanin': 'mean', 'citrate': 'mean', 'glucose': 'mean', 'oleic_acid': 'mean'})
mean_concentrations = dataset.groupby('genus').mean(numeric_only=True)
print(mean_concentrations)
