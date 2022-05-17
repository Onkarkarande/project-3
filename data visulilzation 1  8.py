import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
df=sns.load_dataset('titanic')
print(df.head())
sns.distplot(df["fare"])
sns.jointplot(x="age",y="fare",data=df)
sns.pairplot(data=df)
sns.barplot(x="sex",y="age",data=df)
sns.boxplot(x="sex",y="age",data=df)
sns.violinplot(x="sex",y="age",data=df)
sns.distplot(df["age"],kde=False,bins=10)
sns.countplot(x="sex",data=df)
