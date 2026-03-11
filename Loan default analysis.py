import pandas as pd 
from sklearn.datasets import fetch_openml
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind
import seaborn as sns
import matplotlib.pyplot as plt

#load dataset
data = fetch_openml("credit-g", version=1, as_frame=True)
df = data.frame
print("Loaded! Shape:", df.shape)
print(df.head())
print(df.columns)
print(df.info())

#target variable distribution 
print(df["class"].value_counts())

#employment vs loan default 
print(pd.crosstab(df["employment"], df["class"]))
print(pd.crosstab(df["employment"], df["class"], normalize="index"))


cont_table = pd.crosstab(df["employment"], df["class"])
chi2, p, dof, expected = chi2_contingency(cont_table)

print("Chi-square statistic:", chi2)
print("Degrees of freedom:", dof)
print("P-value:", p)

employment_rates = pd.crosstab(df["employment"], df["class"], normalize="index")
employment_risk = (employment_rates["bad"] * 100).sort_values(ascending=False)
print("\n Employment Default Risk Ranking (%)")
print(employment_risk)

#checking status vs loan default
print(pd.crosstab(df["checking_status"], df["class"]))
print(pd.crosstab(df["checking_status"], df["class"], normalize="index"))

cont_table = pd.crosstab(df["checking_status"], df["class"])
chi2, p, dof, expected = chi2_contingency(cont_table)

print("Chi-square statistic:", chi2)
print("Degrees of freedom:", dof)   
print("P-value:", p)

checking_rates = pd.crosstab(df["checking_status"], df["class"], normalize="index")
checking_risk = (checking_rates["bad"] * 100).sort_values(ascending=False)
print("\n Checking Status Default Risk Ranking (%)")
print(checking_risk)

#duration vs loan default
duration_summary = df.groupby("class")["duration"].mean()
print(duration_summary)

bad_loans = df[df["class"] == "bad"]["duration"]
good_loans = df[df["class"] == "good"]["duration"]

t_stat, p_value = ttest_ind(bad_loans, good_loans)

print("T-statistic:", t_stat)
print("P-value:", p_value)

#box plot
plt.figure(figsize=(8, 5))
sns.boxplot(x="class", y="duration", data=df)
plt.title("Loan Duration by Loan Outcome (Good vs Bad)")
plt.xlabel("Loan Outcome")
plt.ylabel("Loan Duration (months)")
plt.tight_layout()
plt.savefig("C:/Users/janie/Documents/loan_duration_boxplot.png")
plt.show()

#column chart
default_rates = pd.crosstab(df["checking_status"], df["class"], normalize="index")
default_percent = default_rates["bad"] * 100
plt.figure(figsize=(8,5))

default_percent.plot(kind="bar")

plt.title("Default Rate by Checking Account Status")
plt.xlabel("Checking Account Status")
plt.ylabel("Default Rate (%)")
plt.xticks(rotation=45)   
plt.tight_layout()        
plt.savefig("C:/Users/janie/Documents/default_rate_by_checking_status.png")
plt.show()

#Key Insights 
print("\nKey Insights")
print("- Approximately 30% of borrowers defaulted in the dataset.")
print("- Employment status is significantly associated with loan default.")
print("- Checking account status shows the strongest relationship with default risk.")
print("- Borrowers with negative checking balances have the highest default risk.")
print("- Borrowers who default tend to have longer loan durations.")

