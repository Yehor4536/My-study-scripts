import pandas as pd
import numpy as np
from scipy import stats

path = r"C:\Users\egorg\Desktop\data1.csv"
df = pd.read_csv(path)
df.columns = df.columns.str.lower()

print("-= COHORTS(month + special day) =-")
cohort_data = df.groupby(["month", "specialday"], observed=False)["productrelated"].mean()

print(cohort_data.head())
print("=====")

print("-= UNSTACKED COHORTS =-")
cohort_matrix = cohort_data.unstack(level="specialday")

print(cohort_matrix.head())
print("!=====!")

print("-= ELASTICITY =-")
e_matrix = cohort_matrix.pct_change(axis=1) * 100

print(e_matrix)
print("And what is this?")
print("*!=====!*")

print("-= MAYs DATA =-")
df_may = df[df["month"] == "May"].copy()
max_views_m = df_may["productrelated"].quantile(0.95)
df_may_clean = df_may[df_may["productrelated"] <= max_views_m].copy()

df_analysis = df_may_clean[df_may_clean["specialday"].isin([0.0, 0.8])]
may_stats = df_analysis.groupby("specialday")["productrelated"].agg(["mean", "count", "std"])

print(may_stats)
print("!=====!")

print("-= N, MEAN, SD AND SE =-")
n = may_stats["count"]
mean = may_stats["mean"]
sd = may_stats["std"]

se = sd / np.sqrt(n)
print("N: ", n)
print("Mean: ", mean)
print("SD: ", sd)
print("SE: ", se)
print("=====")

print("-= CI =-")
ci_lower = mean - 1.96 * se
ci_upper = mean + 1.96 * se

print("CI lower: ")
print(ci_lower)
print("CI upper: ")
print(ci_upper)
print("!=====!")

print("-= CHI2 TEST, GROUPS AND COMPARISON =-")
normal_g = df_analysis[df_analysis["specialday"] == 0.0]["productrelated"]
special_g = df_analysis[df_analysis["specialday"] == 0.8]["productrelated"]

t_stat, p_val = stats.ttest_ind(normal_g, special_g, egual_var=False)

print("NORMAL group: ", normal_g)
print("SPECIAL group: ", special_g)
print("P: ", p_val)
print("*!=====!*")