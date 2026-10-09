import pandas as pd

from scipy import stats

path = r"C:\Users\egorg\Desktop\data1.csv"
df = pd.read_csv(path)

print(df.columns)

print("-= VISITOR TYPES =-")
new_v = df[df["VisitorType"] == "New_Visitor"]
return_v = df[df["VisitorType"] == "Returning_Visitor"]

print("New visitors: " + str(new_v))
print("Returning visitors: " +  str(return_v))
print("=====")

print("-= SESSIONS =-")
new_sessions = len(new_v)
return_sessions = len(return_v)

print("New visitors sessions:" + str(new_sessions))
print("Returning visitors sessions:" + str(return_sessions))
print("!=====!")

print("-= VISITOR PURCHASES =-")
new_purchase = len(new_v[new_v["Revenue"] == True])
return_purchase= len(return_v[return_v["Revenue"] == True])

print("New visitor purchases: "  + str(new_purchase))
print("Return visitor purchases: "  + str(return_purchase))
print("*!=====!*")

print("-= CONVERSIONS =-")
new_cr = (new_purchase / new_sessions) * 100
return_cr = (return_purchase / return_sessions) * 100

print("New visitors conversion rate: " + str(round(new_cr, 2)) + "%")
print("Returning visitors conversion rate: " + str(round(return_cr, 2)) + "%")
print("!=====!")

print("-= TABLE =-")
table = pd.crosstab(df["VisitorType"], df["Revenue"])

print(table)
print("=====")

from scipy.stats import chi2_contingency

print("-= CHI-TEST =-")
chi2, p, dof, expected = chi2_contingency(table)

print("Statistics X: ", chi2)
print("P-value: ", p)

if p < 0.05:
    print("There IS a ground to believe that VisitorType related to Revenue...")
else:
    print("There IS NOT a ground to believe that VisitorType related to Revenue...")

print("!=====!")