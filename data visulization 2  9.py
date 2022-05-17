import pandas as pd
import numpy as np
import io
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn import preprocessing
df=sns.load_dataset("titanic")
df.head()
#%%
df.isnull().sum()
sns.catplot(x ="sex", hue ="survived",kind ="count", data=df)
sns.catplot(x="embarked",hue="survived",kind="count",col="pclass",data=df)
group=df.groupby(['pclass',"survived"])
pclass_survived=group.size().unstack()
sns.heatmap(pclass_survived,annot=True,fmt="d")
df["Fare_Range"]=pd.qcut(df["fare"],4)
sns.barplot(x="Fare_Range",y="survived",data=df)
