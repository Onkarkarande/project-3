import pandas as pd
import numpy as np
import io
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn import preprocessing
dir
df=pd.read_csv('iris.csv')
df.head()
#%%
import statistics
print(f"sepal length mean:{statistics.mean(df['SepalLengthCm'])}")
print(f"sepal width mean:{statistics.mean(df['SepalWidthCm'])}")
print(f"sepal length mean:{statistics.mean(df['PetalLengthCm'])}")
print(f"sepal width mean:{statistics.mean(df['PetalWidthCm'])}")
print(f"sepal lengthmedian:{statistics.median(df['SepalLengthCm'])}")
print(f"sepal width median:{statistics.median(df['SepalWidthCm'])}")
print(f"sepal length median:{statistics.median(df['PetalLengthCm'])}")
print(f"sepal width median:{statistics.median(df['PetalWidthCm'])}")
print(f"sepal length mode:{statistics.mode(df['SepalLengthCm'])}")
print(f"sepal width mode:{statistics.mode(df['SepalWidthCm'])}")
print(f"petal length mode:{statistics.mode(df['PetalLengthCm'])}")
print(f"petal width mode:{statistics.mode(df['PetalWidthCm'])}")
print(f"sepal length standard deviation :{statistics.stdev(df['SepalLengthCm'])}")
print(f"sepal width standard deviation :{statistics.stdev(df['SepalWidthCm'])}")
print(f"petal length standard deviation :{statistics.stdev(df['PetalLengthCm'])}")
print(f"petal length standard deviation :{statistics.stdev(df['PetalWidthCm'])}")
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
sns.heatmap(df.corr(),annot=True)
