import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv('abc.csv')
print(df.head())
df=df.drop(['Unnamed: 0'],axis=1)
print(df.head())
print(df.shape)
df.info()
print(df.columns)
x=df[["crim","lstat"]]
print(x)
y=df[["medv"]]
print(y)
print(df.corr())
plt.figure(figsize=(12,6))
print(plt.show())
print(sns.heatmap(df.corr().abs(),annot=True))
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=5)
print("The len of x: ",len(x))
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
print(regression.fit(x_train,y_train))
y_predct=regression.predict(x_test)
print(y_predct)
print("Accuracy of Linear Regression: ",regression.score(x_train,y_train))
from sklearn.metrics import r2_score,mean_squared_error
print(r2_score(y_test,y_predct))
print(np.sqrt(mean_squared_error(y_test, y_predct)))

