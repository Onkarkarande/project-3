import pandas as pd
import numpy as np
import io
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn import preprocessing
df=pd.read_csv('aaa.csv')
print(df)
#%%
df.head()
df.describe()
df.corr()
df[df.notnull()]
df.isnull().sum()
df=df.dropna()
df
sns.histplot(df.age)
df.age.mean()
df.age.std()
upper_limit=df.age.mean()+ 3*df.age.std()
lower_limit=df.age.mean()- 3*df.age.std()
df[(df.age>upper_limit) | (df.age<lower_limit)]
df_age=df[(df.age<upper_limit) & (df.age>lower_limit)]
df_age.age.hist()
df['zscore']= (df.age-df.age.mean()) / (df.age.std())
df.zscore
df_zscore=df[(df.zscore>-3) & (df.zscore<3)]
df.zscore
Q1=df.age.quantile(0.25)
Q3=df.age.quantile(0.75)
IQR=Q3-Q1
IQR
upper_limit=Q3 + 1.5*IQR
lower_limit=Q3 - 1.5*IQR
upper_limit
lower_limit
df[(df.age<upper_limit) & (df.age>lower_limit)]
df.age.hist()
df.age
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
df_zscore.age=scaler.fit_transform(df_zscore[['age']])
df_zscore.age
