import pandas as pd
import numpy as np

path = r"C:\Users\egorg\Desktop\data1.csv"
df = pd.read_csv(path)

print("-= BINS =-")
df["product_bins"] = pd.cut(df["ProductRelated"], bins=4)

print(df["product_bins"].value_counts())
print("=====")

print("-= BINS; LABELS AND CLEAN DATA =-")
max_normal_views = df["ProductRelated"].quantile(0.95)
df_clean = df[df["ProductRelated"] <= max_normal_views].copy()

custom_bins = [0, 10, 30, 60, float("inf")]
custom_labels = ["0-10 (Low interest)", "10-30 (Optimal interest)", "30-60 (High interest)", "60+ (Analysiss paralises)"]

df_clean["behaviour_tier"] = pd.cut(df_clean["ProductRelated"], bins=custom_bins, labels=custom_labels)
print("!=====!")

print("-= CONVERSION BY TIERs =-")
conversion_by_tiers = df_clean.groupby("behaviour_tier", observed=False)["Revenue"].mean() * 100

print(conversion_by_tiers)
print("*!=====!*")

print("-= ILOC AND SO ON =-")
F_group_conv = conversion_by_tiers.iloc[0]
L_group_conv = conversion_by_tiers.iloc[-1]

print("FIRST group(0): ")
print(F_group_conv)
print("SECOND group(-1): ")
print(L_group_conv)
print("!=====!")

print("-= CORRELATION =-")
correlation = df_clean["ProductRelated"].corr(df_clean["Revenue"])
print(correlation)
print("=====")