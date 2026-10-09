import pandas as pd
import numpy as np
from scipy import stats
import math

path = r"C:\Users\egorg\Desktop\data1.csv"
df = pd.read_csv(path)

print(df.columns)
print(df.head())
print("=====")

print("-= HOLIDAY SHOPPERS =-")
holiday_shoppers = df[df["SpecialDay"] > 0.8]

print(holiday_shoppers.head())
print("!=====!")

print("-= VISITOR STATS =-")
visitor_stats = df.groupby("VisitorType")[["ProductRelated", "Revenue"]].mean()

print(visitor_stats.head())
print("*!=====!*")

print("-= NORMAL- AND WEEKEND-USERS =-")
df["Segment"] = "normal_user"
df.loc[(df["ProductRelated"] > 20) & (df["Weekend"] == True), "Segment"] = "weekend_user"

print(df["Segment"].head())
print("!=====!")

print("-= COLUMN is_holiday =-")
df["is_holiday"] = np.where(df["SpecialDay"] > 0, 1, 0)

print(df["is_holiday"].head())
print("=====")

print("-= TABLE AND CONVERSIONS IN THE TABLE =-")
table = pd.crosstab(df["is_holiday"], df["Revenue"])
o_con = 1831 / (9248 + 1831) * 100
I_con = 77 / (1174 + 77) * 100

print("Table: ")
print(table)
print("0; No holiday conversion: ", o_con)
print("1; IS holiday conversion: ", I_con)
print("!=====!")

print("-= X, EXPECTED AND CRAMERS V(table) =-")
chi2, p, dof, expected = stats.chi2_contingency(table)

print("Table Chi2/X: ", chi2)
print("Table P-value: ", p)
print("Table Expected: ", expected)
print("=====")

print("-= SD =-")
sd = df.groupby("is_holiday")["Revenue"].std()
print("!=====!")