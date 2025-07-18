import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("used_cars_data.csv")
print(data.head(10))
print(data.tail(5))
print(data.info())
print(data.nunique())
print(data.isnull().sum())
print((data.isnull().sum()/(len(data)))*100)
data=data.drop(['S.No.'],axis=1)
data.info()
print(data.info())
from datetime import date
date.today().year
data['Car_Age']=date.today().year-data['Year']
data.head()
print(data.head())

# If the car is 2 years old or less
data['Is_Newly_Listed'] = data['Car_Age'].apply(lambda x: 1 if x <= 12 else 0)
print(data.head())

# if the brand is luxury (like Audi, BMW, Mercedes), 0 otherwise
luxury_brands = ['Audi', 'BMW', 'Mercedes', 'Jaguar', 'Land Rover']
data['Is_Luxury_Brand'] = data['Name'].apply(lambda x: 1 if any(brand in x for brand in luxury_brands) else 0)
print(data.head())

data['Brand']=data.Name.str.split().str.get(0)
data['Model']=data.Name.str.split().str.get(1)+data.Name.str.split().str.get(2)
print(data[['Name','Brand','Model']])
print(data.Brand.unique())
print(data.Brand.nunique())

searchfor = ['Isuzu' ,'ISUZU','Mini','Land']
data[data.Brand.str.contains('|'.join(searchfor))].head(5)
print(data.head())

data["Brand"].replace({"ISUZU": "Isuzu", "Mini": "Mini Cooper","Land":"Land Rover"}, inplace=True)
print(data.head())

data.describe().T
data.describe(include='all').T
cat_cols=data.select_dtypes(include=['object']).columns
num_cols = data.select_dtypes(include=np.number).columns.tolist()
print("Categorical Variables:")
print(cat_cols)
print("Numerical Variables:")
print(num_cols)


