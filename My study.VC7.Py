import pandas as pd

path = r"C:\Users\egorg\Desktop\2019-Oct.csv"
df = pd.read_csv(path)

print(df.columns)
print("=====")

print("-= DESCRIBED PRICE =-")
print(df["price"].describe())
print("!=====!")

price_median = df["price"].median()
print("MEDIAN Price: ", price_median)
df["price_group"] = "low"
df.loc[df["price"] > 30, "price_group"] = "high"
print("I did not understand the line above.")
print(df["price_group"].value_counts())
print("*!=====!*")

print("-= UNIQUE USERS =-")
low_view = df[(df["price_group"] == "low") & (df["event_type"] == "view")]["user_id"].nunique()
high_view = df[(df["price_group"] == "high") & (df["event_type"] == "view")]["user_id"].nunique()
low_cart = df[(df["price_group"] == "low") & (df["event_type"] == "cart")]["user_id"].nunique()
high_cart = df[(df["price_group"] == "high") & (df["event_type"] == "cart")]["user_id"].nunique()

print("The low_view: ", low_view)
print("The low_cart: ", low_cart)
print("The high_view: ", high_view)
print("The high_cart: ", high_cart)
print("!=====!")

print("-= CONVERSIONS =-")
low_con = low_cart / low_view
high_con = high_cart / high_view

print("Low conversion(view - cart): ", low_con)
print("High_conversion[view - cart): ", high_con)
print("=====")


print("-= LOW/HIGH == PURCHASE =-")
low_pur = df[(df["price_group"] == "low") & (df["price"] == True)]["user_id"].nunique()
high_pur = df[(df["price_group"] == "high") & (df["price"] == True)]["user_id"].nunique()

print("LOW-users, who did purchase: ", low_pur)
print("HIGH-users, who did purchase: ", high_pur)