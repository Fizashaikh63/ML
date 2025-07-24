import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Pie chart
data = pd.read_csv("used_cars_data.csv")
print(data.info())
Locationn = data['Location'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(Locationn, labels=Locationn.index, autopct='%1.1f%%', startangle=90, shadow=True )
plt.title('Distribution of Cars in terms of location')
plt.show()
#Bar chart
data = pd.read_csv("used_cars_data.csv")
car_name=data['Name'].head(3)
Fuel_type=data['Fuel_Type'].head(3)
plt.figure(figsize=(12, 6))
plt.bar(car_name,Fuel_type,color='green')
plt.xlabel("car_name")
plt.ylabel("Fuel_type")
plt.title("carname vs fuel fuel type")
plt.show()

#histogram
data = pd.read_csv("used_cars_data.csv")
prices = data['Price'].head(10)
plt.figure(figsize=(10, 5))
plt.hist(prices, bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Price (in Lakhs)")
plt.ylabel("Number of Cars")
plt.title("Distribution of Car Prices")
plt.grid(True)
plt.show()

#Box plot

data = pd.read_csv("used_cars_data.csv")
columns_to_plot = ['Kilometers_Driven', 'Price', 'Seats']
plt.figure(figsize=(10, 6))
plt.boxplot([data[col].dropna() for col in columns_to_plot], patch_artist=True, labels=columns_to_plot)

plt.title("Box Plot of Kilometers Driven, Price, and Seats")
plt.ylabel("Values")
plt.grid(True)
plt.show()

#EDA Bivariate Analysis

# Load your dataset
data = pd.read_csv("used_cars_data.csv")

# Extract Brand and Model from 'Name'
data['Brand'] = data['Name'].apply(lambda x: str(x).split()[0])
data['Model'] = data['Name'].apply(lambda x: ' '.join(str(x).split()[1:3]))

# Create subplots: 3 rows x 2 columns
fig, axs = plt.subplots(3, 2, figsize=(15, 12))
fig.tight_layout(pad=5)

# 1. Location vs Price
location_price = data.groupby('Location')['Price'].mean().sort_values(ascending=False)[:10]
axs[0, 0].bar(location_price.index, location_price.values, color='skyblue')
axs[0, 0].set_title("Location vs Price")
axs[0, 0].set_xticklabels(location_price.index, rotation=45)

# 2. Transmission vs Price
trans_price = data.groupby('Transmission')['Price'].mean()
axs[0, 1].bar(trans_price.index, trans_price.values, color='orange')
axs[0, 1].set_title("Transmission vs Price")

# 3. Fuel_Type vs Price
fuel_price = data.groupby('Fuel_Type')['Price'].mean()
axs[1, 0].bar(fuel_price.index, fuel_price.values, color='green')
axs[1, 0].set_title("Fuel Type vs Price")

# 4. Owner_Type vs Price
owner_price = data.groupby('Owner_Type')['Price'].mean()
axs[1, 1].bar(owner_price.index, owner_price.values, color='purple')
axs[1, 1].set_title("Owner Type vs Price")

# 5. Brand vs Price (Top 10 Brands)
brand_price = data.groupby('Brand')['Price'].mean().sort_values(ascending=False)[:10]
axs[2, 0].bar(brand_price.index, brand_price.values, color='red')
axs[2, 0].set_title("Brand vs Price")
axs[2, 0].set_xticklabels(brand_price.index, rotation=45)

# 6. Model vs Price (Top 10 Models)
model_price = data.groupby('Model')['Price'].mean().sort_values(ascending=False)[:10]
axs[2, 1].bar(model_price.index, model_price.values, color='teal')
axs[2, 1].set_title("Model vs Price")
axs[2, 1].set_xticklabels(model_price.index, rotation=45)

# Show all plots
plt.show()