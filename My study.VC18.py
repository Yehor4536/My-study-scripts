import pandas as pd
import numpy as np

path = r"C:\Users\egorg\Desktop\data1.csv"
df = pd.read_csv(path)
df.columns = df.columns.str.lower()

print("-= COLUMNS =-")
print(df.columns)
print("=====")

print("-= USERS =-")
df["purchases"] = np.where(df["revenue"] == True, "is_r", "is_not_r")
information = df.groupby("purchases")["productrelated_duration"].agg(["mean", "median"])

print("Users: ", df["purchases"].count)
print("Information: ", information)
print("!=====!")