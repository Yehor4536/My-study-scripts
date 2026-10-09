import pandas as pd
from scipy import stats
import math

path = r"C:\Users\egorg\Desktop\data1.csv"
df = pd.read_csv(path)

c_r = df.shape
print(len(df))
print(df.columns)
print("c and r: ", c_r)
print("=====")
print("-= TABLE - WEEKEND/REVENUE =-")
weekend_table = pd.crosstab(df["Weekend"], df["Revenue"])

print(weekend_table)
print("Weekend table SHAPE: ", weekend_table.shape)
print("!=====!")

print("-= RATE-TABLE - WEEKEND/REVENUE - ")
weekend_rate = pd.crosstab(df["Weekend"], df["Revenue"], normalize="index")

print(weekend_rate)
print("*!=====!*")

print("-= CHI-TEST =-")
chi2, p, dof, expected = stats.chi2_contingency(weekend_table)

print("The P-value of weekend_table: ", p)
print("The Chi2 of weekend_table: ", chi2)
print("The Expected of weekend_table: ", expected)
print("!=====!")


print("-= CONTRIBUTION =-")
contribution = (weekend_table - expected) ** 2 / expected

print(contribution)
print("TOTAL:", contribution.to_numpy().sum())
print("I do not understand the line above! Especially meaning of ;to_numpy();")
print("=====")

print("-= CRAMERS V =-")
cv = chi2 / (df.shape * (2 - 1))
print("cv: ", cv)
print(math.sqrt(0.00084))