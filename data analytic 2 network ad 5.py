import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv()
print(df.head())
print(df.info)
print(df.describe())
print(df.shape)
print(df.columns)
x=df[["Age","EstimatedSalary"]]
print(x)
y=df[["Purchased"]]
print(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=(1))
print(len(x))
print(len(y))
print(len(x_train))
print(len(x_test))
print(len(y_train))
print(len(y_test))
from sklearn.linear_model import LogisticRegression
regression=LogisticRegression()
rg= regression.fit(x_train,y_train)
y_predct=regression.predict(x_test)
print(y_predct)
from sklearn.metrics import confusion_matrix,accuracy_score,recall_score,precision_score,classification_report
cm=confusion_matrix(y_test, y_predct)
print(cm)
print("accuracy score is:",accuracy_score(y_test, y_predct))
print("recall score is: ",recall_score(y_test, y_predct))
print("precision_score is :",precision_score(y_test, y_predct))
print("Classification Report :",classification_report(y_test, y_predct))


