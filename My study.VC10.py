import pandas as pd

path = r"C:\Users\egorg\Desktop\data1.csv"
df = pd.read_csv(path)

print(df.columns)
print(df.head())
print("=====")

print("-= HOLIDAY SHOPPERS =-")
holiday_shoppers = df[df["SpecialDay"] > 0.8]

print(holiday_shoppers.head())
print("!=====!")

visitor_stats = df.groupby("VisitorType")[["ProductRelated", "Revenue"]].mean()
print("-= VISITOR STATS =-")

print(visitor_stats.head())
print("*!=====!*")

print("-= NORMAL- AND WEEKEND-USERS =-")
df["Segment"] = "normal_user"
df.loc[(df["productRelated"] > 20) & (df["Weekend"] == True), "Segment"] = "weekend_user"

print("")


