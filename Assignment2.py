import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from pandas.core.common import random_state
from sklearn.linear_model import LinearRegression
# Get dataset
df_sal = pd.read_csv('Salary_Data.csv')
df_sal.head()
print(df_sal.head())
# Describe data
df_sal.describe()
print(df_sal.describe())
plt.title('Salary Distribution Plot')
sns.distplot(df_sal['Salary'])
plt.show()
