import pandas as pd
import numpy as np

path = r"C:\Users\egorg\Desktop\data1.csv"
df = pd.read_csv(path)
df.columns = df.columns.str.lower()

print("-= COLUMNS =-")
print(df.columns)
print("=====")

print("-= USERS =-")
df["revenue_users"] = np.where(df["revenue"] == True, "is", "isnt")

print(df["revenue_users"])
print("!=====!")

print("-= MEAN TIME ON INF + ADM =-")
page_analysis = df.groupby("revenue")[["administrative_duration", "informational_duration"]].agg(["mean", "std"])


print(page_analysis)
print("*!=====!*")

print("-= SPECIAL DAY INFLUENCE(conv%) =-")
special_data = df.groupby("specialday")["revenue"].agg( lambda x: round((x.sum() / x.count()) * 100, 2))

print(special_data)
print("!=====!")

print("-= DEVICES & WEEKEND CONVERSION=-")
conv_devices = df.groupby("operatingsystems")["revenue"].agg( lambda x: round((x.sum() / x.count()) * 100, 2))
conv_devices_w = df[df["weekend"] == True].groupby("operatingsystems")["revenue"].agg(lambda x: round((x.sum() / x.count()) * 100, 2))

print("Conversion at different devices: ", conv_devices)
print("Conversion at different devices AT weekend: ", conv_devices_w)
print("=====")

print("-= TABLES =-")
pivot_conv = pd.pivot_table(df, values="revenue", index="specialday", columns="weekend", aggfunc="mean")

print(pivot_conv)
print("!=====!")