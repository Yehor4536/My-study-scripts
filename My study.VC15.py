import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

path = r"C:\Users\egorg\Desktop\data1.csv"
df = pd.read_csv(path)

print("-= STATS IN GROUPS(weekend) =-")
stats = df.groupby("Weekend")["Revenue"].agg(["mean", "std", "count"])

conv = stats["mean"]
n = stats["count"]
sd = stats["std"]

print("Statss N:")
print(n)
print("Statss Conversion:")
print(conv)
print("Statss SD:")
print(sd)
print("=====")

print("-= SE AND CI(stats )=-")
se = sd / np.sqrt(n)

ci_lower = (conv - 1.96 * se) * 100
ci_upper = (conv + 1.96 * se) * 100

print("SE:")
print(se)
print("CI Lower:")
print(ci_lower)
print("CI Upper:")
print(ci_upper)
print("!=====!")

print("-= TABLE =-")
table = pd.crosstab(df["Weekend"], df["Revenue"])

print(table)
print("*!=====!*")

print("-= CHI2 TEST AND CRAMERs V =-")
chi2, p, dof, expected = chi2_contingency(table)

cramer_v = np.sqrt(chi2 / (n * min(table.shape)))

print("P: ", p)
print("Chi2: ", chi2)
print("E: ", expected)
print("Cramer V: ", cramer_v)
print("!=====!")