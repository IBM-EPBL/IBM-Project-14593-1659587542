import math

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn import metrics


def grouping(num):
    return math.ceil(num / 12) * 12


def dictionary(strings):
    dictionary = dict()
    uniques = strings.unique()
    for i in range(len(uniques)):
        dictionary[uniques[i]] = i
    return dictionary


df = pd.read_csv('Crude.csv')
df.Date = df.Date.astype(str)

df[['Month', 'Day','Year']]=df['Date'].str.split('/', expand=True)


df.drop('Date', axis=1, inplace=True)
df = df.dropna()
df.iloc[:, :] = df.iloc[:, :].astype(int)
df.drop_duplicates(inplace = True)


x = df.iloc[:, np.r_[1:4]]
y = df.iloc[:, np.r_[0]]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

for i in df.index:
    df.at[i, 'Value'] = grouping(df.at[i, 'Value'])

w = df.iloc[:, np.r_[1:4]]
z = df.iloc[:, np.r_[0]]
w_train, w_test, z_train, z_test = train_test_split(x, y, test_size=0.20)