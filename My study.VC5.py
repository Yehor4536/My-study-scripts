import pandas as pd
from scipy import stats
import math

path = r"C:\Users\egorg\Desktop\data1.csv"
df = pd.read_csv(path)

print("-= TABLE =-")
table = pd.crosstab(df["VisitorType"], df["Revenue"])

print(table)
print("=====")
chi2, p, dof, expected = stats.chi2_contingency(table)

print("Chi2: ", chi2)
print("P-value: ", p)
print("Expected: ", expected)
print("!=====!")

print("-= TABLE RATE =-")
table_rate = pd.crosstab(df["VisitorType"], df["Revenue"], normalize="index")

print(table_rate)
print("Table SHAPE: ", table.shape)
print(len(df))
print("*!=====!*")

print("-= CRAMERS V / CONVERSIONS")

print("Cramers V: ", 0.104, "(I calculated it myself, just as you said)")
print("The difference of the conversions: 6,1 p.p(I learn it from the results)")
