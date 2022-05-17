import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv("iris.csv")
print(df.head())
#%%
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.columns)
print(df.corr())
x=df.drop(columns="Species",axis="columns")
y=df[["Species"]]
plt.figure(figsize=(12,6))
sns.heatmap(df.corr().abs(),annot=True)
from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
label=lb.fit_transform(df["Species"])
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=1)
print(len(x))
print(len(y))
from sklearn.naive_bayes import GaussianNB
GB=GaussianNB()
ft=GB.fit(x_train, y_train)
y_predict=GB.predict(x_test)
from sklearn.metrics import classification_report,accuracy_score,recall_score,precision_score,confusion_matrix
cm=confusion_matrix(y_test, y_predict)
ac=accuracy_score(y_test, y_predict)
rc=recall_score(y_test, y_predict,average="micro")
pc=precision_score(y_test, y_predict,average="micro")
#r2=r2_score(y_test, y_predict)
cp=classification_report(y_test, y_predict)
print("Confusion Matrix is ",cm)
sns.heatmap(cm,annot=True,cmap="viridis")
print("Accuracy Score is ",ac)
print("Recall Score is ",rc)
print("Precision Score is ",pc)
print("classification_report :",cp)
#print(sns.heatmap(cm,annot=True,cmap="viridis")