import pandas as pd
import numpy as np

path = r"C:\Users\egorg\Desktop\data1.csv"
df = pd.read_csv(path)
df.columns = df.columns.str.lower()

print("-= USERS, REVENUE = YES/NO =-")
df["user_rev"] = "no"
df.loc[df["revenue"] == True, "user_rev"] == "yes"
yes_users = df[df["user_rev"] == "yes"]
no_users = df[df["user_rev"] == "no"]

print("YES users(who DID purchase): ")
print(yes_users)
print("YES users(who DID NOT purchase): ")
print(no_users)
print("!=====!")

print("-= USERs DATA AND MEDIAN =-")
df_users = df.groupby("user_rev")["bouncerates"].agg(["mean", "max", "min"])
median_users = df.groupby("user_rev")["pagevalues"].median()

print("DATA: ")
print(df_users)
print("MEDIAN: ")
print(median_users)
print("*!=====!*")

