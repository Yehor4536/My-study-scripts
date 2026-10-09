import pandas as pd
import numpy as np

path = r"C:\Users\egorg\Desktop\data1.csv"
df = pd.read_csv(path)

print("-= COLUMNS =-")
print(df.columns)
print("=====")

print("-= SEASONS(May, November) + ITS N, CONVERSION AND SD =-")
df_season = df["month"].isin(["May", "Nov"])
season_stats = df_season.groupby("month")["Revenue"].agg(["count", "mean", "std"])

print(season_stats)
print("!=====!")

print("-= SEASONSs CI =-")
s_p = season_stats["mean"]
s_n = season_stats["count"]
s_sd = season_stats["std"]
s_se = s_sd / np.sqrt(s_n)

ci_lower = (s_p - 1.96 * s_se) * 100
ci_upper = (s_p + 1.96 * s_se) * 100

print("CI Lower __ :")
print(ci_lower)
print("CI Uppear -- :")
print(ci_upper)
print("*!=====!*")

