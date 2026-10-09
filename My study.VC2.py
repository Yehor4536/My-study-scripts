import pandas as pd

path = r"C:\Users\egorg\Desktop\2019-Oct.csv"

df = pd.read_csv(path)

print(df.head())
print("=====")

print(df.shape)
print("!=====!")

print(df.columns)
print("*!=====!*")

print("-= EACH VALUE IN E.TYPE =-")
print(df["event_type"].value_counts())
print("!=====!")

views = df[df["event_type"] == "view"]["user_id"].nunique()
print("-= VIEWS =-")
print(views)
print("*!=====!*")

carts = df[df["event_type"] == "cart"]["user_id"].nunique()
print("-= CARTS =-")
print(carts)
print("!=====!")

purchases = df[df["event_type"] == "purchase"]["user_id"].nunique()
print("-= PURCHASES =-")
print(purchases)
print("=====")

view_to_cart = carts / views
cart_to_purchase = purchases / carts
print("-= VIEW TO CART =-")
print(view_to_cart * 100)
print("!=====!")

print("-= CART TO PURCHASE =-")
print(cart_to_purchase * 100)
print("*!=====!*")


print("-= CONVERSION VIEW TO CART / CART TO PURCHASE =-")
v_c_con = carts / views 
c_p_con = purchases / carts 

print("View to Cart: " + str(v_c_con))
print("View to Cart %: " + str(v_c_con * 100))
print("Cart to Purchase: " + str(c_p_con))
print("Cart to Purchase %: " + str(c_p_con * 100))
print("=====")

print("-= ABSOLUTE LOSS: VIEW-CART / CART-PURCHASE =-")
A_v_c_loss = views - carts 
A_c_p_loss = carts - purchases

print("Absolute loss View to Cart: " + str(A_v_c_loss))
print("Absolute loss Cart to Purchase: " + str(A_c_p_loss))
print("!=====!")

print("-= OVERALL VIEW TO PURCHASE =-")
O_v_p = view_to_cart * cart_to_purchase
print("Ovarall View to Purchase: " + str(O_v_p))
print("Ovarall View to Purchase %: " + str(O_v_p * 100))
print("*!=====!*")

print("-= DROP OFF: VIEW-CART / CART-PURCHASE =-")
DO_v_c = 1 - v_c_con
DO_c_p = 1 - c_p_con

print("Drop off View to Cart: " + str(DO_v_c))
print("Drop off Cart to Purchase: " + str(DO_c_p))
print("!=====!")

print("-= V/C/P USERS =-")
v_users = set(df[df["event_type"] == "view"]["user_id"])
c_users = set(df[df["event_type"] == "cart"]["user_id"])
p_users = set(df[df["event_type"] == "purchase"]["user_id"])

print("View users: " + str(v_users))
print("Cart users: " + str(c_users))
print("Purchase users: " + str(p_users))
print("=====")

print("-= VIEW AND CART / CART AND PURCHASE =-")
v_and_c = v_users & c_users
c_and_p = c_users & p_users 

print("View and Cart: " + str(v_and_c))
print("Cart and Purchase: " + str(c_and_p))
print("!=====!")

