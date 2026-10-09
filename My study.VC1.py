import pandas as pd

from scipy import stats

path = r"C:\Users\egorg\Desktop\data1.csv"

df = pd.read_csv(path)

print(df.head())
print("=====")

print(df.shape)
print("!=====!")

print(df.columns)
print("*!=====!*")

print("-= SESSIONS QUANTITY =-")
New_v = df[df["VisitorType"] == "New_Visitor"]
Returned_v = df[df["VisitorType"] == "Returning_Visitor"]
print("-= VISITOR SESSIONS =-")
print(df.groupby("VisitorType")["ProductRelated"].sum())
print("!=====!")

print("-= VISITOR PURCHASES =-")
print(df.groupby("VisitorType")["Revenue"].sum())
print("=====")

print("-= CONVERSION OF VIS.TYPES =-")
print()
print("-= EVERY SESSIONS =-")
E_s = df[df["ProductRelated"] >= 0]
print(E_s)
print("!=====!")

print("-= SESSIONS > 5 =-")
P_5 = df[df["ProductRelated"] >= 5]
print(P_5)
print("=====")

print("-= SESSIONS > 10 =-")
P_10 = df[df["ProductRelated"] >= 10]
print(P_10)
print("!=====!")

print("-= REVENUE/CUSTOMERS =-")
revenue_users = df[df["Revenue"] == True]
print(revenue_users)
print("*!=====!*")

print("==-= FUNNEL AND STAGES =-==")
print("- STAGE 1 TO 2 -")
print(P_5 / E_s * 100, "%")
print("===")

print("- STAGE 2 TO 3 -")
print(P_10 / P_5 * 100, "%")
print("!===!")

print("- STAGE 3 TO 4 -")
print(revenue_users / P_10 * 100, "%")
print("*!===!*")

print("-= AVERAGE CONVERSION FROM STAGE 1 TO LAST =-")
print(revenue_users / E_s * 100, "%")
print("=====")