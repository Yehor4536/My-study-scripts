import os
import pandas as pd
import numpy as np
import kagglehub

f_path = kagglehub.dataset_download("ulrikthygepedersen/online-retail-dataset")
path = os.path.join(f_path, "online_retail.csv")
df = pd.read_csv(path)
# Import dataset...
print("-= COLUMNS =-")
print(df.columns)
print("=====")
# First lines...
print("-= HEAD =-")
print(df.head())
print("!=====!")
# Data cleaning...
print("-= CLEAN DATA =-")
df_clean = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)].copy()

print(df_clean.head())
print("*!=====!*")
# Total revenue...
print("-= TOTAL SUM + REVENUE =-")
total = df_clean["Quantity"] * df_clean["UnitPrice"]

print("Total revenue: ", sum(total))
print("!=====!")

# Popular purchases...
print("-= POP-PURCHASES =-")
df_product = df_clean.groupby("Description")["Quantity"].sum()

print("Most popular products: ")
print(df_product.sort_values(ascending=False).head())
print("=====")

# Orders in countries...
print("-= ORDERS(countries) =-")
orders = df.groupby("Country")["InvoiceNo"].nunique()

print(orders.sort_values())
print("!=====!")

