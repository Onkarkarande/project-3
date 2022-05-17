import pandas as pd
from sklearn import preprocessing
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv('aaa.csv')
print(df.head())
#%%
x=df[['Id']].values.astype(float)
min_max_scaler=preprocessing.MinMaxScaler()
x_scaled=min_max_scaler.fit_transform(x)
df_normalized=pd.DataFrame(x_scaled)
df_normalized
#%%
df['Species'].unique()
label_encoder=preprocessing.LabelEncoder()
df['Species']=label_encoder.fit_transform(df['Species'])
df['Species'].unique()
feature_df=df.drop(columns=['Species'])
one_hot_df=pd.get_dummies(df,prefix='Species',columns=["Species"],drop_first=False)
one_hot_df
print(df.describe())
df.isnull().sum()
df.isnull().any()
df.dtypes
