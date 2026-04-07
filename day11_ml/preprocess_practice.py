import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df = sns.load_dataset('titanic')
#print(df.head())
#print(df.info())
#print(df.describe()) # 수치형에 대해서만
#print(df.shape)
#print(df.tail())

#print(df.isnull().sum())
#df.drop(['deck', 'embark_town'], axis=1, inplace=True)
#print(df)
#df.dropna(inplace=True)
#print(df)
#print(df['age'].mean())
#print(df['age'].mode())
#print(df['age'].median())

#df['age'] = df['age'].fillna(df['age'].mean(),inplace=True)
#print(df['age'])

#sns.boxplot(x=df['age'])
#plt.show()
#df = df[(df['age'] > 0) & (df['age'] == df['age'].astype(int))]
#print(df.info())

'''
data = {
    'Data' : ['2026-01-01',
        '2026-01-02',
        '2026-01-03',
        '2026-01-04']
}

df = pd.DataFrame(data)
print(df)
df[['Year', 'Month', 'Day']] = df['Data'].str.split('-',expand=True)
print(df)
'''
print(df['fare'])
df['fare'] = df['fare'].apply(lambda x : np.log(x+1) if x > 0 else 0)
print(df['fare'])