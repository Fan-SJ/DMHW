#!/usr/bin/python
# -*- coding: UTF-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#
dataset1 = pd.read_csv('records-for-2011.csv')
dataset2 = pd.read_csv('records-for-2012.csv')
dataset3 = pd.read_csv('records-for-2013.csv')
dataset4 = pd.read_csv('records-for-2014.csv')
dataset5 = pd.read_csv('records-for-2015.csv')
dataset6 = pd.read_csv('records-for-2016.csv')

dataset = pd.concat([dataset1, dataset2, dataset3, dataset4, dataset5, dataset6], axis=0, join='inner')
# print(dataset.columns)

# 缺失值个数
total = dataset.isnull().sum().sort_values(ascending=False)
# 标称属性频数
agency_set = dataset['Agency'].value_counts()
beat_set = dataset['Beat'].value_counts()
incident_type_id_set = dataset['Incident Type Id'].value_counts()
incident_type_description = dataset['Incident Type Description'].value_counts()



# dataset = dataset.drop(dataset[dataset['Beat'].isnull()].index)
# dataset['Beat'] = dataset['Beat'].fillna(dataset['Beat'].mode().iloc[0])
beat_set = dataset['Beat'].value_counts()
# dataset['price'] = dataset['price'].fillna(dataset['price'].mode().iloc[0])
print(beat_set.index)

plt.figure(figsize=(6, 8))
plt.barh(beat_set.index,beat_set, height=0.5)
plt.title('Beat Number')
plt.xlabel('number')
plt.ylabel('beat')

plt.show()



