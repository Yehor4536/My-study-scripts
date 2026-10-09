import pandas as pd
import numpy as np
from scipy import stats

path = r"C:\Users\egorg\Desktop\data1.csv"
df = pd.read_csv(path)
df.columns = df.columns.str.lower()

print("-= IMPULSIVE AND RATIONAL USERS =-")
df_buyers = df[df["revenue"] == True].copy()
buyer_type = np.where((df["weekend"] == True) & (df["productrelated"] <= 10), "i", "r")

print("R: ", buyer_type["r"].count())
print("I: ", buyer_type["i"].count())
print("=====")

print("-= AGG / MEAN, SD AND N =-")
buyer_stats = df.groupby("buyer_type")["productrelated"].agg(["mean", "count", "std"])
n = buyer_stats["count"]
sd = buyer_stats["std"]
conv = buyer_stats["mean"]

print("N: ", n)
print("Conversion: ", conv)
print("SD: ", sd)
print("!=====!")

print("-= CI AND SE =-")
se = sd / np.sqrt(n)
ci_lower = conv + 1.96 * se
ci_upper = conv - 1.96 * se

print("CI lower: ", ci_lower)
print("CI upper: ", ci_upper)
print("SE: ", se)
print("*!=====!*")

print("-= TABLE =-")
table = pd.crosstab(df["buyer_type"], df["productrelated"])

print(table)
print("!=====!")

print("-= CHI2 TEST =-")
chi2, p, dof, expected = stats.chi2_contingency(table)

print("P: ", p)
print("Expected: ", expected)
print("chi2: ", chi2)
print("=====")

print("-= CRAMERs V =-")
cramer_v = np.sqrt(chi2 / (n * min(table.shape)))

print("Cramers V: ", cramer_v)
print("!=====!")