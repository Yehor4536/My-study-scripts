import pandas as pd
import numpy as np
#Importing data...
path = r"C:\Users\egorg\Desktop\2019-Oct.csv"
df = pd.read_csv(path)
#Columns and first lines...
print("-= COLUMNS + LINES =-")
print(df.columns)
print(df.head())
print("=====")
#New column...
print("-= REVENUE COLUMN =-")
df["revenue"] = np.where(df["event_type"] == "purchase", df["price"], 0)

print("Revenue: ", df["revenue"].sum())
print("!=====!")
#Actions(event type)...
print("-= EVENT TYPES CALCULATING =-")
view_sum = df[df["event_type"] == "view"].shape[0]
cart_sum = df[df["event_type"] == "cart"].shape[0]
purchase_sum = df[df["event_type"] == "purchase"].shape[0]
remove_cart_sum = df[df["event_type"] == "remove_from_cart"].shape[0]

print("VIEWS: ", view_sum)
print("CARTS: ", cart_sum)
print("PURCHASES: ", purchase_sum)
print("REMOVE FROM CART ", remove_cart_sum)
print("*!=====!*")
#Event conversions...
print("-= EVENT CONVERSIONS =-")
view_cart = cart_sum / view_sum if view_sum > 0 else 0
cart_purchase = purchase_sum / cart_sum if cart_sum > 0 else 0
view_purchase = purchase_sum / view_sum if view_sum > 0 else 0
remove_cart_cart = remove_cart_sum / cart_sum if cart_sum > 0 else 0

print("VIEW_CART conversion: ", view_cart)
print("CART-PURCHASE conversion: ", cart_purchase)
print("PURCHASE-VIEW conversion: ", view_purchase)
print("CART-REMOVE FROM CART conversion", remove_cart_cart)
print("!=====!")
#Most popular brands and so on...
print("-= POPULAR BRENDS =-")
cart = df[df["event_type"] == "cart"]
pop_brand_cart = cart["brand"].value_counts(dropna=False)
lost_items = df[df["event_type"] == "remove_from_cart"]
pop_brand_cart_lost = lost_items["brand"].value_counts(dropna=False)

print("Top 5 most popular brands added to cart: ")
print(pop_brand_cart.head())
print("Top 5 brands, where it added to cart, but was not revenue or the user removed the brand from cart: ")
print(pop_brand_cart_lost.head())
print("=====")
#Lost profit...
print("-= LOST PROFIT =-")
lost_profit = df[df["event_type"] == "remove_from_cart"]["price"].sum()

print(lost_profit)
print("!=====!")