import pandas as pd
import numpy as np
from scipy import stats 
from scipy.stats import chi2_contingency
import math

path = r"C:\Users\egorg\Desktop\data1.csv"
df = pd.read_csv(path)

print(df.columns)
print("=====")

print("-= CONVERSIONS OF V.TYPES =-")
c_conv = df.groupby("VisitorType", observed=False)["Revenue"].mean() * 100

print(c_conv)
print("!=====!")

print("-= =-")
new_conv = c_conv.iloc[0]
return_conv = c_conv.iloc[-1]

print("New: ", new_conv)
print("Return: ", return_conv)
print("*!=====!*")

print("-= TABLE =-")
table = pd.crosstab(df["VisitorType"], df["Revenue"])

print(table)
print("!=====!")

print("-= CHI TEST =-")
chi2, p, dof, expected = chi2_contingency(table)

print("Table P: ", p)
print("Table expected: ", expected)
print("Table chi2: ", chi2)
print("=====")

print("-= CRAMERs V =-")
n = table.sum().sum()
min_cr = min(table.shape) - 1

print("N: ", n)
print("Cramers V:")
print(np.sqrt(chi2 / (n - min_cr)))
print("!=====!")


print("-= SD OF GROUPS =-")
group_sd = df.groupby("VisitorType")["Revenue"].std()

print(group_sd)
print("*!=====!*")

print("-= N OF GROUP=-")
group_n = df.groupby("VisitorType")["Revenue"].count()

print(group_n)
print("!=====!")

print("-= SD + SE OF GROUPS=-")
group_se = group_sd / np.sqrt(group_n)
conv_prop = c_conv / 100

ci_lower = conv_prop - 1.96 * group_se
ci_upper = conv_prop + 1.96 * group_se

print("CI lower(%):")
print(ci_lower * 100)
print("CI upper(%):")
print(ci_upper * 100)
print("=====")


print("-= SEASONS(May, November) + ITS N, CONVERSION AND SD =-")
df_season = df["Month"].isin(["May", "November"])
season_stats = df_season.groupby("Month")["Revenue"].agg(["count", "mean", "std"])

print(season_stats)
print("!=====!")
