# Loan Default Risk Analysis

## Project Overview
This project uses the German Credit dataset to explore factors associated with loan default. The goal was to practice applying statistical methods to a real-world problem and complete a full data analysis from data exploration to interpretation.

## The Data
The dataset contains information on **1000 loan applicants in Germany**, including variables such as employment status, checking account balance, and loan duration. Each loan is labeled as either **"good" (repaid)** or **"bad" (defaulted)**. About **30% of the loans defaulted**, which was higher than I initially expected.

## Methods
I focused on three variables that seemed most relevant to loan repayment:

- **Employment status** (categorical → chi-square test)
- **Checking account balance** (categorical → chi-square test)
- **Loan duration** (numerical → independent t-test)

I also created visualizations to explore the patterns in the data, including:

- A **boxplot** comparing loan duration between good and bad loans
- A **bar chart** showing default rates across checking account status groups

## Key Findings
- **Checking account status showed the strongest relationship with loan default.** Borrowers with negative balances defaulted at nearly **50%**, while the **no checking account group had the lowest default rate (about 11.6%)**, which was unexpected.
- **Employment stability appears to matter.** Borrowers with less than one year of employment showed higher default rates than even the unemployed group.
- **Loan duration also showed a clear pattern.** Defaulted loans averaged about **5.5 months longer** than loans that were successfully repaid.

## Tools
- Python  
- pandas  
- scipy  
- matplotlib  
- seaborn  

## Project Files
- `loan_default_analysis.py` — Python code used for the analysis  
- `loan_default_analysis_report.docx` — full written analysis report  
- `loan_duration_boxplot.png` — boxplot visualization  
- `default_rate_by_checking_status.png` — bar chart visualization