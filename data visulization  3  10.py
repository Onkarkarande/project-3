import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
df=pd.read_csv('iris.csv',header=None)
df.columns=["col1","col2","col3","col4","col5","col6"]
df.head()
#%%
column=len(list(df))
column
df.info()
np.unique(df["col6"])
df.describe()
#%%
fig,axes=plt.subplots(2,2,figsize=(16,8))
axes[0,0].set_title("distribution of first column")
axes[0,0].hist(df["col1"]);
axes[0,1].set_title("distribution of second column")
axes[0,1].hist(df["col2"]);
axes[1,0].set_title("distribution of Third column")
axes[1,0].hist(df["col3"]);
axes[1,1].set_title("distribution of fourth column")
axes[1,1].hist(df["col4"]);
#%%
data_to_plot=[df["col1"],df["col2"],[df["col3"],df["col4"]
sns.set_style("whitegrid")
fig.plt.figure(1,figsize=(12,8))  
ax= fig.add_subplot(111)
bp=ax.boxplot(data_plot);                                  
