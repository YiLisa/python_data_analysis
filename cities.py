#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:11:00 2018

@author: yi
"""

import pandas as pd

df1 = pd.read_excel('/Users/yi/allcity.xlsx')
print(df1.head(5))
df2 = pd.read_excel('/Users/yi/city_2018.xlsx')
print(df2.head(5))
df2['市'] = df2['市'].apply(lambda x:x.strip())

city = pd.merge(df1,df2,on='市', how='left').drop('省_y',axis = 1).fillna(-1)

print(city.head(15))
print(city.tail(10))
writer = pd.ExcelWriter('cities.xlsx')
city.to_excel(writer,'Sheet 1')
writer.save()
