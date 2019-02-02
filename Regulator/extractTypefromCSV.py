# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import pandas as pd

df = pd.read_csv('result.csv')
typeTable = open("type.csv", 'wb')
typeTable.write('No,Type')
typeFea =  df['Type'].tolist()
typeCount = 1
typeDict = dict()
for fea in typeFea:
    if fea not in typeDict:
        typeDict[fea] = typeCount
        typeTable.write(str(typeCount) + ',')
        typeTable.write(fea)
        typeTable.write('\n')
        typeCount = typeCount + 1
df['NewType'] = df['Type'].apply(lambda x: typeDict[x])
df = df.drop(columns=['Type'])
df.to_csv('modifResult.csv')