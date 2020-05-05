#!/usr/bin/python
# -*- coding: UTF-8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('winemag-data-130k-v2.csv')
缺失值个数
total = dataset.isnull().sum().sort_values(ascending=False)
# print(total)
# 标称属性频数
country_set = dataset['country'].value_counts()
province_set = dataset['province'].value_counts()
region_1_set = dataset['region_1'].value_counts()
region_2_set = dataset['region_2'].value_counts()

points_mean = dataset['points'].mean()
# 五数概括
points_min = dataset['points'].min()
points_q1 = np.percentile(dataset['points'], 25)
points_median = dataset['points'].median()
points_q3 = np.percentile(dataset['points'], 75)
points_max = dataset['points'].max()


price_min = dataset['price'].min()
price_q1 = np.percentile(dataset['price'], 25)
price_q1 = dataset['price'].quantile(0.25)
price_median = dataset['price'].median()
price_q3 = dataset['price'].quantile(0.75)
price_max = dataset['price'].max()




dataset = dataset.drop(dataset[dataset['price'].isnull()].index)
# dataset['price'] = dataset['price'].fillna(dataset['price'].mode().iloc[0])
print(dataset['price'])
plt.boxplot(dataset['price'])
plt.ylabel("price")
plt.xlabel("boxplot")



