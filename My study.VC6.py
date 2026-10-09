import pandas as pd

path = r"C:\Users\egorg\Desktop\2019-Oct.csv"
df = pd.read_csv(path)

print(df.shape)
print("=====")

print(df["event_type"].value_counts())
print("!=====!")

print("-= USER TYPES / USER TYPES COUNT =-")
view_users = set(df[df["event_type"] == "view"]["user_id"])
cart_users = set(df[df["event_type"] == "cart"]["user_id"])
purchase_users = set(df[df["event_type"] == "purchase"]["user_id"])

print("View:", len(view_users))
print("Cart:", len(cart_users))
print("Purchase:", len(purchase_users))
print("*!=====!*")

print("-= USERS =-")
cart_and_purchase = cart_users & purchase_users
view_and_cart = view_users & cart_users

p_purchase_given_cart = len(cart_and_purchase) / len(cart_users)
p_cart_given_view = len(view_and_cart) / len(cart_users)
p_cart_given_purchase = len(cart_and_purchase) / len(purchase_users)

print("P(Cart | View):", p_cart_given_view)
print("P(Purchase | Cart):", p_purchase_given_cart)



