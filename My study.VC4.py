import pandas as pd

path = r"C:\Users\egorg\Desktop\2019-Oct.csv"

df = pd.read_csv(path)

print(df.columns)
print(df.shape)
print(df.head())
print("=====")

print("-= USER EVENTS =-")
user_events = df.groupby(["user_id", "event_type"]).size().unstack(fill_value=0)
print("I do not understand the (fill_value=0)...")

print("First lines in user_events: ", user_events.head())
print("Described user_events: ", user_events.describe())
print("!=====!")

print("-= USER SESSIONS / PROFILE =-")
user_sessions = df.groupby("user_id")["user_session"].nunique()
user_profile = user_events.copy()
user_profile["sessions"] = user_sessions
print("I do not understand the .copy() comand and how does the line above work...")

print(user_profile.head())
print("*!=====!*")

print("-= TYPES OF USERS IN USER-PROFILE =-")
active_users = user_profile["view"] > 10 
not_active_users = user_profile["view"] <= 3
pur_users = user_profile["purchase"] >= 1

print("ACTIVE users in user_profile: ", len(active_users))
print("NOT ACTIVE users in user_profile: ", len(not_active_users))
print("PURCHASE-users in user_profile: ", len(pur_users))
print("!=====!")

