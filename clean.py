import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("food_coded.csv")
# Handle missing values
# Fill numerical columns with their mean, median, and mode
num = df.select_dtypes(include=['float64', 'int64']).columns
print(df)
df.info()
df.isnull().sum().head(60)

for n in num:
    if df[n].isnull().sum() > 0:
        df[n] = df[n].fillna(df[n].mean()).inplace=True
       # df[n + '_median'] = df[n].fillna(df[n].median())
        #df[n + '_mode'] = df[n].fillna(df[n].mode()[0])

# Fill categorical columns with the mode value
car = df.select_dtypes(include=['object']).columns

for c in car:
    if df[c].isnull().sum() > 0:
        df[c].fillna(df[c].mode,inplace=True)

# Remove duplicate columns
df = df.loc[:, ~df.columns.duplicated()]

# Remove original columns after imputation
df_cleaned = df.drop(columns=num.to_list() + car.to_list())
df.drop(['comfort_food_reasons_coded.1','comfort_food_reasons_coded','eating_changes_coded1'],axis=1,inplace=True)
print("this is final data ")
print(df)
df.isnull().sum().head(60)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
